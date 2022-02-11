import os
import sys
import json
from datetime import datetime, timedelta
from inspect import getmembers, isfunction
import requests

# Icons used for PASS or FAIL in the md file
result_icons = {"pass": "&#x1F49A;", "fail": "&#x1F534;"}
# Links for various backlog queries to be used in the md file
query_links = {}

def initialize_queries():
    with open("queries.txt", "r") as qr:
        for q in qr.readlines():
            k, v = q.split("|", 1)
            # print(k)
            # print(v)
            query_links[k] = v.strip("\n")


# Initialize a blank md file to replace the current README
def initialize_md():
    with open("index.md", "a") as md:
        md.write("# QE-C Backlog Status\n\n")
        md.write("**Latest Run:** " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " GMT\n")
        md.write("*(Please refresh to see latest results)*\n\n")

def anchor(text):
    name = text.replace("(", "").replace(")", "").replace(" ", "_").lower()
    return f"<a name='{name}'></a>"

def link(text, url):
    return f"[ {text} ]({url})"

def category_to_md(category):
    link = anchor(category)
    toMD(f"\n# {category} {link}\n")

def header_to_md(header):
    link = anchor(header)
    toMD(f"**{header} {link}**\n\n")

def byDefaultEnv(name, defaultValue):
    if name in os.environ:
        return os.environ[name]
    else:
        return defaultValue

def toMD(text):
    with open("index.md", "a") as md:
        md.write(text)

def table_header_to_md_adv(columns):
    text =  " | ".join(columns) + "\n"
    hyphens = []
    for i in columns:
        hyphens.append("---")
    text = text + " | ".join(hyphens) + "\n"
    toMD(text)

def table_results_to_md_adv(values):
    toMD(" | " + " | ".join(values) + "\n")

def query_base(query):
    key = os.environ['key']
    answer = requests.get(
        f"{query_links[query].replace('issues', 'issues.json')}"
        + f"&key={key}")
    return json.loads(answer.content)

def query_count(query):
    root = query_base(query)
    return int(root["total_count"])

def print_default_headers():
    if "category" in os.environ:
        category_to_md(os.environ["category"])
        if "category_description" in os.environ:
            toMD(os.environ["category_description"] + '\n')

    if "header" in os.environ:
        header_to_md(os.environ["header"])
        if "header_description" in os.environ:
            toMD(os.environ["header_description"] + '\n')

def print_footer():
    if "footer" in os.environ:
        toMD(os.environ["footer"] + '\n')

def open_table(columns):
    if "tb_start" in sys.argv:
        table_header_to_md_adv(columns)

def close_table():
    if "tb_end" in sys.argv:
        table_end_to_md()

def calc_icon(value1, value2, gt_icon, lt_icon):
    inverted = byDefaultEnv("inverted", False)
    if inverted is True:
        tmp = lt_icon
        lt_icon = gt_icon
        gt_icon = tmp

    if value1 > value2:
        icon = result_icons[gt_icon]
    else:
        icon = result_icons[lt_icon]

    return icon

# Customizable table
def gha_table(columns):
    print_default_headers()

    headers = []
    rows = []
    for col in columns:
        headers.append(str(col["header"]))
        if "link" in col:
            rows.append(link(str(col["text"]), col["link"]))
        else:
            rows.append(str(col["text"]))

    open_table(headers)
    table_results_to_md_adv(rows)
    close_table()
    print_footer()

# DEPRECATED Append individual results to md file
def results_to_md(a, b, c, d):
    with open("index.md", "a") as md:
        md.write("| " + a + " | " + b + " | " + c + " | " + d + "\n")

# DEPRECATED
def table_header_to_md():
    with open("index.md", "a") as md:
        md.write(
            "Backlog Query | Number of Issues | Ideal Number (min/max) | Status\n--- | --- | --- | ---\n")

def table_end_to_md():
    toMD("\n\n")

# DEPRECATED
def epic_header_to_md():
    with open("index.md", "a") as md:
        md.write(
            "Epic | Status | Start Date | Done Ratio\n--- | --- | --- | ---\n")

# DEPRECATED
def table_comp_header_to_md(a, b, c):
    with open("index.md", "a") as md:
        md.write(
            "Backlog Query | " + a + " | " + b + " | " + c + " | Status\n--- | --- | --- | --- | ---\n")

