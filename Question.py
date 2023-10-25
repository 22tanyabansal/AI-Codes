# Define the set of questions and their corresponding answers
questions = {
    1: "John likes apples.",
    2: "Yes, someone likes apples.",
    3: "No, it's not true that nobody likes apples.",
    4: "John likes apples, plays cricket, and enjoys playing the piano.",
    5: "Yes, someone plays at least one instrument.",
    6: "John likes to play chess, drink buttermilk, but does not play any instrument.",
    7: "John shares at least one hobby and at least one instrument with someone.",
    8: "People share common instruments but no hobbies in common: [John, Alice]."
}

# Function to display the menu and get user input
def display_menu():
    print("Menu:")
    for key, value in questions.items():
        print(f"{key}. {value}")
    print("Enter the question number (1-8) or 0 to exit:")

# Main program
while True:
    display_menu()
    choice = int(input("Your choice: "))

    if choice == 0:
        print("Exiting the program.")
        break
    elif choice in questions:
        print(f"Answer to Question {choice}: {questions[choice]}\n")
    else:
        print("Invalid question number. Please select a valid option.\n")
