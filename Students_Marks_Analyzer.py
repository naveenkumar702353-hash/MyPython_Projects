import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Setup Data
students_data = pd.DataFrame({
    "Student_Id": [101,102,103,104,105,106,107,108,109,110],
    "Name": ["Naveen","Kumar","Arun","Vijay","Santhosh","Ajith","Sanmugam","Surya","Dhanush","Kathi"],
    "Physics": [78,67,98,67,50,70,88,69,79,75],
    "Chemistry": [80,75,69,90,65,80,69,80,79,90],
    "Maths": [90,80,70,75,78,60,69,84,79,90]
})

# 2. Add Average directly to the DataFrame
subjects = ["Physics", "Chemistry", "Maths"]
students_data["Average"] = students_data[subjects].mean(axis=1)

# 3. Print Summary Statistics using built-in methods
for sub in subjects:
    print(f"--- {sub} Statistics ---")
    print(f"Total:   {students_data[sub].sum()}")
    print(f"Average: {students_data[sub].mean():.2f}")
    print(f"Highest: {students_data[sub].max()}")
    print(f"Lowest:  {students_data[sub].min()}\n")

# 4. Filter High Achievers
print("Students with Average > 80:")
print(students_data[students_data["Average"] > 80]["Name"].to_string(index=False))

# 5. Plot 1: Student Averages
plt.figure(figsize=(8, 4))
plt.plot(students_data["Name"], students_data["Average"], marker="o", markerfacecolor="grey", color="black", markersize=7)
plt.xlabel("Students Name")
plt.ylabel("Average")
plt.xticks(rotation=45)
plt.tight_layout() # Automatically manages padding so text isn't cut off

# 6. Plot 2: Subject Averages
plt.figure(figsize=(6, 4))
subject_means = students_data[subjects].mean()
plt.bar(subject_means.index, subject_means.values, color=['blue', 'green', 'orange'])
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.tight_layout()

plt.show()
