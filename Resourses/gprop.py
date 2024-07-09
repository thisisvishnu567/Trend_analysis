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

#gprop input
user_input = input("Enter the options : ").strip().lower()