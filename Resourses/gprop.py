gproperties = [
  "web",
  "youtube",
  "news",
  "images",
  "froogle"
]

# Printing options
print("Options:")
for index, option in enumerate(gproperties, start=1):
    print(f"{index}. {option}")

while True:
    try:
        # User input
        user_input = input("Enter the options: ").strip().lower()

        # Check if user_input is valid
        if user_input.isdigit():
            user_input = int(user_input)
            if 1 <= user_input <= len(gproperties):
                selected_option = gproperties[user_input - 1]
                print(f"You selected: {selected_option}")
                break
            else:
                print("Invalid input. Please enter a number within the range.")
        else:
            print("Invalid input. Please enter a number.")

    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting.")
        break
    except Exception as e:
        print(f"Error: {e}. Please try again.")