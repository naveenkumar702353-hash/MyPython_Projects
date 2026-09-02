import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.DataFrame({
    "Employee_ID":[101,102,103,104,105,106,107,108,109,110],
    "Employee_Name":["Naveen","Kumar","Vijay","Arun","Vignesh","Vikram","Ajith","Surya","Arya","Kamal"],
    "Department":["IT","HR","Finance","IT","Marketing","Finance","IT","HR","Marketing","Finance"],
    "Salary":np.array([50000,30000,30000,80000,40000,45000,70000,65000,60000,90000]),
    "Year_of_experience":[2,2,3,3,4,4,3,5,5,4]
    })
Average_salary=df["Salary"].mean()
Highest_Salary=df["Salary"].max()
Lowest_Salary=df["Salary"].min()
increment_percentage=10
df["New_Salary"]=df["Salary"]*(1+increment_percentage/100)
depart_avg=df.groupby("Department")["Salary"].mean()
print(f"Average Salary :{Average_salary}")
print(f"Highest Salary :{Highest_Salary}")
print(f"Lowest Salary :{Lowest_Salary}")
print(f"Employees with Salaries Greater than Fifty Thousand :\n{df[df['Salary']>50000]['Employee_Name'].to_string(index=False)}")
print(f"Employees Salary after 10% increment :{df['New_Salary'].to_string(index=False)}")
print(f"Average Department Salary\n{depart_avg}")
plt.figure(figsize=(8,4))
plt.bar(depart_avg.index,depart_avg.values)
plt.title("Department vs Average Salary")
plt.xlabel("Department")
plt.ylabel("Average salary")

plt.figure(figsize=(6,4))
plt.scatter(df["Year_of_experience"],df["Salary"],color="red",alpha=0.5,edgecolor="black",label="Salary")
plt.xlabel("Year_of_experience")
plt.ylabel("Salary")
plt.legend()
plt.show()
