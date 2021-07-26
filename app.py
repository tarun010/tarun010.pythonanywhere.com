from flask import Flask, render_template
import requests


user_name = "Tarun"

github_projects_url = "https://api.github.com/users/tarun010/repos"
projects_from_github = requests.get(github_projects_url).json()

projects = []

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



list_of_food = [
    "Tea",
    "Apples",
    "Ramen"
]

app = Flask(__name__)

@app.route("/")
def about_page():
    return render_template("about.html", name=user_name, list_of_food=list_of_food)

@app.route("/contact")
def contact_page():
    return render_template("contact.html", name=user_name)

@app.route("/projects")
def project_page():
    return render_template("projects.html", name=user_name, projects=projects)

@app.route("/blog")
def blog_page():
    return render_template("blog.html", name=user_name)
