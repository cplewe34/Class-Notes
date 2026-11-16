import pandas as pd

#park_info = pd.read_csv("Level11/national_parks_sample.csv")

#parkloc = park_info.loc[park_info["StateOrStates"] == "Utah"]

#parkiloc = park_info.iloc[4]

#print(parkloc) 
#print(parkiloc)

park_info = pd.read_csv("Level11/national_parks_sample.csv")


parkloc = park_info.loc[(park_info["Region"] == "Southeast") & (park_info["CampingAvailable"] == "Yes")]




print(parkloc[["Park", "StateOrStates", "AnnualVisitorsThousands", "TrailMiles"]])

