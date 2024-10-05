print("Welcome to Tip Calculator!")
totalbill = float(input("What's the Total Bill:\n$ "))
tip = int(input("How much Tip would you like to give\nTip: 10% 12% or 15% \n"))
split = int(input("How many people would you split the bill:\n"))
bill = totalbill * (1 + tip/100)
bill = bill/split
print(f"Total bill divided among {split} people with {tip}% tip: {bill:.2f} each.")

# Welcome to Tip Calculator!
# What's the Total Bill:
# $ 124.56
# How much Tip would you like to give
# Tip: 10% 12% or 15%
# 12
# How many people would you split the bill:
# 7
# Total bill divided among 7 people with 12% tip: 19.93 each.

# === Code Execution Successful ===

