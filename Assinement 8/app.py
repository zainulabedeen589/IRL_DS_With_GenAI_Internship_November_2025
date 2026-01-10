from flask import Flask, render_template, request
import re

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    test_string = ""
    regex_pattern = ""

    if request.method == "POST":
        test_string = request.form.get("test_string")
        regex_pattern = request.form.get("regex_pattern")

        try:
            # Find all matches using the re module
            results = re.findall(regex_pattern, test_string)
        except re.error as e:
            results = [f"Invalid Regex Error: {e}"]

    return render_template(
        "index.html",
        results=results,
        test_string=test_string,
        regex_pattern=regex_pattern,
    )


if __name__ == "__main__":
    app.run(debug=True)
