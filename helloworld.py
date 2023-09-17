import http.client
import chardet
import requests  # Import the requests library for HTTP requests

def test_url (url):
  # Define the target URL
  try:
      # Create an HTTP connection to the target server
      connection = http.client.HTTPSConnection(url)

      # Send an HTTP GET request
      connection.request("GET", "/")

      # Get the response
      response = connection.getresponse()

      # Print the response status code
      print("Response Status Code:", response.status)

      # Read the response content as binary data
      content = response.read()

      # Print the length of the content
      print("Content Length:", len(content))
      
      # Close the connection
      connection.close()
  except Exception as e:
      print(f"An error occurred: {e}")

def fetch_github_user(username):
    # Define the URL for the GitHub API
    url = f"https://api.github.com/users/{username}"

    try:
        # Send an HTTP GET request to the GitHub API
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            user_data = response.json()

            # Extract and return the user's name
            user_name = user_data.get("name")
            return user_name

        else:
            # If the request was not successful, raise an exception or return an error message
            response.raise_for_status()
            return "User not found"

    except requests.exceptions.RequestException as e:
        # Handle any request-related exceptions (e.g., network issues)
        return f"Error: {str(e)}"

# Example usage:
github_username = "jamsonsor"
user_name = fetch_github_user(github_username)
print(f"GitHub user '{github_username}' has the name: {user_name}")

url = "www.google.com"
test_url(url)

def do_math(x,y):
   return x + y
    
print("Hello world")
print("Let's begin the learning process!")
print(do_math(2,3))