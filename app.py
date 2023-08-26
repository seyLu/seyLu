from flask import Flask, render_template
from pymdownx import superfences

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
            extension_configs={
                "pymdownx.superfences": {
                    "custom_fences": [
                        {
                            "name": "mermaid",
                            "class": "mermaid",
                            "format": superfences.fence_div_format,
                        }
                    ]
                }
            },
        ),
    )


if __name__ == "__main__":
    app.config["SERVER_NAME"] = "flask:5000"
    app.run()
