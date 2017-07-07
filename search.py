# Script finds all labels containing keyword or text fragment
import sys
import pandas as pd
import re

if __name__=="__main__":
	contents = pd.read_csv("data/CRDC2013_14content.csv", encoding="Latin-1")
	name = sys.argv[1]
	labels = contents[contents["LABEL"].str.contains(name, case=False)]
	pd.set_option('display.max_colwidth', -1)
	print(labels[["NAME", "LABEL"]])
