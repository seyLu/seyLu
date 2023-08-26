from flask import Flask, render_template
from livereload import Server

from markdown import markdown

app = Flask(__name__)


@app.route("/")
def index():
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
    app.debug = True

    server = Server(app.wsgi_app)
    server.watch("markdown/", "python scripts/readme.py")
    server.serve()
