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
def results_to_md(item, number, limits, status):
    with open("index.md", "a") as md:
        md.write("| " + item + " | " + number + " | " + limits + " | " + status + "\n")


def category_to_md(category):
    with open("index.md", "a") as md:
        md.write(f"\n# {category}\n")


def header_to_md(header):
    with open("index.md", "a") as md:
        md.write(f"**{header}**\n")


def table_header_to_md():
    with open("index.md", "a") as md:
        md.write(
            "Backlog Query | Number of Issues | Ideal Number | Status\n--- | --- | --- | ---\n")


def table_end_to_md():
    with open("index.md", "a") as md:
        md.write("\n\n")


# Customizable check function
def gha_check():
    initialize_queries()
    key = os.environ['key']
    query = os.environ['query']
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
    if issue_count > 0:
        print(f"Backlog has {query} tickets!")
        print(f"Please check {query_links[query]}")
        results_to_md(
            f"[{query}]({query_links[query]})",
                      str(issue_count), "0", result_icons["fail"])
        if "tb_end" in sys.argv:
            table_end_to_md()
        exit(1)
    print(f"{query} length is 0, all good!")
    results_to_md(f"[{query}]({query_links[query]})",
                  "0", "0", result_icons["pass"])
    if "tb_end" in sys.argv:
        table_end_to_md()


functions = {name: obj for name, obj in getmembers(sys.modules[__name__]) if (isfunction(
    obj) and name.startswith("gha"))}
if "init" in sys.argv:
    initialize_md()
else:
    gha_check()
