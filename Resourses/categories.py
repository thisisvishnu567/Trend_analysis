categories = {
    "Arts & Entertainment": [
        "Books & Literature",
        "Celebrity Fan and Gossip",
        "Comics & Animation",
        "Events & Listings",
        "Humor",
        "Movies",
        "Music & Audio",
        "Performing Arts",
        "TV & Video",
        "Visual Art & Design"
    ],
    "Autos & Vehicles": [
        "Automotive Industry",
        "Automotive Parts & Services",
        "Bikes & Scooters",
        "Boating",
        "Campers & RVs",
        "Classic Vehicles",
        "Motor Vehicles (By Type)"
    ],
    "Beauty & Fitness": [
        "Beauty Pageants",
        "Body Art",
        "Cosmetic Procedures",
        "Face & Body Care",
        "Fitness",
        "Hair Care",
        "Makeup & Cosmetics",
        "Weight Loss"
    ],
    "Books & Literature": [
        "Children\’s Literature",
        "Comics",
        "E-books",
        "Fan Fiction",
        "Literary Classics",
        "Magazines",
        "Poetry",
        "Romance Novels"
    ],
    "Business & Industrial": [
        "Advertising & Marketing",
        "Aerospace & Defense",
        "Agriculture & Forestry",
        "Business Operations",
        "Business Services",
        "Chemicals",
        "Construction & Maintenance",
        "Energy & Utilities",
        "Industrial Materials & Equipment",
        "Manufacturing",
        "Metals & Mining",
        "Pharmaceuticals & Biotech"
    ],
    "Computers & Electronics": [
        "Computer Hardware",
        "Consumer Electronics",
        "Networking",
        "Programming",
        "Software",
        "Tech News"
    ],
    "Finance": [
        "Accounting & Auditing",
        "Banking",
        "Credit & Lending",
        "Insurance",
        "Investing",
        "Money Management",
        "Taxation"
    ],
    "Food & Drink": [
        "Beverages",
        "Cooking & Recipes",
        "Food & Grocery Retailers",
        "Food Services"
    ],
    "Games": [
        "Board Games",
        "Card Games",
        "Computer & Video Games",
        "Gambling",
        "Roleplaying Games",
        "Video Game Consoles"
    ],
    "Health": [
        "Alternative & Natural Medicine",
        "Dentistry",
        "Health Conditions",
        "Health Education & Medical Training",
        "Medical Devices & Equipment",
        "Mental Health",
        "Nutrition",
        "Pharmacy",
        "Public Health"
    ],
    "Hobbies & Leisure": [
        "Birdwatching",
        "Crafts",
        "Fishing",
        "Gardening",
        "Outdoors",
        "Photography",
        "Radio Control & Modeling",
        "Stargazing",
        "Video & Computer Games"
    ],
    "Home & Garden": [
        "Bed & Bath",
        "Building Materials & Supplies",
        "Home Appliances",
        "Home Decor",
        "Home Improvement",
        "Home Storage & Shelving",
        "Housekeeping",
        "Landscaping"
    ],
    "Internet & Telecom": [
        "Email & Messaging",
        "Internet Software & Apps",
        "Mobile & Wireless",
        "Search Engines",
        "Web Design & Development"
    ],
    "Jobs & Education": [
        "Career Resources & Planning",
        "College & University",
        "Education Resources",
        "K-12 Education",
        "Special Education",
        "Training & Certification",
        "Vocational & Continuing Education"
    ],
    "Law & Government": [
        "Government",
        "Immigration & Border Issues",
        "Legal"
    ],
    "News": [
        "Business News",
        "Entertainment News",
        "Health News",
        "Science News",
        "Sports News",
        "Technology News",
        "Weather News"
    ],
    "Online Communities": [
        "Blogs & Forums",
        "Dating & Personals",
        "Social Networks"
    ],
    "People & Society": [
        "Dating & Relationships",
        "Family & Relationships",
        "Men\’s Interests",
        "Religion & Belief",
        "Seniors & Retirement",
        "Social Issues & Advocacy",
        "Teens",
        "Women\’s Interests"
    ],
    "Pets & Animals": [
        "Animal Products & Services",
        "Pet Food & Supplies",
        "Pets",
        "Veterinary Medicine"
    ],
    "Real Estate": [
        "Property Development",
        "Property Management",
        "Real Estate Agencies",
        "Rental Listings",
        "Residential Properties"
    ],

     "Reference": [
        "Dictionaries & Encyclopedias",
        "General Reference",
        "Libraries & Museums"
    ],
    "Science": [
        "Astronomy",
        "Biology",
        "Chemistry",
        "Earth Sciences",
        "Engineering & Technology",
        "Mathematics",
        "Physics",
        "Scientific Institutions"
    ],
    "Shopping": [
        "Apparel",
        "Consumer Electronics",
        "Coupons & Discount Offers",
        "Gifts & Special Event Items",
        "Luxury Goods",
        "Office Supplies",
        "Online Shopping",
        "Sporting Goods"
    ],
    "Sports": [
        "Baseball",
        "Basketball",
        "Combat Sports",
        "Cycling",
        "Extreme Sports",
        "Football",
        "Golf",
        "Horse Racing",
        "Motor Sports",
        "Soccer",
        "Tennis",
        "Water Sports",
        "Winter Sports"
    ],
    "Travel": [
        "Accommodation",
        "Air Travel",
        "Car Rental & Taxi Services",
        "Cruises & Charters",
        "Tourist Destinations",
        "Travel Agencies & Services",
        "Travel Guides & Travelogues"
    ]
}

print("Categories : ")
for i, c in enumerate(categories, start=1):
    print(f"{i}. {c}")

while True:
    try:
        main_category_input = input("Enter the main category option : ").strip().lower()

        if main_category_input.isdigit():
            main_category_input = int(main_category_input)
            if 1 <= main_category_input <= len(categories):
                selected_category = list(categories.keys())[main_category_input - 1]
                print(f"You selected category: {selected_category}")
                print("Subcategories:")
                for idx, subcat in enumerate(categories[selected_category], start=1):
                    print(f"{idx}. {subcat}")
                
                while True:
                    try:
                        subcategory_input = input("Enter the subcategory option : ").strip().lower()

                        if subcategory_input.isdigit():
                            subcategory_input = int(subcategory_input)
                            if 1 <= subcategory_input <= len(categories[selected_category]):
                                selected_subcategory = categories[selected_category][subcategory_input - 1]
                                # print(f"You selected subcategory: {selected_subcategory}")
                                break
                            else:
                                print("Invalid input. Please enter a number within the range.")
                        else:
                            print("Invalid input. Please enter a number.")

                    except KeyboardInterrupt:
                        print("\nProcess interrupted. Exiting.")
                        exit()
                    except Exception as e:
                        print(f"Error: {e}. Please try again for subcategory.")
                break
            else:
                print("Invalid input. Please enter a number within the range.")
        else:
            print("Invalid input. Please enter a number.")

    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting.")
        exit()
    except Exception as e:
        print(f"Error: {e}. Please try again for category.")