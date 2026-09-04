import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Date": [
        "2026-01-03", "2026-01-05", "2026-01-08", "2026-01-12",
        "2026-01-15", "2026-01-18", "2026-01-22", "2026-01-25",
        "2026-02-02", "2026-02-05", "2026-02-09", "2026-02-13",
        "2026-02-17", "2026-02-21", "2026-02-25", "2026-02-28",
        "2026-03-03", "2026-03-06", "2026-03-10", "2026-03-14",
        "2026-03-18", "2026-03-22", "2026-03-26", "2026-03-30"
    ],

    "Category": [
        "Food", "Transport", "Shopping", "Bills",
        "Food", "Entertainment", "Transport", "Food",
        "Bills", "Shopping", "Food", "Transport",
        "Entertainment", "Food", "Bills", "Shopping",
        "Transport", "Food", "Entertainment", "Bills",
        "Shopping", "Food", "Transport", "Food"
    ],

    "Description": [
        "Lunch", "Bus", "Clothes", "Electricity",
        "Dinner", "Movie", "Auto", "Groceries",
        "Internet", "Shoes", "Restaurant", "Metro",
        "Concert", "Groceries", "Mobile Bill", "Books",
        "Cab", "Lunch", "Movie", "Electricity",
        "Clothes", "Restaurant", "Bus", "Groceries"
    ],

    "Amount": np.array([
        250, 80, 1200, 1800,
        450, 500, 150, 900,
        1000, 1800, 350, 100,
        1200, 700, 900, 600,
        300, 280, 450, 1600,
        1500, 500, 120, 850
    ]),

    "Payment_Mode": [
        "UPI", "Cash", "Card", "UPI",
        "UPI", "Card", "Cash", "UPI",
        "UPI", "Card", "Cash", "UPI",
        "Card", "UPI", "UPI", "Cash",
        "UPI", "Cash", "Card", "UPI",
        "Card", "UPI", "Cash", "UPI"
    ]
})
print(df)
Total_expense=df["Amount"].sum()
Average_expense=df["Amount"].mean()
Highest_expense=df["Amount"].max()
Lowest_expense=df["Amount"].min()
