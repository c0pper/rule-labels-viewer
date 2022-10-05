from flask import Flask, render_template
from pathlib import Path
import re

app = Flask(__name__)

title = "Simone Martin"

rules_folder = input("Insert rules folder path: ")
p = Path(rules_folder)
rule_files = list(p.glob('**/*.cr'))

labels = []
for f in rule_files:
    with open(f, "r", encoding="UTF8") as file:
        content = file.read()
        cat_labels_list = re.findall(r'DOMAIN\[(.*?)\]', content)
        xtr_labels_list = re.findall(r'IDENTIFY\[(.*?)\]', content)

    single_doc = {}
    single_doc["doc"] = f.name
    single_doc["cat_labels"] = cat_labels_list
    single_doc["xtr_labels"] = xtr_labels_list
    labels.append(single_doc)


@app.route("/")
def home():
    return render_template(
        "index.html",
        title=title,
        labels=labels
    )



if __name__ == "__main__":

    app.run(debug=True)
