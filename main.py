# Higher Lower Game - Day 14 - Angela Yu 100 Days of Code
# A game where players guess which celebrity/account has more followers

# Import required modules
from art import logo, vs  # ASCII art for game logo and "vs" display
from game_data import data  # List of dictionaries containing account information
import random  # For selecting random accounts


def format_data(account):
    """
    Takes the account data and returns the printable format.

    Args:
        account (dict): Dictionary containing account info (name, description, country, follower_count)

    Returns:
        str: Formatted string with account name, description, and country
    """
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """
    Take a user's guess and the follower counts and returns if they got it right.

    Args:
        user_guess (str): User's input ('a' or 'b')
        a_followers (int): Follower count for account A
        b_followers (int): Follower count for account B

    Returns:
        bool: True if user guessed correctly, False otherwise
    """
    if a_followers > b_followers:
        return user_guess == "a"  # A has more followers, so correct answer is 'a'
    else:
        return user_guess == "b"  # B has more followers, so correct answer is 'b'


# Display the game logo at start
print(logo)

# Initialize game variables
score = 0  # Keep track of player's score
game_should_continue = True  # Flag to control the game loop

# Generate a random account from the game data to start as account B
account_b = random.choice(data)

# Main game loop - continues until player gets an answer wrong
while game_should_continue:

    # Rotate accounts: previous B becomes new A, generate new B
    # This creates continuity - the account they just compared becomes the next comparison point
    account_a = account_b
    account_b = random.choice(data)

    # Ensure we don't get the same account twice in a row
    # Keep generating new account B until it's different from account A
    if account_a == account_b:
        account_b = random.choice(data)

    # Display the two accounts to compare
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)  # Display "VS" ASCII art
    print(f"Against B: {format_data(account_b)}.")

    # Get user's guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen for better user experience
    # Print 20 newlines to push previous content up and out of view
    print("\n" * 20)
    print(logo)  # Redisplay logo after clearing screen

    # Get the actual follower counts for comparison
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # Check if the user's guess was correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Provide feedback and update score
    if is_correct:
        # User was right - increment score and continue game
        score += 1
        print(f"You're right! Current score {score}")
    else:
        # User was wrong - end game and show final score
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False  # Exit the game loop