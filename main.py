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
transportation_modes =["Ariplane Flight", "Rental Car", "Train", "Private Jet"]
list_of_entertainment_options = ["Sky Diving", "City Tour", "Local Cuisine Cooking Class", "Casino Expierence"]

import random

# # random destination generator
def random_value(lists):
    destination = (random.choice(destinations))
    return destination

random_destination = random_value(destinations)

# # random restaurant generator
def random_value(lists):
    restaurant = (random.choice(restaurants)) 
    return restaurant

random_restaurant = random_value(restaurants)

# # random mode of transportation generator 
def random_value(lists):
    transportation_mode = (random.choice(transportation_modes))
    return transportation_mode

random_transportation_mode = random_value(transportation_modes)

# # random entertainment option generator
# def random_value(lists):
#     entertainment_option = (random.choice(list_of_entertainment_options))
#     return entertainment_option

# random_entertainment_option = random_value(list_of_entertainment_options)


# destination selection
print("Welcome to your day trip generator where we'll help you confirm your next desired getaway! If you aren't sure what you'd like to do for your getaway, you've come to the right place!")
print(f"To start, we have selected {random_destination} for you. Is this okay?")
user_response = input("Enter Yes/No: ")

random_des_one = "Cape Verde"
random_des_two = "Japan"
random_des_three = "Las Vegas"
random_des_four = "South Africa"
random_destination_selected = (random_destination)

while user_response == "No":
    if user_response == "Yes":
        break
    if random_destination_selected == random_des_one:
        destinations.remove(random_destination_selected)
        random_destination_selected = random.choice(destinations)
        print(f"Ahhh okay. What about {random_destination_selected}?")
        user_response = input("Enter Yes/No: ")
    elif random_destination_selected == random_des_two:
        destinations.remove(random_destination_selected)
        random_destination_selected = random.choice(destinations)
        print(f"Ahhh okay. What about {random_destination_selected}?")
        user_response = input("Enter Yes/No: ")
    elif random_destination_selected == random_des_three:
        destinations.remove(random_destination_selected)
        random_destination_selected = random.choice(destinations)
        print(f"Ahhh okay. What about {random_destination_selected}?")
        user_response = input("Enter Yes/No: ")
    elif random_destination_selected == random_des_four:
        destinations.remove(random_destination_selected)
        random_destination_selected = random.choice(destinations)
        print(f"Ahhh okay. What about {random_destination_selected}?")
        user_response = input("Enter Yes/No: ")

print(f"Great, {random_destination} is waiting on you! Next, we'll chose your mode of transportation.")

# mode of transportation selection  
print(f"We have selected a {random_transportation_mode} for you. Is this okay?")
user_response = input("Enter Yes/No: ")

random_trans_one = "Ariplane Flight"
random_trans_two = "Rental Car"
random_trans_three = "Train"
random_trans_four = "Private Jet"
random_trans_selected = (random_transportation_mode)
 

while user_response == "No":
    if user_response == "Yes":
        break
    if random_trans_selected == random_trans_one:
        transportation_modes.remove(random_trans_selected)
        random_trans_selected = random.choice(transportation_modes)
        print(f"Ahhh okay. What about {random_trans_selected}?")
        user_response = input("Enter Yes/No: ")
    elif random_trans_selected == random_trans_two:
        transportation_modes.remove(random_trans_selected)
        random_trans_selected = random.choice(transportation_modes)
        print(f"Ahhh okay. What about {random_trans_selected}?")
        user_response = input("Enter Yes/No: ")
    elif random_trans_selected == random_trans_three:
        transportation_modes.remove(random_trans_selected)
        random_trans_selected = random.choice(transportation_modes)
        print(f"Ahhh okay. What about {random_trans_selected}?")
        user_response = input("Enter Yes/No: ")
    elif random_trans_selected == random_trans_four:
        transportation_modes.remove(random_trans_selected)
        random_trans_selected = random.choice(transportation_modes)
        print(f"Ahhh okay. What about {random_trans_selected}?")
        user_response = input("Enter Yes/No: ")


print(f"Awesome, a {random_destination} is a great way to travel. Next, we'll chose a place for you to dine.")

# restaurant selection
print(f"We have selected a {random_transportation_mode} for you. Is this okay?")