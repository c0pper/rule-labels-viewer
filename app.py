from flask import Flask, redirect, url_for, render_template
from datetime import date
from project_details import *

app = Flask(__name__)

title = "Simone Martin"

now = date.today()
current_year = now.year
email = "martin.s.marotta@gmail.com"
location = "Naples, IT"
skype = "martin.s.marotta@gmail.com"

navmenu = [("#hero", "bx bx-home", "Home"),
("#about", "bx bx-user", "About"),
("#skills", "bx bx-user", "Skills"),
("#resume", "bx bx-file-blank", "Resume"),
("#projects", "bx bx-book-content", "Projects"),
("#contact", "bx bx-envelope", "Contact")]

lang_skills = [("english", 100), ("Russian", 70), ("SPANISH", 30), ("FRENCH", 30), ("JAPANESE", 20)]
comp_skills = [("PHOTOSHOP", 80), ("HTML", 70), ("PYTHON", 50), ("WORDPRESS/CMS", 50), ("CSS", 30)]

projects = [("The Karman Line", "portfolio-1.jpg", "karman-line"),
("This website. Like it's '95.", "portfolio-1.jpg", "karman-line"),
("SpaceX Website italian localisation", "portfolio-1.jpg", "karman-line"),
("GTA Napoli", "portfolio-1.jpg", "karman-line"),
("Unidia", "portfolio-1.jpg", "karman-line"),
("'Mirai' Substitles", "portfolio-1.jpg", "karman-line"),
("'Clients' localisation", "portfolio-1.jpg", "karman-line"),
("'NMusic' localisation", "portfolio-1.jpg", "karman-line")
]


def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
 
    return age


@app.route("/")
def home():
    return render_template("index.html",
    title=title,
    navmenu=navmenu,
    email=email,
    location=location,
    skype=skype,
    age=calculateAge(date(1993, 9, 4)),
    copyright_year=current_year,
    lang_skills=lang_skills,
    comp_skills=comp_skills,
    projects=projects
    )


@app.route("/karman-line")
def base():
    return render_template("karman-line.html",
    title="The Karman Line",
    copyright_year=current_year,
    navmenu=navmenu,
    data=karman_line
    )


if __name__ == "__main__":
    app.run(debug=True)