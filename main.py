# # Day Trip Generator

# # (5 points): As a developer, I want to make at least three commits with descriptive messages. 
# # (5 points): As a developer, I want to store my destinations, restaurants, mode of transportations, and entertainments in their own separate lists. 
# # (5 points): As a user, I want a destination to be randomly selected for my day trip. 
# # (5 points): As a user, I want a restaurant to be randomly selected for my day trip. 
# # (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 
# # (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip. 
# # (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things. 
# # (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections. 
# # (10 points): As a user, I want to display my completed trip in the console. 
# # (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!


# # list of trip options
# destinations = ["Cape Verde", "Japan", "Las Vegas", "South Africa"]
# restaurants = ["steakhouse", "sushi", "hibachi", "soul food"]
# transportation_modes =["commercial airplane", "rental car", "train", "private jet"]
# entertainment_options = ["sky diving", "city tour", "local cuisine cooking class", "casino expierence"]



# import random

# # # random destination generator
# def random_value(lists):
#     destination = (random.choice(destinations))
#     return destination

# random_destination = random_value(destinations)



# # # random restaurant generator
# def random_value(lists):
#     restaurant = (random.choice(restaurants)) 
#     return restaurant

# random_restaurant = random_value(restaurants)




# # # random mode of transportation generator 
# def random_value(lists):
#     transportation_mode = (random.choice(transportation_modes))
#     return transportation_mode

# random_transportation_mode = random_value(transportation_modes)




# # # random entertainment option generator
# def random_value(lists):
#     entertainment_option = (random.choice(entertainment_options))
#     return entertainment_option

# random_entertainment_option = random_value(entertainment_options)




# # destination selection
# print("Welcome to your day trip generator where we'll help you confirm your next desired getaway! If you aren't sure what you'd like to do for your getaway, you've come to the right place!")
# print(f"To start, we have selected {random_destination} for you. Is this okay?")
# user_response = input("Enter Yes/No: ")

# random_des_one = "Cape Verde"
# random_des_two = "Japan"
# random_des_three = "Las Vegas"
# random_des_four = "South Africa"
# random_destination_selected = (random_destination)


# while user_response == "No":
#     if user_response == "Yes":
#         break
#     if random_destination_selected == random_des_one:
#         destinations.remove(random_destination_selected)
#         random_destination_selected = random.choice(destinations)
#         print(f"No worries. What about {random_destination_selected}?")
#         user_response = input("Enter Yes/No: ")
#     elif random_destination_selected == random_des_two:
#         destinations.remove(random_destination_selected)
#         random_destination_selected = random.choice(destinations)
#         print(f"No worries. What about {random_destination_selected}?")
#         user_response = input("Enter Yes/No: ")
#     elif random_destination_selected == random_des_three:
#         destinations.remove(random_destination_selected)
#         random_destination_selected = random.choice(destinations)
#         print(f"No worries. What about {random_destination_selected}?")
#         user_response = input("Enter Yes/No: ")
#     elif random_destination_selected == random_des_four:
#         destinations.remove(random_destination_selected)
#         random_destination_selected = random.choice(destinations)
#         print(f"No worries. What about {random_destination_selected}?")
#         user_response = input("Enter Yes/No: ")

# print(f"Great, {random_destination_selected} is waiting on you! Next, we'll choose your mode of transportation.")
# print(" ")




# # mode of transportation selection  
# print(f"We have selected a {random_transportation_mode} for you. Is this okay?")
# user_response = input("Enter Yes/No: ")

# random_trans_one = "commercial airplane"
# random_trans_two = "rental car"
# random_trans_three = "train"
# random_trans_four = "private jet"
# random_trans_selected = (random_transportation_mode)
 

# while user_response == "No":
#     if user_response == "Yes":
#         break
#     if random_trans_selected == random_trans_one:
#         transportation_modes.remove(random_trans_selected)
#         random_trans_selected = random.choice(transportation_modes)
#         print(f"No worries. What about a {random_trans_selected}?")
#         user_response = input("Enter Yes/No: ")
#     elif random_trans_selected == random_trans_two:
#         transportation_modes.remove(random_trans_selected)
#         random_trans_selected = random.choice(transportation_modes)
#         print(f"No worries. What about a {random_trans_selected}?")
#         user_response = input("Enter Yes/No: ")
#     elif random_trans_selected == random_trans_three:
#         transportation_modes.remove(random_trans_selected)
#         random_trans_selected = random.choice(transportation_modes)
#         print(f"No worries. What about a {random_trans_selected}?")
#         user_response = input("Enter Yes/No: ")
#     elif random_trans_selected == random_trans_four:
#         transportation_modes.remove(random_trans_selected)
#         random_trans_selected = random.choice(transportation_modes)
#         print(f"No worries. What about a {random_trans_selected}?")
#         user_response = input("Enter Yes/No: ")

