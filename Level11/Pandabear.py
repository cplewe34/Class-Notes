import pandas as pd

#park_info = pd.read_csv("Level11/national_parks_sample.csv")

#parkloc = park_info.loc[park_info["StateOrStates"] == "Utah"]

#parkiloc = park_info.iloc[4]

#print(parkloc) 
#print(parkiloc)

park_info = pd.read_csv("Level11/national_parks_sample.csv")


#parkloc = park_info.loc[(park_info["Region"] == "Southeast") & (park_info["CampingAvailable"] == "Yes")]

#print(parkloc[["Park", "StateOrStates", "AnnualVisitorsThousands", "TrailMiles"]])

#result = park_info.query('Park == "Everglades"')[["Park", "Region", "TrailMiles"]]
park_info.at[9, "ReviewStatus"] = "Needs Review"

park_info["ReviewStatus"] = "Not Reviewed"

park_info.at[10, "PlanningPriority"] = "Standard"

park_info["PlanningPriority"] = "Low"

park_info.loc[park_info["TrailMiles"] >= 500, "PlanningPriority"] = "High"

print(park_info[["Park", "ReviewStatus", "PlanningPriority"]])

