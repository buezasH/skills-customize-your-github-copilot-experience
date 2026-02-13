# 📘 Assignment: APIs and HTTP Requests in Python

## 🎯 Objective

Learn how to interact with web APIs using Python's `requests` library. You will practice sending HTTP requests, handling JSON responses, and building a small program that fetches and displays real-world data from a public API.

## 📝 Tasks

### 🛠️	Fetch Data from a Public API

#### Description
Write a Python script that sends a GET request to a public API and prints the response. Use the free [JSONPlaceholder](https://jsonplaceholder.typicode.com/) API to retrieve a list of posts.

#### Requirements
Completed program should:

- Import and use the `requests` library to send a GET request to `https://jsonplaceholder.typicode.com/posts`
- Check the response status code and print an error message if the request fails
- Parse the JSON response and print the title of each post
- Limit the output to the first 10 posts

Example output:
```
Post 1: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
Post 2: qui est esse
Post 3: ea molestias quasi exercitationem repellat qui ipsa sit aut
...
```

### 🛠️	Build a User Lookup Tool

#### Description
Create an interactive program that asks the user for a user ID and fetches that user's information from the API. Display the user's name, email, and city in a formatted output.

#### Requirements
Completed program should:

- Prompt the user to enter a user ID (1–10)
- Send a GET request to `https://jsonplaceholder.typicode.com/users/{id}` using the provided ID
- Handle invalid input and display a helpful error message
- Display the user's name, email, and city in a clearly formatted output
- Allow the user to look up multiple users until they choose to quit

Example output:
```
Enter a user ID (1-10) or 'q' to quit: 3
Name: Clementine Bauch
Email: Nathan@yesenia.net
City: McKenziehaven

Enter a user ID (1-10) or 'q' to quit: q
Goodbye!
```
