# Student Life Manager
#### Video Demo:  <VIDEO_URL_HERE>

---

## Description
This project is a small web application built for the CS50 final project using the Flask microframework. Its purpose is to demonstrate a complete, deployable web application with user authentication, data persistence, and a simple UI that organizes and displays content (for example, assignments and an index/home page). The app intentionally keeps its scope focused so it can showcase good software design, secure user workflows, clear documentation, and maintainable code.

The application allows users to register and log in, view content specific to authenticated users, and interact with pages rendered from server-side templates. The project serves as both a learning exercise and a small production-ready prototype that can be extended with additional features (APIs, more complex models, richer UI) if desired.

## Key Features
- User registration and login with secure password handling
- Server-rendered pages using Flask templates (Jinja2)
- Data persistence with SQLAlchemy (SQLite as the default development database)
- Clear project structure separating static files, templates, and application logic
- Minimal and focused UI for demonstrating functionality (index, assignments, login/register pages)

## What the files do
Below is a short explanation of the files and folders in this repository. If you added or changed files for your specific implementation, update these descriptions accordingly.

- `app.py` — The main Flask application module. It defines the Flask app instance, routes (for example `/`, `/login`, `/register`, `/assignments`), and the application entry point. It also wires together configuration and the database.
- `models.py` — Contains the SQLAlchemy model definitions used by the app (for example a `User` model and any models used to represent assignments or content).
- `requirements.txt` — Lists Python package dependencies required to run the project (e.g., Flask, Flask-SQLAlchemy, Werkzeug). Install these into a virtual environment prior to running the app.
- `static/` — Static assets such as `styles.css`. These are served directly by Flask during development.
- `templates/` — HTML templates (e.g., `layout.html`, `index.html`, `login.html`, `register.html`, `assignments.html`). These templates use Jinja2 templating and provide the app's UI.
- `instance/` — Optional folder for instance-specific configuration and the SQLite database file (if used). This folder is not committed with sensitive production configuration values.
- `__pycache__/` — Python bytecode cache (auto-generated; typically excluded from version control).

## Design decisions and trade-offs
- Framework: I chose Flask because it’s lightweight, well-suited to small projects, and is the framework used throughout CS50’s web curriculum.
- Database: SQLAlchemy (with SQLite in development) is used for reliability and ease of deployment. SQLite keeps the setup simple and portable for grading and demos.
- Server-side rendering: Templates keep complexity low and make it easy to demonstrate rendering logic, authentication flows, and form handling without building a client-side framework.
- Security: Passwords should be hashed using appropriate functions (e.g., Werkzeug utilities). Sessions are used to track signed-in users. For a production deployment, additional hardening (HTTPS, secure cookies, more strict config) would be required.

These choices aim to strike a balance between clarity for reviewers (and graders) and practical, maintainable architecture.

## Installation & Setup (Windows)
1. Clone or copy this repository to your local machine.
2. Open a terminal and create a virtual environment:

```powershell
python -m venv venv
```

3. Activate the virtual environment:

- PowerShell:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force
.\venv\Scripts\Activate.ps1
```
- CMD:
```cmd
venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. (Optional) If your app relies on a database file or environment variables, create them now. By default the app uses a local SQLite file (commonly stored in `instance/`).

6. Run the app:

```bash
# If app.py exposes a Flask app and runs when executed
python app.py
# or use flask run (after setting FLASK_APP)
# set FLASK_APP=app.py
# flask run
```

7. Open your browser and go to `http://127.0.0.1:5000/`.

## Usage
- Register a new user via the **Register** page.
- Log in with the registered credentials and navigate the site.
- Visit the **Assignments** page to see example content that is part of the app.
- Use the UI to test typical user flows, and consult the server logs for debug information during development.

## Testing and Validation
There are no automated tests included in this template. For a more robust project, consider adding unit tests for models and integration tests for routes using Flask’s test client. Manual testing should exercise registration/login flows, form validation, and database persistence.

## Known issues and future improvements
- Add a REST API for programmatic access to assignments or resources.
- Improve frontend with client-side validation and better mobile responsiveness.
- Add automated tests and CI for continuous validation.
- Harden security for production: add HTTPS, set cookie flags, and configure secrets management.

## Credits & Acknowledgements
This project follows the CS50 web development course patterns and is intended as a final project submission. Thanks to the CS50 staff and material for the foundational guidance.

---

If you’d like, I can fill in the **Project Title** and the **Video Demo URL** for you and tailor the description to specific features you implemented — just tell me your project title and paste your video URL (YouTube or similar), and I’ll update the file. ✅
