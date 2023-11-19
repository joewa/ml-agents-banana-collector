# Python script to make the documentation
import os
import shutil
from ghp_import import ghp_import


docsdir = "docs"
shutil.copyfile("README.md", os.path.join(docsdir, "README.md"))
shutil.copytree("assets", os.path.join(docsdir, "assets"), dirs_exist_ok=True)
os.system("jupyter-book clean docs")
os.system("jupyter-book build docs")
ghp_import(os.path.join(docsdir, "_build", "html"), nojekyll=True, push=True)
