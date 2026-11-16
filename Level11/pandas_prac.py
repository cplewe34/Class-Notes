import pandas as pd

#if it inside a sub folder you have to call the file
#national_park_data = pd.read_csv("Level11/national_parks_sample.csv")

#print(national_park_data)

park_info = pd.read_csv("Level11/national_parks_sample.csv")

#iloc grabs information from a certain row
#loc filters down to 
#, .loc[] is used to select specific rows and columns from a DataFrame using labels (names or indexes).
#he main difference between .loc[] and .iloc[] in Pandas is how they select data.

#loc access specific colums
#iloc access specific row
#at. is specific cell
#.loc[] selects data using labels (names).

#.iloc[] selects data using integer positions (numbers).
#print(park_info.loc[park_info["Waterfalls"] == "Yes"])

#print(park_info.iloc[2])

#at looks at the Think of .at[] as a faster, more direct version of .loc[] when you only need one cell

#this changes the value in the database
#park_info.at[1, "Waterfalls"] = "Yes"

#print(park_info.at[1, "Waterfalls"])

#In Python Pandas, .iterrows() allows you to loop through a DataFrame one row at a time.
#for row, col in park_info.iterrows():
    #print(row, col)
   # print()

#first part make the requirements and second part prints what you want if it meets the requirement

#print(park_info.query("HighestPointFeet >= 10000 or AnnualVisitorsThousands < 601")[["Park", "HighestPointFeet", "AnnualVisitorsThousands"]])


#this makes it not a panda and makes it a one dimensional
blah = park_info.query("HighestPointFeet >= 10000 or AnnualVisitorsThousands < 601")[["Park", "HighestPointFeet", "AnnualVisitorsThousands"]]
print(blah)