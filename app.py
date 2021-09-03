from flask import Flask, render_template
from datetime import date
from resume import ed_experiences, w_experiences
from project_details import *

app = Flask(__name__)

title = "Simone Martin"

now = date.today()
current_year = now.year
email = "martin.s.marotta@gmail.com"
location = "Naples, IT"
skype = "martin.s.marotta@gmail.com"

social_buttons = [
    # url, href class, i class
    ("https://github.com/c0pper/", "github", "bx bxl-github"),
    ("https://www.instagram.com/sim01110011.01101001.01101101/", "instagram", "bx bxl-instagram"),
    ("https://www.youtube.com/channel/UCtUNRX-B_j2ipkL1Lihih8w/", "youtube", "bx bxl-youtube"),
    ("https://www.facebook.com/Simooon/", "facebook", "bx bxl-facebook")
]

navmenu = [
    ("#hero", "bx bx-home", "Home"),
    ("#about", "bx bx-user", "About"),
    ("#skills", "bx bx-user", "Skills"),
    ("#resume", "bx bx-file-blank", "Resume"),
    ("#projects", "bx bx-book-content", "Projects"),
    ("#contact", "bx bx-envelope", "Contact")
]

lang_skills = [("english", 100), ("Russian", 70), ("SPANISH", 30), ("FRENCH", 30), ("JAPANESE", 20)]
comp_skills = [("PHOTOSHOP", 80), ("HTML", 70), ("PYTHON", 50), ("WORDPRESS/CMS", 50), ("CSS", 30)]

projects = [  # Title, img, url
    (zettibot["title"], "zettibot.png", "zettibot-ai"),
    (pers_website["title"], "personal_website.png", "personal-website"),
    (python_cv["title"], "pycv.png", "py-cv"),
    (anime_scraper["title"], "animedownloader.png", "anime-downloader"),
    # ("Text Collection", "karman.png", "text-collection"),
    (karman_line["title"], "karman.png", "karman-line"),
    (win95_site["title"], "win95.png", "win95-site"),
    (spacex_it["title"], "starman.png", "spacex-it"),
    (gta_napoli["title"], "gta.png", "gta-napoli"),
    (unidia["title"], "unidia.png", "unidia"),
    (mirai_subs["title"], "mirai.png", "mirai-subs"),
    (clients_app["title"], "clients.png", "clients-app"),
    (nmusic_app["title"], "nmusic.png", "nmusic-app")
]


def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))

    return age


@app.route("/")
def home():
    return render_template(
        "index.html",
        title=title,
        social_buttons=social_buttons,
        navmenu=navmenu,
        email=email,
        location=location,
        skype=skype,
        age=calculateAge(date(1993, 9, 4)),
        copyright_year=current_year,
        lang_skills=lang_skills,
        comp_skills=comp_skills,
        ed_experiences=ed_experiences,
        w_experiences=w_experiences,
        projects=projects
    )


@app.route("/zettibot-ai")
def zettibot_ai():
    return render_template(
        "project_base.html",
        title=zettibot["title"],
        copyright_year=current_year,
        social_buttons=social_buttons,
        navmenu=navmenu,
        data=zettibot
    )


@app.route("/personal-website")
def personal_website():
    return render_template(
        "project_base.html",
        title=pers_website["title"],
        copyright_year=current_year,
        social_buttons=social_buttons,
        navmenu=navmenu,
        data=pers_website
    )


@app.route("/py-cv")
def pyCV():
    return render_template(
        "project_base.html",
        title=python_cv["title"],
        copyright_year=current_year,
        social_buttons=social_buttons,
        navmenu=navmenu,
        data=python_cv
    )


@app.route("/anime-downloader")
def anime_downloader():
    return render_template(
        "project_base.html",
        title=anime_scraper["title"],
        copyright_year=current_year,
        social_buttons=social_buttons,
        navmenu=navmenu,
        data=anime_scraper
    )


@app.route("/text-collection")
def text_collection():
    return render_template(
        "project_base.html",
        title=text_collect["title"],
        copyright_year=current_year,
        social_buttons=social_buttons,
        navmenu=navmenu,
        data=text_collect
    )


@app.route("/karman-line")
def karman():
    return render_template(
        "project_base.html",
        title=karman_line["title"],
        copyright_year=current_year,
        social_buttons=social_buttons,
        navmenu=navmenu,
        data=karman_line
    )


@app.route("/win95-site")
def win95():
    return render_template(
        "project_base.html",
        title=win95_site["title"],
        copyright_year=current_year,
        social_buttons=social_buttons,
        navmenu=navmenu,
        data=win95_site
    )


@app.route("/spacex-it")
def spacex():
    return render_template(
        "project_base.html",
        title=spacex_it["title"],
        copyright_year=current_year,
        social_buttons=social_buttons,
        navmenu=navmenu,
        data=spacex_it
    )


@app.route("/gta-napoli")
def gta():
    return render_template(
        "project_base.html",
        title=gta_napoli["title"],
        copyright_year=current_year,
        social_buttons=social_buttons,
        navmenu=navmenu,
        data=gta_napoli
    )


@app.route("/unidia")
def uni():
    return render_template(
        "project_base.html",
        title=unidia["title"],
        copyright_year=current_year,
        social_buttons=social_buttons,
        navmenu=navmenu,
        data=unidia
    )


@app.route("/mirai-subs")
def mirai():
    return render_template(
        "project_base.html",
        title=mirai_subs["title"],
        copyright_year=current_year,
        social_buttons=social_buttons,
        navmenu=navmenu,
        data=mirai_subs
    )


@app.route("/clients-app")
def clients():
    return render_template(
        "project_base.html",
        title=clients_app["title"],
        copyright_year=current_year,
        social_buttons=social_buttons,
        navmenu=navmenu,
        data=clients_app
    )


@app.route("/nmusic-app")
def nmusic():
    return render_template(
        "project_base.html",
        title=nmusic_app["title"],
        copyright_year=current_year,
        social_buttons=social_buttons,
        navmenu=navmenu,
        data=nmusic_app
    )


if __name__ == "__main__":
    app.run(debug=True)
