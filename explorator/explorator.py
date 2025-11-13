import pandas as pd

df_parcours_explorateurs = pd.read_csv("parcours_explorateurs.csv")

explorators_start = df_parcours_explorateurs.loc[
    df_parcours_explorateurs["type_aretes"] == "depart",
    "noeud_amont"
].tolist()

ways_length = [0]*len(explorators_start)

for id,start in enumerate(explorators_start):
    amont = start
    line = df_parcours_explorateurs.loc[df_parcours_explorateurs["noeud_amont"] ==amont ].iloc[0]
    arrivee = False
    while not arrivee:
        ways_length[id]+=line["distance"]
        df_parcours_explorateurs.loc[df_parcours_explorateurs["arete_id"] == line["arete_id"], "explorateur"] = "explorator_" + str(id)
        if line["type_aretes"] == "arrivee":
            arrivee = True
        else:
            amont = line["noeud_aval"]
            line = df_parcours_explorateurs.loc[df_parcours_explorateurs["noeud_amont"] ==amont ].iloc[0]

df_parcours_explorateurs.to_csv("parcours_explorateurs_completed.csv",index=False)
     
print(max(ways_length))


