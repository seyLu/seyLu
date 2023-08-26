from flask import Flask, render_template

import markdown

app = Flask(__name__)


@app.route("/")
def index():
    with open("README.md") as f:
        md = f.read()

    return render_template(
        "index.html",
        md=markdown.markdown(
            md,
            extensions=[
                "pymdownx.superfences",
                "codehilite",
                "tables",
            ],
        ),
    )


if __name__ == "__main__":
    app.config["SERVER_NAME"] = "flask:5000"
    app.run()
