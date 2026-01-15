import sqlite3
import string
import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Database initialization
def init_db():
    conn = sqlite3.connect("urls.db")
    db = conn.cursor()
    db.execute("""CREATE TABLE IF NOT EXISTS web_urls 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  long_url TEXT NOT NULL, 
                  short_code TEXT NOT NULL UNIQUE)""")
    conn.commit()
    conn.close()


# 6 characters ka random short code banane ke liye
def generate_short_code():
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for i in range(6))


@app.route("/", methods=["GET", "POST"])
def index():
    short_url = None
    if request.method == "POST":
        long_url = request.form["long_url"]
        short_code = generate_short_code()

        conn = sqlite3.connect("urls.db")
        db = conn.cursor()
        try:
            db.execute(
                "INSERT INTO web_urls (long_url, short_code) VALUES (?, ?)",
                (long_url, short_code),
            )
            conn.commit()
            short_url = request.host_url + short_code
        except sqlite3.IntegrityError:
            # Agar code repeat ho jaye to dobara generate karega
            return index()
        finally:
            conn.close()

    return render_template("index.html", short_url=short_url)


@app.route("/<short_code>")
def redirect_to_url(short_code):
    conn = sqlite3.connect("urls.db")
    db = conn.cursor()
    db.execute("SELECT long_url FROM web_urls WHERE short_code=?", (short_code,))
    row = db.fetchone()
    conn.close()

    if row:
        return redirect(row[0])
    return "<h1>URL Not Found</h1>", 404


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
