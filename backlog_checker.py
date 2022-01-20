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
            print(k)
            print(v)
            query_links[k] = v.strip("\n")


# Initialize a blank md file to replace the current README
def initialize_md():
    with open("index.md", "a") as md:
        md.write("# QE-C Backlog Status\n\n")
        md.write("**Latest Run:** " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " GMT\n")
        md.write("*(Please refresh to see latest results)*\n\n")


# Append individual results to md file
def results_to_md(a, b, c, d):
    with open("index.md", "a") as md:
        md.write("| " + a + " | " + b + " | " + c + " | " + d + "\n")


def category_to_md(category):
    with open("index.md", "a") as md:
        md.write(f"\n# {category}\n")


def header_to_md(header):
    with open("index.md", "a") as md:
        md.write(f"**{header}**\n")


def table_header_to_md():
    with open("index.md", "a") as md:
        md.write(
            "Backlog Query | Number of Issues | Ideal Number (min/max) | Status\n--- | --- | --- | ---\n")

def table_end_to_md():
    with open("index.md", "a") as md:
        md.write("\n\n")

def epic_header_to_md():
    with open("index.md", "a") as md:
        md.write(
            "Epic | Status | Start Date | Done Ratio\n--- | --- | --- | ---\n")

def table_comp_header_to_md(a, b, c):
    with open("index.md", "a") as md:
        md.write(
            "Backlog Query | " + a + " | " + b + " | " + c + " | Status\n--- | --- | --- | --- | ---\n")

def table_comp_results_to_md(a, b, c, d, e):
    with open("index.md", "a") as md:
        md.write("| " + a + " | " + b + " | " + c + " | " + d + " | " + e + "\n")

# Customizable check function
def gha_check():
    initialize_queries()
    key = os.environ['key']
    query = os.environ['query']
    max_level = int(os.getenv('max_level', default = 0))
    if "category" in os.environ:
        category_to_md(os.environ["category"])
    if "header" in os.environ:
        header_to_md(os.environ["header"])
    if "tb_start" in sys.argv:
        table_header_to_md()
    answer = requests.get(
        f"{query_links[query].replace('issues', 'issues.json')}"
        + f"&key={key}")
    root = json.loads(answer.content)
    issue_count = int(root["total_count"])
    if issue_count > max_level:
        print(f"Backlog has {query} tickets!")
        print(f"Please check {query_links[query]}")
        results_to_md(
            f"[{query}]({query_links[query]})",
                      str(issue_count), str(max_level), result_icons["fail"])
        if "tb_end" in sys.argv:
            table_end_to_md()
        exit(1)
    print(f"{query} length is {issue_count}, all good!")
    results_to_md(f"[{query}]({query_links[query]})",
                  str(issue_count), str(max_level), result_icons["pass"])
    if "tb_end" in sys.argv:
        table_end_to_md()

def gha_comp():
    initialize_queries()
    key = os.environ['key']
    rowText = os.environ["rowText"]

    if "category" in os.environ:
        category_to_md(os.environ["category"])
    if "header" in os.environ:
        header_to_md(os.environ["header"])
    if "tb_start" in sys.argv:
        table_comp_header_to_md(os.environ['head1'], os.environ['head2'], os.environ['head3'])

    query1 = os.environ['query1']
    answer1 = requests.get(
        f"{query_links[query1].replace('issues', 'issues.json')}"
        + f"&key={key}")
    root1 = json.loads(answer1.content)
    issue_count_1 = int(root1["total_count"])

    query2 = os.environ['query2']    
    answer2 = requests.get(
        f"{query_links[query2].replace('issues', 'issues.json')}"
        + f"&key={key}")
    root2 = json.loads(answer2.content)
    issue_count_2 = int(root2["total_count"])

    query3 = os.environ['query3']    
    answer3 = requests.get(
        f"{query_links[query3].replace('issues', 'issues.json')}"
        + f"&key={key}")
    root3 = json.loads(answer3.content)
    issue_count_3 = int(root3["total_count"])

    print(f"{rowText} where {issue_count_1} <= {issue_count_2}")

    if issue_count_1 > issue_count_2:
        table_comp_results_to_md(rowText, str(issue_count_1), str(issue_count_2), str(issue_count_3), result_icons["fail"])
        if "tb_end" in sys.argv:
            table_end_to_md()
        exit(1)

    print(f"{rowText} where {issue_count_1} <= {issue_count_2}, all good!")
    table_comp_results_to_md(rowText,
                  str(issue_count_1), str(issue_count_2), str(issue_count_3), result_icons["pass"])

    if "tb_end" in sys.argv:
        table_end_to_md()

def gha_check_inverted():
    initialize_queries()
    key = os.environ['key']
    query = os.environ['query']
    min_level = int(os.getenv('min_level', default = 1))
    if "category" in os.environ:
        category_to_md(os.environ["category"])
    if "header" in os.environ:
        header_to_md(os.environ["header"])
    if "tb_start" in sys.argv:
        table_header_to_md()
    answer = requests.get(
        f"{query_links[query].replace('issues', 'issues.json')}"
        + f"&key={key}")
    root = json.loads(answer.content)
    issue_count = int(root["total_count"])
    if issue_count < min_level:
        print(f"Backlog has {query} tickets!")
        print(f"Please check {query_links[query]}")
        results_to_md(
            f"[{query}]({query_links[query]})",
                      str(issue_count), str(min_level), result_icons["fail"])
        if "tb_end" in sys.argv:
            table_end_to_md()
        exit(1)
    print(f"{query} length is {issue_count}, all good!")
    results_to_md(f"[{query}]({query_links[query]})",
                  str(issue_count), str(min_level), result_icons["pass"])
    if "tb_end" in sys.argv:
        table_end_to_md()


# Customizable check function
def gha_epics():
    initialize_queries()
    key = os.environ['key']
    query = os.environ['query']
    if "category" in os.environ:
        category_to_md(os.environ["category"])
    header_to_md(os.environ["header"])
    answer = requests.get(
        f"{query_links[query].replace('issues', 'issues.json')}"
        + f"&key={key}")
    root = json.loads(answer.content)
    issue_count = int(root["total_count"])
    if issue_count <= 0:
        with open("index.md", "a") as md:
            md.write("\n\nNo active epics for this project\n\n")
    else:
        epic_header_to_md()
        for issue in root['issues']:
            epic_issue = "https://progress.opensuse.org/issues/" + str(issue['id'])
            subject = issue['subject']
            subject = subject.replace("[epic]", "").replace("[", "{").replace("]",
                                                                              "}").replace(
                "(", "{").replace(")", "}")
            if len(subject) > 53:
                subject = subject[:50] + "..."
            print(issue['status']['name'])
            start = issue['start_date'] if 'start_date' in issue else "-"
            if "done_ratio" in issue:
                done = str(issue['done_ratio']) + "%"
            else:
                done = "-"
            results_to_md(f"[{subject}]({epic_issue})", issue['status']['name'], start, done)
        table_end_to_md()


if "init" in sys.argv:
    initialize_md()
elif "epic" in sys.argv:
    gha_epics()
elif "comp" in sys.argv:
    gha_comp()
elif "inverted" in sys.argv:
    gha_check_inverted()
else:
    gha_check()
