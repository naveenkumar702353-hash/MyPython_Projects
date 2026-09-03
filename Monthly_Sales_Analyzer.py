import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.DataFrame({
    "Employees":["Naveen","Kumar","Vijay","Kavin","Praveen"],
    "Jan":np.array([1500,2000,1000,1800,1300]),
    "Feb":np.array([1700,1800,1300,1600,1500]),
    "Mar":np.array([1600,1900,1500,2000,1450]),
    "Apr":np.array([2000,1600,1850,1500,2000]),
    "May":np.array([1800,1500,2000,1700,1800]),
    "Jun":np.array([1900,1600,1900,1300,1700])
    })

df["Total_Sales"]=df[["Jan","Feb","Mar","Apr","May","Jun"]].sum(axis=1)
print(f"Employee with Highest Salary:{df.loc[df['Total_Sales'].idxmax(), 'Employees']}")
months=["Jan","Feb","Mar","Apr","May","Jun"]
for i in months:
    print(f"------{i} Monthly Sales------")
    print(f"Total Sales:{df[i].sum()}")

H_months=df[months].sum()
print(f"Best Performing Month:{H_months.idxmax()}")

df_long=pd.melt(
    df,
    id_vars="Employees",
    value_vars=months,
    var_name="Months",
    value_name="Sales"
    )
print(df_long)
plt.figure(figsize=(8,4))
plt.plot(df["Employees"],df["Total_Sales"],color="red",marker=".",markersize=15,markerfacecolor="black")
plt.xlabel("Employees")
plt.ylabel("Total Sales")

plt.figure()
for employee in df["Employees"]:
    employee_data = df[df["Employees"] == employee]

    plt.plot(
        months,
        employee_data[months].values[0],
        marker="o",
        label=employee
    )

plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()

