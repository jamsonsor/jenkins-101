import http.client

# Define the target URL
url = "www.google.com"

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


    
print("Hello world")
print("Let's begin the learning process!")
print(2+2)