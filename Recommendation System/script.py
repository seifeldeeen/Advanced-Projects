from md import movies_data, types

# Global list for filtered movie types
listOfItems = []
new_list_of_items = []

def greeting():
    print('Welcome to our simple Movie Recommendation system, where you can look for the best movies of all time. Here we have some types of movies:')
    for i, genre in enumerate(types):
        print(f"{i + 1}. {genre}")

def LookForFirstLetter():
    global listOfItems  # Ensure listOfItems is accessible in other functions
    # Ask for the initial(s) of the type of movie
    first = input('Type the initial(s) of the type of movie you want (1 or 2 letters): ').lower()

    # Prepare a dictionary to group types by their initials
    initials_map = {t[:2].lower(): [] for t in types}  # Using a set comprehension to speed up genre matching
    for t in types:
        initials_map[t[:2].lower()].append(t)

    # Check if there are any matches and handle the user input
    possible_matches = [key for key in initials_map if key.startswith(first)]
    if possible_matches:
        # If there's only one match, skip the second letter input
        if len(possible_matches) == 1:
            listOfItems = initials_map[possible_matches[0]]
        else:
            listOfItems = [item for match in possible_matches for item in initials_map[match]]
    else:
        print("Hmm, sounds like there's no type of movie starting with this. Let's try again!")
        LookForFirstLetter()

    # Show the matching types
    print("\nYou selected movies of the following type(s):")
    for item in listOfItems:
        print(f"- {item.capitalize()}")

def secondLetterCheck():
    return len(listOfItems) > 1  # Return true if there are multiple matches

def lookForSecondLetter():
    global listOfItems  # Ensure listOfItems is accessible in other functions
    global new_list_of_items

    if secondLetterCheck():  # Only ask for the second letter if needed
        # Ask the user for the second letter
        second_letter = input('Type the second initial of the type you want (e.g., "d" for Adventure): ').lower()
        new_list_of_items = [t for t in listOfItems if len(t) > 1 and t[1].lower() == second_letter]

        if new_list_of_items:
            # If we found items with that second letter, show them
            print("\nYou selected movies of the following type(s):")
            for item in new_list_of_items:
                print(f"- {item.capitalize()}")
        else:
            print("No types found with that second letter. Please try again.")
            lookForSecondLetter()

def ShowMovies():
    global new_list_of_items
    global listOfItems

    # Filter movies based on selected genres
    selected_genres = new_list_of_items if new_list_of_items else listOfItems

    if selected_genres:
        for movie in movies_data:
            if movie[0].lower() in [genre.lower() for genre in selected_genres]:
                print('Here are the names of the movies you are looking for:')
                print(f"- Movie's Name: {movie[1]}")
                print(f"- Releasing Date: {movie[3]}")
                print(f"- Movie's rating: {movie[2]}/5")
                print(f"- Releasing Company: {movie[4]}")

def startSystem():
    LookForFirstLetter()
    if secondLetterCheck():
        lookForSecondLetter()
    ShowMovies()
    last_question_probably()

def last_question_probably():
    global listOfItems
    global new_list_of_items
    
    third = input("Do you want to look for a different movie type? y/n: ")
    
    if third.lower() == 'y':
        # Clear selected genre lists before restarting
        listOfItems = []  # Reset the list
        new_list_of_items = []  # Reset the list
        startSystem()  # Call the startSystem to begin the process again
    else:
        print("Thanks for using my recommendations system, until next time!")

greeting()
startSystem()
