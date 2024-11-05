# List of products and their quality control results
quality_results = {
    "Widget A": [True, True, False, True, True],  # Pass/Fail results for Widget A
    "Widget B": [False, True, True, True, False], # Pass/Fail results for Widget B
    "Widget C": [True, True, True, True, True]    # Pass/Fail results for Widget C
}

# Function to analyze quality control results
def analyze_quality(results):
    for product, passes in results.items():
        pass_rate = sum(passes) / len(passes) * 100
        print(f"{product}: {pass_rate:.2f}% pass rate")

# Analyze and display quality control results
analyze_quality(quality_results)
