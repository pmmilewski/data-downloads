# Script finds all labels containing keyword or text fragment
import sys
import pandas as pd

def search_label(string):
    contents = pd.read_csv("data/CRDC2013_14content.csv", encoding="Latin-1")
    name = string
    results = contents[contents["LABEL"].str.contains(name, case=False)]
    return results

def search_name(string):
    contents = pd.read_csv("data/CRDC2013_14content.csv", encoding="Latin-1")
    name = string
    results = contents[contents["NAME"].str.contains(name, case=False)]
    return results

def view_results(results):
    pd.set_option('display.max_colwidth', -1)
    pd.set_option('display.max_rows', 1000)
    print(results[["NAME", "LABEL"]])

if __name__=="__main__":
    try:
        if sys.argv[2].lower()=="name":
            view_results(search_name(sys.argv[1]))
        elif sys.argv[2].lower()=="label":
            view_results(search_label(sys.argv[1]))
        else:
            print("Wrong arguments, use python search.py [string] [label|name]")
    except IndexError:
        view_results(search_label(sys.argv[1]))
