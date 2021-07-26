from flask import Flask, render_template

app = Flask(__name__)

name = "Tarun"

@app.route("/")
def about_page():
    return render_template("about.html", name=name)

@app.route("/contact")
def contact_page():
    return render_template("contact.html", name=name)

@app.route("/projects")
def project_page():
    return render_template("projects.html", name=name)

@app.route("/blog")
def blog_page():
    return render_template("blog.html", name=name)