# print(f"Awesome, a {random_trans_selected} is a great way to travel. Next, we'll choose a place for you to dine.")
# print(" ")




# # restaurant selection
# print(f"We have selected a {random_restaurant} restaurant for you. Is this okay?")
# user_response = input("Enter Yes/No: ")

# random_res_one = "steakhouse"
# random_res_two = "sushi"
# random_res_three = "hibachi"
# random_res_four = "soul food"
# random_res_selected = (random_restaurant)


# while user_response == "No":
#     if user_response == "Yes":
#         break
#     if random_res_selected == random_res_one:
#         restaurants.remove(random_res_selected)
#         random_res_selected = random.choice(restaurants)
#         print(f"No worries. What about a {random_res_selected} restaurant?")
#         user_response = input("Enter Yes/No: ")
#     elif random_res_selected == random_res_two:
#         restaurants.remove(random_res_selected)
#         random_res_selected = random.choice(restaurants)
#         print(f"No worries. What about a {random_res_selected} restaurant?")
#         user_response = input("Enter Yes/No: ")
#     elif random_res_selected == random_res_three:
#         restaurants.remove(random_res_selected)
#         random_res_selected = random.choice(restaurants)
#         print(f"No worries. What about a {random_res_selected} restaurant?")
#         user_response = input("Enter Yes/No: ")
#     elif random_res_selected == random_res_four:
#         restaurants.remove(random_res_selected)
#         random_res_selected = random.choice(restaurants)
#         print(f"No worries. What about a {random_res_selected} restaurant?")
#         user_response = input("Enter Yes/No: ")

# print(f"Nice! The locals always suggest a good {random_res_selected} restaurant. Lastly, we'll choose an activity for you to enjoy.")
# print(" ")




# # entertainment selection
# print(f"We have selected a {random_entertainment_option} activity for you. Is this okay?")
# user_response = input("Enter Yes/No: ")

# random_ent_one = "sky diving"
# random_ent_two = "city tour"
# random_ent_three = "local cuisine cooking class"
# random_ent_four = "casino expierence"
# random_ent_selected = (random_entertainment_option)


# while user_response == "No":
#     if user_response == "Yes":
#         break
#     if random_ent_selected == random_ent_one:
#         entertainment_options.remove(random_ent_selected)
#         random_ent_selected = random.choice(entertainment_options)
#         print(f"No worries. What about a {random_ent_selected} activity?")
#         user_response = input("Enter Yes/No: ")
#     elif random_ent_selected == random_ent_two:
#         entertainment_options.remove(random_ent_selected)
#         random_ent_selected = random.choice(entertainment_options)
#         print(f"No worries. What about a {random_ent_selected} activity?")
#         user_response = input("Enter Yes/No: ")
#     elif random_ent_selected == random_ent_three:
#         entertainment_options.remove(random_ent_selected)
#         random_ent_selected = random.choice(entertainment_options)
#         print(f"No worries. What about a {random_ent_selected} activity?")
#         user_response = input("Enter Yes/No: ")
#     elif random_ent_selected == random_ent_four:
#         entertainment_options.remove(random_ent_selected)
#         random_ent_selected = random.choice(entertainment_options)
#         print(f"No worries. What about a {random_ent_selected} activity?")
#         user_response = input("Enter Yes/No: ")

# print(f"A {random_ent_selected} activity should be fun! Now let's go ahead and confirm your selections.")
# print(" ")

# print("The trip we have generated for you is:")
# print(f"Destination: {random_destination_selected}")
# print(f"Tranportation: {random_trans_selected}")
# print(f"Restaurant: {random_res_selected}")
# print(f"Entertainment: {random_ent_selected}")
# print(" ")


# user_input = input("Would you like to finalize this trip? Enter Yes/No: ")
# not_confirmed = True

# while not_confirmed == True:
#     if user_input == "Yes":
#         not_confirmed = True
#         print(f"Get ready for your dream getaway! You will be arriving in {random_destination_selected} by {random_trans_selected}, where you'll engage in a {random_ent_selected} activity, and end the day dining a popular local {random_res_selected} restaurant!")
#         break
#     else:
#         print("Please exit and restart trip generator")
#         break