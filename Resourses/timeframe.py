tf = [
    "Past hour",
    "Past 4 hours",
    "Past 7 days",
    "Past 30 days",
    "Past 90 days",
    "Past 12 months",
    "Past 5 years",
    "2004 - present",
    "Custom time range"
]

print("Select a time frame:")
for index, option in enumerate(tf, start=1):
    print(f"{index}. {option}")

# Loop to get valid input
while True:
    try:
        choice = int(input("Enter your choice (1-9): "))
        if 1 <= choice <= 9:
            selected_option = tf[choice - 1]
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")
    except ValueError:
        print("Invalid input. Please enter a number.")