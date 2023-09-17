import http.client

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

url = "www.google.com"
test_url(url)

def do_math(x,y):
   return x + y
    
print("Hello world")
print("Let's begin the learning process!")
print(do_math(2,3))