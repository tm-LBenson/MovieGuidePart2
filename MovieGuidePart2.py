# Lewis Benson
# CIS261
# MovieGuidePart2

MOVIE_FILE = 'movies.txt'

def load_movies_from_file():
    """Load movie titles from a file into a list."""
    try:
        with open(MOVIE_FILE, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return None

def display_menu():
    """Display a menu of choices to the user."""
    print()
    print("The Movie List program")
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")
    print()

def get_user_choice():
    """Get the user's menu choice."""
    return input("Command: ").lower()

def display_movies(movies_list):
    """Display all movies from the list."""
    print()
    print("The Movie List")
    for i, movie in enumerate(movies_list, start=1):
        print(f"{i}. {movie}")

def add_movie(movies_list):
    """Add a movie to the list."""
    movie_title = input("Movie: ")
    movies_list.append(movie_title)
    print()
    print(f"{movie_title} was added.")

def delete_movie(movies_list):
    """Delete a movie from the list."""
    index = int(input("Number: ")) - 1
    if 0 <= index < len(movies_list):
        movie = movies_list.pop(index)
        print()
        print(f"{movie} was deleted.")
    else:
        print()
        print("Invalid movie number.")

def save_movies_to_file(movies_list):
    """Save the list of movies back to the file."""
    with open(MOVIE_FILE, 'w') as file:
        for movie in movies_list:
            file.write(f"{movie}\n")

def display_invalid_command_message():
    """Display an invalid command message."""
    print()
    print("Not a valid command. Please try again.")

def main():
    """Run the movie list program."""
    movies_list = load_movies_from_file()
    if movies_list is None:
        print()
        print("Exiting program due to missing file.")
        return
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == "exit":
            print()
            print("Bye!")
            print()
            break
        elif choice == "list":
            display_movies(movies_list)
        elif choice == "add":
            add_movie(movies_list)
            save_movies_to_file(movies_list)
        elif choice == "del":
            delete_movie(movies_list)
            save_movies_to_file(movies_list)
        else:
            display_invalid_command_message()

if __name__ == "__main__":
    main()
