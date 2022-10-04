from pathlib import Path
import re


p = Path(r'C:\workspace\mirc0_trascrizioni\rules')
rule_files = list(p.glob('**/*.cr'))

for f in rule_files:
    with open(f, "r", encoding="UTF8") as file:
        content = file.read()
        labels_list = re.findall(r'DOMAIN\[(.*?)\]|IDENTIFY\[(.*?)\]', content)
        print(labels_list, f.name)