from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random
import string
import validators

app = Flask(__name__)

# Database Configuration (SQLite)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///urls.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# Database Model
class URLMapping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)


# Short code generate karne ka function
def generate_short_code():
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(6))


# Database create karein
with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def home():
    short_url = None
    error = None
    if request.method == "POST":
        original = request.form.get("url")

        # URL Verification (Googled Method)
        if not validators.url(original):
            error = "Invalid URL! Please enter a valid URL (e.g., https://google.com)"
        else:
            # Check if URL already exists
            existing = URLMapping.query.filter_by(original_url=original).first()
            if existing:
                code = existing.short_code
            else:
                code = generate_short_code()
                new_url = URLMapping(original_url=original, short_code=code)
                db.session.add(new_url)
                db.session.commit()

            short_url = request.host_url + code

    return render_template("home.html", short_url=short_url, error=error)


# History Page
@app.route("/history")
def history():
    all_urls = URLMapping.query.all()
    return render_template("history.html", urls=all_urls)


# Redirect Function
@app.route("/<code Charl>")
def redirect_to_url(code):
    mapping = URLMapping.query.filter_by(short_code=code).first_or_404()
    return redirect(mapping.original_url)


if __name__ == "__main__":
    app.run(debug=True)
