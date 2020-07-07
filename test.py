groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]

total = 0
totalprint = "$"
for item in groceries:
    quantity = input(f"What quantity of {item [0]} where purchased?")
    item[1] = item[1] * int(quantity)
    total = total + item[1]

print("====Izzy's Food Emporium====")
for item in groceries:
    print(f"{item[0]:<20} ${item[1]:.2f}")
print("============================")
print(f"{totalprint:>22}{total:>1.2f}")