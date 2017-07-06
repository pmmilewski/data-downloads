import pandas as pd

if __name__=="__main__":
    data = pd.read_csv("data/CRDC2013_14.csv", encoding="Latin-1")
    data["total_enrollment"] = data["TOT_ENR_M"] + data["TOT_ENR_F"]
    races = ["HI", "AM", "AS", "HP", "BL", "WH", "TR"]
    genders = ["F", "M"]
    rgenr = dict()
    for r in races:
        rgenr["SCH_ENR_"+r] = data["SCH_ENR_"+r+"_M"].sum() + data["SCH_ENR_"+r+"_F"].sum()
        for g in genders:
            rgenr["SCH_ENR_"+r+"_"+g] = data["SCH_ENR_"+r+"_"+g].sum()
    all_enrollment = data["total_enrollment"].sum()
    prgenr = {k: v / all_enrollment * 100 for k, v in rgenr.items()}
    for k,v in prgenr.items():
        print(str(k) + ": " + str(v) + "%") 