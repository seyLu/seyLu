from flask import Flask, render_template

from markdown import markdown  # type: ignore[attr-defined]

app = Flask(__name__)


@app.route("/")
def index() -> str:
    with open("README.md") as f:
        md = f.read()

    return render_template(
        "index.html",
        md=markdown(
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
