import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.DataFrame({
    "Employees":["Naveen","Kumar","Vijay","Kavin","Praveen"],
    "Jan":np.array([1500,2000,1000,1800,1300]),
    "Feb":np.array([1700,1800,1300,1600,1500]),
    "Mar":np.array([1600,1900,1500,2000,1450]),
    "Apr":np.array([2000,1700,1850,1500,2000]),
    "May":np.array([1800,1500,2000,1700,1800]),
    "Jun":np.array([1900,1600,1900,1300,1700])
    })
print(df)
pd.melt(df,index="Employees",columns="Months",values="Sales")
Employee=df["Employees"]
#for emp in Employee:
   # print(f"Total Sales for each Employee
