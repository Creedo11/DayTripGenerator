# Day Trip Generator

# (5 points): As a developer, I want to make at least three commits with descriptive messages. 
# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportations, and entertainments in their own separate lists. 
# (5 points): As a user, I want a destination to be randomly selected for my day trip. 
# (5 points): As a user, I want a restaurant to be randomly selected for my day trip. 
# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 
# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip. 
# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things. 
# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections. 
# (10 points): As a user, I want to display my completed trip in the console. 
# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!



# list of trip options
destinations = ["Cape Verde", "Japan", "Las Vegas", "South Africa"]
restaurants = ["ABS Steakhouse", "ABC Sushi", "ABC Hibachi", "ABC Soul Food Joint"]
transportation_modes =["Ariplane Flight", "Rental Car", "Train", "Boat"]
list_of_entertainment_options = ["Sky Diving", "City Tour", "Local Cuisine Cooking Class", "Casino Expierence"]


import random

# random destination generator
def random_value(lists):
    destination = (random.choice(destinations))
    return destination

random_destination = random_value(destinations)

# random restaurant generator
def random_value(lists):
    restaurant = (random.choice(restaurants))
    return restaurant

random_restaurant = random_value(restaurants)

# random mode of transportation generator 
def random_value(lists):
    transportation_mode = (random.choice(transportation_modes))
    return transportation_mode

random_transportation_mode = random_value(transportation_modes)

# random entertainment option generator
def random_value(lists):
    entertainment_option = (random.choice(list_of_entertainment_options))
    return entertainment_option

random_entertainment_option = random_value(list_of_entertainment_options)

print("Welcome to your day trip generator where we'll help confirm your next desired getaway! If you aren't sure what you'd like to do for your getaway, you've come to the right place!")
print(f"We have selected {random_destination} for you. Is this good?")


def user_selected_destination(list_of_denstenations):
    for destination in list_of_denstenations
        if destination == "Cape Verd":
            




    # elif random_destination == "Japan":
    #     user_selection == "Yes"
    #     destinations.remove("Japan")
    #     print(f"We have selected {random_destination} for you. Is this good? {user_selection}")
    #     valid_response = True
    # elif random_destination == "South Africa":
    #     user_selection == "Yes"
    #     destinations.remove("South Africa")
    #     print(f"We have selected {random_destination} for you. Is this good? {user_selection}")
    #     valid_response = True
    # elif random_destination == "Las Vegas":
    #     user_selection == "Yes"
    #     destinations.remove("Las Vegas")
    #     print(f"We have selected {random_destination} for you. Is this good? {user_selection}")
    #     valid_response = True







































