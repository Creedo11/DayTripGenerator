""" Day Trip Generator

(5 points): As a developer, I want to make at least three commits with descriptive messages. 
(5 points): As a developer, I want to store my destinations, restaurants, mode of transportations, and entertainments in their own separate lists. 
(5 points): As a user, I want a destination to be randomly selected for my day trip. 
(5 points): As a user, I want a restaurant to be randomly selected for my day trip. 
(5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 
(5 points): As a user, I want a form of entertainment to be randomly selected for my day trip. 
(15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things. 
(10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections. 
(10 points): As a user, I want to display my completed trip in the console. 
(5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!
 """

 # list of trip options 
destinations = ["Cape Verde", "Japan", "Las Vegas", "South Africa"]
restaurants = ["steakhouse", "sushi", "hibachi", "soul food"]
transportation_modes =["commercial airplane", "rental car", "train", "private jet"]
entertainment_options = ["sky diving", "city tour", "local cuisine cooking class", "casino expierence"]

import random

# random generator functions
def random_value(lists):
    selected_value = random.choice(lists)
    return selected_value

random_destination = random_value(destinations)

random_restaurant = random_value(restaurants)

random_transportation_mode = random_value(transportation_modes)

random_entertainment_option = random_value(entertainment_options)


# destination selection
print("Welcome to your day trip generator where we'll help you confirm your next desired getaway! If you aren't sure what you'd like to do for your getaway, you've come to the right place!")
print(f"To start, we have selected {random_destination} for you. Is this okay?")
user_response = input("Enter Yes/No: ")


while user_response == "No":
        destinations.remove(random_destination)
        random_destination = random_value(destinations)
        print(f"No worries. What about {random_destination}?")
        user_response = input("Enter Yes/No: ")

print(f"Great, {random_destination} is waiting on you! Next, we'll choose your mode of transportation.")
print(" ")



# mode of transportation selection  
print(f"We have selected a {random_transportation_mode} for you. Is this okay?")
user_response = input("Enter Yes/No: ")
 

while user_response == "No":
        transportation_modes.remove(random_transportation_mode)
        random_transportation_mode = random_value(transportation_modes)
        print(f"No worries. What about a {random_transportation_mode}?")
        user_response = input("Enter Yes/No: ")


print(f"Awesome, a {random_transportation_mode} is a great way to travel. Next, we'll choose a place for you to dine.")
print(" ")



# restaurant selection
print(f"We have selected a {random_restaurant} restaurant for you. Is this okay?")
user_response = input("Enter Yes/No: ")


while user_response == "No":
        restaurants.remove(random_restaurant)
        random_restaurant = random_value(restaurants)
        print(f"No worries. What about a {random_restaurant} restaurant?")
        user_response = input("Enter Yes/No: ")


print(f"Nice! The locals always suggest a good {random_restaurant} restaurant. Lastly, we'll choose an activity for you to enjoy.")
print(" ")



# entertainment selection
print(f"We have selected a {random_entertainment_option} activity for you. Is this okay?")
user_response = input("Enter Yes/No: ")


while user_response == "No":
        entertainment_options.remove(random_entertainment_option)
        random_entertainment_option = random_value(entertainment_options)
        print(f"No worries. What about a {random_entertainment_option} activity?")
        user_response = input("Enter Yes/No: ")


print(f"A {random_entertainment_option} activity should be fun! Now let's go ahead and confirm your selections.")
print(" ")

print("The trip we have generated for you is:")
print(f"Destination: {random_destination}")
print(f"Tranportation: {random_transportation_mode}")
print(f"Restaurant: {random_restaurant}")
print(f"Entertainment: {random_entertainment_option}")
print(" ")


user_input = input("Would you like to finalize this trip? Enter Yes/No: ")
not_confirmed = True

while not_confirmed == True:
    if user_input == "Yes":
        not_confirmed = True
        print(f"Get ready for your dream getaway! You will be arriving in {random_destination} by {random_transportation_mode}, where you'll engage in a {random_entertainment_option} activity, and end the day dining a popular local {random_restaurant} restaurant!")
        break
    else:
        print("Please exit and restart trip generator")
        break