# DEPRECATED
def table_comp_results_to_md(a, b, c, d, e):
    with open("index.md", "a") as md:
        md.write("| " + a + " | " + b + " | " + c + " | " + d + " | " + e + "\n")

# DEPRECATED
def table_comp_results_to_md_withoutStatusColumn(a, b, c, d):
    with open("index.md", "a") as md:
        md.write("| " + a + " | " + b + " | " + c + " | " + d + "\n")

def gha_check():
    initialize_queries()
    
    query = os.environ['query']
    max_level = int(os.getenv('max_level', default = 0))

    issue_count = query_count(query)
    icon = calc_icon(issue_count, max_level, "fail", "pass")

    gha_table([
        {
            "header": "Backlog Query",            
            "text": query,
            "link": query_links[query]
        },
        {
            "header": "Number of issues",            
            "text": str(issue_count)
        },
        {
            "header": "Warning level",
            "text": str(max_level)
        },
        {
            "header": "Status",
            "text": icon
        }
    ])

def gha_comp():
    initialize_queries()

    issue_count_1 = query_count(os.environ['query1'])
    issue_count_2 = query_count(os.environ['query2'])
    issue_count_3 = query_count(os.environ['query3'])

    icon = calc_icon(issue_count_1, issue_count_2, "fail", "pass")

    gha_table([
        {
            "header": "Backlog Query",
            "text": os.environ["rowText"]
        },
        {
            "header": os.environ['head1'],
            "text": str(issue_count_1)
        },
        {
            "header": os.environ['head2'],
            "text": str(issue_count_2)
        },
        {
            "header": os.environ['head3'],
            "text": str(issue_count_3)
        },
        {
            "header": "Status",
            "text": icon
        }
    ])

def gha_comp_2():
    initialize_queries()

    firstColumnTitle = byDefaultEnv("firstColumnTitle", "Project")

    query1 = os.environ['query1']
    query2 = os.environ['query2']
    query3 = os.environ['query3']

    issue_count_1 = query_count(query1)
    issue_count_2 = query_count(query2)
    issue_count_3 = issue_count_1 + issue_count_2

    res1 = link(str(issue_count_1) + " (" + str(round(100*issue_count_1/issue_count_3)) + "%)", query_links[query1])
    res2 = link(str(issue_count_2) + " (" + str(round(100*issue_count_2/issue_count_3)) + "%)", query_links[query2])
    res3 = link(str(issue_count_3), query_links[query3])

    gha_table([
        {
            "header": firstColumnTitle,
            "text": os.environ["rowText"]
        },
        {
            "header": os.environ['head1'],
            "text": res1
        },
        {
            "header": os.environ['head2'],
            "text": res2
        },
        {
            "header": os.environ['head3'],
            "text": res3
        }
    ])

# Customizable check function
def gha_epics():
    initialize_queries()
    query = os.environ['query']

    print_default_headers()

    root = query_base(query)
    issue_count = int(root["total_count"])

    if issue_count <= 0:
        toMD("\n\nNo active epics for this project\n\n")
    else:
        table_header_to_md_adv(["Epic", "Status", "Start Date", "Progress"])

        for issue in root['issues']:
            epic_issue = "https://progress.opensuse.org/issues/" + str(issue['id'])
            subject = issue['subject']
            subject = subject.replace("[epic]", "").replace("[", "{").replace("]",
                                                                              "}").replace(
                "(", "{").replace(")", "}")

            if len(subject) > 53:
                subject = subject[:50] + "..."

            start = issue['start_date'] if 'start_date' in issue else "-"

            if "done_ratio" in issue:
                done = str(issue['done_ratio']) + "%"
            else:
                done = "-"

            table_results_to_md_adv([f"[{subject}]({epic_issue})", issue['status']['name'], start, done])

        table_end_to_md()
        print_footer()

def gha_description():
    text = os.environ['text']
    toMD(text)

if "init" in sys.argv:
    initialize_md()
elif "epic" in sys.argv:
    gha_epics()
elif "comp" in sys.argv:
    gha_comp()
elif "comp2" in sys.argv:
    gha_comp_2()
elif "description" in sys.argv:
    gha_description()
else:
    gha_check()
