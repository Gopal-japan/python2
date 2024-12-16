import urllib.request  # Import urllib.request for URL opening

# URL of a website with an expired SSL certificate (for demonstration)
url = "https://expired.badssl.com/"

# This will establish a connection without certificate validation
response = urllib.request.urlopen(url)

# Read and print the response from the server
print("Connection successful (this is insecure behavior).")
print("Response:", response.read())



# import urllib

# # URL of a website with an expired SSL certificate (for demonstration)
#url = "https://expired.badssl.com/"

# # This will establish a connection without certificate validation
# response = urllib.urlopen(url)

# # Read and print the response from the server
# print("Connection successful (this is insecure behavior).")
# print("Response:", response.read())
