import json

with open('candidates.json', 'r') as fp:
    data = json.load(fp)


def main_page():
    str_candidates = ""
    for d in data:
        str_candidates += f'''<pre>Имя кандидата - {d["name"]}\nПозиция кандидата - {d["position"]}\nНавыки - {d["skills"]}\n</pre>'''
    return str_candidates


def candidates_page(num):
    num = int(num) - 1
    return f'''<img src={data[num]["picture"]}> <pre>Имя кандидата - {data[num]["name"]}\nПозиция кандидата - {data[num]["position"]}\nНавыки - {data[num]["skills"]}\n</pre>'''


def skills_page(skill):
    skills_str = ""
    for d in data:
        list_skill = d["skills"].lower().split(", ")
        if skill.lower() in list_skill:
            skills_str += f'''<pre>Имя кандидата - {d["name"]}\nПозиция кандидата - {d["position"]}\nНавыки - {d["skills"]}\n</pre>'''
    return skills_str
