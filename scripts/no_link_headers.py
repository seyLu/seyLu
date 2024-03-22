#!/usr/bin/env python

"""
Add zero-width character to disable header links.
"""

__author__ = "seyLu"
__github__ = "github.com/seyLu"

__licence__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "seyLu"
__status__ = "Prototype"

import re

if __name__ == "__main__":
    pattern: str = r"<h[1-6]( align=\"center\")?>"
    replacement: str = r"\g<0><a href=\"#\">&#x200B;</a>"

    readme_content: str = ""
    with open("README.md") as f:
        readme_content = re.sub(pattern, replacement, f.read())

    with open("README.md", "w") as f:
        f.write(readme_content)
