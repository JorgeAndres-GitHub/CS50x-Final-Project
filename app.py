from flask import Flask, jsonify, request, render_template, session, redirect, url_for
from models import Subject, Task, User, db
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
from datetime import datetime

app = Flask(__name__)
app.secret_key = "super-secret-key"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
@login_required
def hello():
    user_id = session["user_id"]
    subjects = Subject.query.filter_by(user_id=user_id).all()
    tasks = Task.query.filter_by(user_id=user_id).all()
    return render_template('index.html', subjects=subjects, tasks=tasks)

@app.route("/login", methods=["POST", "GET"])
def login():
    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return "Username and password required", 400

        user = User.query.filter_by(username = username).first()

        if not user or not check_password_hash(user.password_hash, password):
            return "Invalid credentials", 401

        session["user_id"] = user.id
        return redirect("/")
    
    return render_template("login.html")

@app.route("/register", methods=["POST", "GET"])
def register():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username or not password:
            return "Username and password required", 400

        if password != confirmation:
            return "Passwords do not match", 400

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return "Username already taken", 409

        
        password_hash = generate_password_hash(password)

        new_user = User(username=username, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()

        session["user_id"] = new_user.id
        return redirect("/")

    return render_template("register.html")


@app.route("/logout")
def logout():
    session.clear()

    return redirect("/")


@app.route("/subjects", methods=["POST"])
@login_required
def add_subject():
    user_id = session["user_id"]
    name = request.form.get("name")

    if not name:
        return "Subject name required", 400

    new_subject = Subject(name=name, user_id=user_id)
    db.session.add(new_subject)
    db.session.commit()

    return redirect("/")

@app.route("/delete_subject/<int:subject_id>", methods=["POST"])
@login_required
def delete_subject(subject_id):
    user_id = session["user_id"]

    subject = Subject.query.filter_by(id=subject_id, user_id=user_id).first()
    if not subject:
        return "Subject not found", 404

    Task.query.filter_by(subject_id=subject.id).delete()
    db.session.delete(subject)
    db.session.commit()

    return redirect("/")

@app.route("/assignments/<int:subject_id>")
@login_required
def assignments(subject_id):
    user_id = session["user_id"]
    subject = Subject.query.filter_by(id=subject_id, user_id=user_id).first()
    if not subject:
        return "Subject not found", 404

    tasks = Task.query.filter_by(subject_id=subject.id, user_id=user_id).all()
    return render_template("assignments.html", subject=subject, tasks=tasks)

@app.route("/tasks", methods=["POST"])
@login_required
def add_task():
    user_id = session["user_id"]
    title = request.form.get("title")
    description = request.form.get("description")
    due_date_str  = request.form.get("due_date")
    subject_id = request.form.get("subject_id")

    if not title or not subject_id:
        return "Title and Subject required", 400
    
    due_date = None
    if due_date_str:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()

    new_task = Task(title=title, description=description, due_date=due_date if due_date else None, subject_id=subject_id, user_id=user_id)
    db.session.add(new_task)
    db.session.commit()

    return redirect(f"/assignments/{subject_id}")


@app.route("/tasks/<int:task_id>/complete", methods=["POST"])
@login_required
def complete_task(task_id):
    user_id = session["user_id"]

    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if not task:
        return "Task not found", 404

    # Mark as completed
    task.completed = True
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return f"Database error: {e}", 500

    return redirect(url_for("assignments", subject_id=task.subject_id))