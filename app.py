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

projects = [("The Karman Line", "karman.png", "karman-line"),
("This website. Like it's '95.", "win95.png", "win95-site"),
("SpaceX Website italian localisation", "spacex.png", "spacex-it"),
("GTA Napoli", "gta.png", "gta-napoli"),
("Unidia", "unidia.png", "unidia"),
("'Mirai' Substitles", "mirai.png", "mirai-subs"),
("'Clients' localisation", "clients.png", "clients-app"),
("'NMusic' localisation", "nmusic.png", "nmusic-app")
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
def karman():
    return render_template("karman-line.html",
    title="The Karman Line",
    copyright_year=current_year,
    navmenu=navmenu,
    data=karman_line
    )

@app.route("/win95-site")
def win95():
    return render_template("win95-site.html",
    title="This website Windows 95ed",
    copyright_year=current_year,
    navmenu=navmenu,
    data=win95_site
    )

@app.route("/spacex-it")
def spacex():
    return render_template("spacex-it.html",
    title="SpaceX Italian Localisation",
    copyright_year=current_year,
    navmenu=navmenu,
    data=spacex_it
    )

@app.route("/gta-napoli")
def gta():
    return render_template("gta-napoli.html",
    title="GTA Napoli",
    copyright_year=current_year,
    navmenu=navmenu,
    data=gta_napoli
    )

@app.route("/unidia")
def uni():
    return render_template("unidia.html",
    title="Unidia",
    copyright_year=current_year,
    navmenu=navmenu,
    data=unidia
    )

@app.route("/mirai-subs")
def mirai():
    return render_template("mirai-subs.html",
    title="Mirai Subtitles",
    copyright_year=current_year,
    navmenu=navmenu,
    data=mirai_subs
    )

@app.route("/clients-app")
def clients():
    return render_template("clients-app.html",
    title="Clients App Localisation",
    copyright_year=current_year,
    navmenu=navmenu,
    data=clients_app
    )

@app.route("/nmusic-app")
def nmusic():
    return render_template("nmusic-app.html",
    title="NMusic App Localisation",
    copyright_year=current_year,
    navmenu=navmenu,
    data=nmusic_app
    )


if __name__ == "__main__":
    app.run(debug=True)