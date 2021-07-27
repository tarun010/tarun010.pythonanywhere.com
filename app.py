import os
from pathlib import Path

from flask import Flask, render_template
import requests
import decouple

user_name = "Tarun"

github_projects_url = decouple.config("GITHUB_API", default=None)
projects_from_github = requests.get(github_projects_url).json()

contact = decouple.config("CONTACT_FORM_API", default=None)

projects = []

with os.scandir("blog") as it:
    for entry in it:
        if entry.name.endswith(".md") and entry.is_file():
            print(entry.name, entry.path)

            post_data = Path(entry.path).read_text()
            print(post_data)

exit(0)


for project in projects_from_github:
    name = project["name"]
    desc = project["description"]
    url = project["html_url"]

    projects.append({
        "name": name,
        "desc": desc,
        "url": url
    })

print(projects)



#list_of_food = [
#    "Tea",
#    "Apples",
#    "Ramen"
#]

app = Flask(__name__)

@app.route("/")
def about_page():
    return render_template("about.html", name=user_name)#, list_of_food=list_of_food)

@app.route("/blog")
def blog_list_page():
    return render_template("blog_list.html", name=user_name)

@app.route("/blog/<post_name>")
def blog_entry_page(post_name):
    return render_template("blog_entry.html", name=user_name, post_name=post_name)


@app.route("/projects")
def project_page():
    return render_template("projects.html", name=user_name, projects=projects)

@app.route("/contact")
def contact_page():
    return render_template("contact.html", name=user_name, api=contact)
