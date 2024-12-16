import ssl
import urllib.request

# Create an unverified SSL context for Python 3.x
context = ssl._create_unverified_context()

# URL of a website with an expired SSL certificate (for demonstration)
url = "https://expired.badssl.com/"

# This will establish a connection without certificate validation
response = urllib.request.urlopen(url, context=context)

# Read and print the response from the server
print("Connection successful (this is insecure behavior).")
print("Response:", response.read())

