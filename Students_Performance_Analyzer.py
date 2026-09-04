import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Student_ID": [101,102,103,104,105,106,107,108,109,110],
    "Name": ["Naveen","Kumar","Vijay","Kavin","Praveen",
             "Arun","Vignesh","Ajith","Surya","Kamal"],
    "Department": ["Physics","Physics","Chemistry","Physics","Chemistry",
                   "Physics","Chemistry","Physics","Chemistry","Physics"],
    "Physics": [85,72,90,65,78,88,70,95,82,75],
    "Chemistry": [80,75,88,70,85,82,72,90,80,78],
    "Maths": [90,68,92,72,80,85,75,94,86,70]
})
#Calculate the total marks for each student.
subject=["Physics","Chemistry","Maths"]
df["Total"]=df[subject].sum(axis=1)

#Calculate the average marks for each student.
df["Average_Mark"]=df[subject].mean(axis=1)
#Find the student who has the highest total marks.
HM_Student=df.loc[df["Total"].idxmax(),"Name"]
print(f"Student With Highest Total Mark :\n{HM_Student}")

#Find all students whose average is greater than 80.
A_Students=df[df["Average_Mark"]>80]["Name"].to_string(index=False)
print(f"Students Whose Average is Greater than 80:\n{A_Students}")

#Calculate the average marks for each department using groupby().
AD_Mark=df.groupby("Department")["Average_Mark"].mean()
print(f"Average Marks For Each Department:\n{AD_Mark}")

#Find the highest-scoring student in each department.
HD_Students=df.loc[df.groupby("Department")["Total"].idxmax(),["Department","Name","Total"]].to_string(index=False)
print(f"Highest Scoring Student in each Department:\n{HD_Students}")

#Use transform() to calculate the department average for every student.
df["Department_Average"]=df.groupby("Department")["Average_Mark"].transform("mean")
print(df[["Name","Department","Average_Mark","Department_Average"]])
#Create a new Performance column:
conditions = [
    df["Average_Mark"] >= 80,
    df["Average_Mark"] >= 70
]
choices = [
    "Excellent",
    "Good"
]
df["Performance"] = np.select(
    conditions,
    choices,
    default="Needs Improvement"
)
print(df)
#Create a bar graph showing: Department vs Average Marks
plt.figure()
plt.bar(AD_Mark.index,AD_Mark.values)
plt.xlabel("Department")
plt.ylabel("Average Mark")
plt.title("Department vs Average Mark")

#Create a scatter plot showing: Total Marks vs Average Marks
plt.figure(figsize=(6,4))
plt.scatter(df["Total"],df["Average_Mark"],color="green",edgecolor="violet",label="Marks")
plt.legend()
plt.show()

