import requests


def fetch_posts():
    """Fetch and display the first 10 posts from the API."""
    # TODO: Send a GET request to https://jsonplaceholder.typicode.com/posts
    # TODO: Check the response status code
    # TODO: Parse the JSON response
    # TODO: Print the title of the first 10 posts
    pass


def lookup_user():
    """Look up a user by ID and display their information."""
    # TODO: Prompt the user for a user ID (1-10) or 'q' to quit
    # TODO: Send a GET request to https://jsonplaceholder.typicode.com/users/{id}
    # TODO: Handle invalid input with a helpful error message
    # TODO: Display the user's name, email, and city
    # TODO: Allow repeated lookups until the user quits
    pass


if __name__ == "__main__":
    print("=== Task 1: Fetch Posts ===")
    fetch_posts()

    print("\n=== Task 2: User Lookup Tool ===")
    lookup_user()
