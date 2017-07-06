import sys
import pandas as pd

if __name__=="__main__":
	contents = pd.read_csv("data/CRDC2013_14content.csv", encoding="Latin-1")
	name = sys.argv[1]
	label = contents[contents["NAME"]==name]["LABEL"]
	print(name + "	" +label.values[0])
	
