# Daily production data for a week (rows: days, columns: products)
production_data = [
    [50, 30, 20],  # Day 1
    [40, 25, 30],  # Day 2
    [60, 35, 25],  # Day 3
    [70, 20, 15],  # Day 4
    [55, 45, 35],  # Day 5
    [65, 30, 20],  # Day 6
    [80, 40, 30]   # Day 7
]

# Function to calculate total production for the week
def total_production(production_data):
    total = [0] * len(production_data[0])  # Initialize total for each product
    for day in production_data:
        for i in range(len(day)):
            total[i] += day[i]
    return total

# Calculate and display total production
total = total_production(production_data)
print("Total Production for the Week:")
for i in range(len(total)):
    print(f"Product {i + 1}: {total[i]} units")
