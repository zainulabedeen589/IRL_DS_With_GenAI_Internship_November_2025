from flask import Flask, request

app = Flask(__name__)


@app.route("/greet")
def uppercase_name():
    # Fetch the 'name' from query parameters (e.g., /greet?name=john)
    user_name = request.args.get("name")

    if user_name:
        # Convert to upper case
        upper_name = user_name.upper()
        return f"<h1>Hello, {upper_name}!</h1>"
    else:
        return "<h1>Please provide a name in the URL (e.g., /greet?name=yourname)</h1>"


if __name__ == "__main__":
    app.run(debug=True)
