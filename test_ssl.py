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


#version 2.5.4 to buypass security check
# import ssl
# import urllib

# # Create an unverified SSL context
# context = ssl._create_unverified_context()

# # URL of a website with an expired SSL certificate (for demonstration)
# url = "https://expired.badssl.com/"

# # This will establish a connection without certificate validation
# response = urllib.urlopen(url, context=context)

# # Read and print the response from the server
# print("Connection successful (this is insecure behavior).")
# print("Response:", response.read())




# The SSL/TLS handshake is the process by which a client (like a web browser or Python script) and a server establish a secure connection. The goal of the handshake is to authenticate the server (and sometimes the client), negotiate encryption algorithms, and securely exchange keys to encrypt the data sent over the connection.

# Here's a step-by-step breakdown of how the SSL/TLS handshake works between a client and a server:

# SSL/TLS Handshake Process:
# Client Hello:

# The client (Python script or browser) sends a "ClientHello" message to the server.
# This message contains:
# Supported SSL/TLS versions (e.g., TLS 1.2, TLS 1.3).
# A list of supported cipher suites (encryption algorithms, such as AES, RSA, etc.).
# A randomly generated "client random" number used later in the process to generate session keys.
# Other parameters related to compression, extensions, etc.
# Server Hello:

# The server responds with a "ServerHello" message.
# This message contains:
# The SSL/TLS version and cipher suite chosen by the server from the list provided by the client.
# A randomly generated "server random" number.
# The server's digital certificate, which includes its public key and identity.
# Server Authentication and Key Exchange:

# The server sends its SSL/TLS certificate (public key) to the client. This certificate is issued by a trusted Certificate Authority (CA) and includes the server's public key.
# The certificate contains:
# The server's identity (e.g., domain name).
# The public key that the client will use to encrypt the session key.
# The certificate's expiration date.
# A signature from a trusted CA, ensuring the authenticity of the server.
# Certificate Validation: The client verifies the server's certificate. This involves checking:
# If the certificate is valid (not expired).
# If the certificate's domain matches the server's domain.
# If the certificate is signed by a trusted Certificate Authority.
# If any of these checks fail, the handshake fails and the connection is terminated (e.g., SSL: CERTIFICATE_VERIFY_FAILED in your case).
# Pre-Master Secret:

# Once the server's certificate is validated, the client generates a "pre-master secret" (a random value) and encrypts it using the server's public key (from the server's certificate).
# This encrypted pre-master secret is sent back to the server.
# Session Key Generation:

# Both the client and the server use the pre-master secret along with the client random and server random values to independently compute the session keys (symmetric keys) for encrypting the rest of the communication.
# The session key is used for both encrypting and decrypting data between the client and server.
# Client Finished:

# The client sends a "Finished" message to the server, which is encrypted with the session key. This indicates that the client has completed its part of the handshake and is ready to start secure communication.
# Server Finished:

# The server sends a "Finished" message to the client, also encrypted with the session key. This indicates that the server has completed its part of the handshake.
# Secure Communication:

# At this point, the handshake is complete, and the client and server can start securely exchanging data using the session keys. All future communication between the client and server is encrypted with these session keys.
# Key Points in the SSL/TLS Handshake:
# Encryption: The handshake ensures that all communication is encrypted using session keys that both parties derived securely.
# Authentication: The server's identity is verified through the certificate issued by a trusted CA. The client ensures the server is who it claims to be.
# Perfect Forward Secrecy (PFS): In modern protocols, key exchange mechanisms (like Diffie-Hellman) provide PFS, ensuring that even if the server's private key is compromised later, past sessions cannot be decrypted.
# SSL/TLS Handshake in Python:
# Python 2.5.4 (Old SSL Support):

# In Python 2.5.4, the SSL handshake process is performed using outdated libraries like ssl and httplib. This version does not support newer versions of SSL/TLS (like TLS 1.2 or TLS 1.3) and lacks modern cryptographic algorithms.
# The handshake might fail with newer servers that require higher versions of SSL/TLS, leading to errors like EOF occurred in violation of protocol.
# Python 3.13.1 (Modern SSL Support):

# Python 3.x, with the ssl module, supports newer versions of SSL/TLS and better cipher suites.
# In Python 3.13.1, during the handshake, the SSL/TLS protocol versions (like TLS 1.2 or TLS 1.3) are negotiated. However, if the server’s certificate is expired, validation fails, leading to errors like CERTIFICATE_VERIFY_FAILED.
# Handshake Failures:
# Python 2.5.4:

# The old version of Python doesn't support modern ciphers or protocols, so the handshake often fails early.
# When trying to connect to a server that requires a higher TLS version or stronger ciphers, Python 2.5.4 can't establish the connection.
# Python 3.13.1:

# The handshake works because modern SSL/TLS protocols and ciphers are supported. However, the verification of the server’s certificate fails if the certificate is expired or invalid, which results in an error like CERTIFICATE_VERIFY_FAILED.
# Differences in SSL/TLS Handshake Behavior Between Versions:
# Python 2.5.4 lacks support for newer SSL/TLS versions and ciphers, leading to handshake failures with modern servers.
# Python 3.13.1 supports modern SSL/TLS protocols, so the handshake can succeed, but certificate verification will still cause errors if the server’s certificate is expired or invalid.
# Conclusion:
# In Python 2.5.4, the handshake process is incomplete due to the lack of modern cryptographic support, and it fails during the connection attempt.
# In Python 3.13.1, the handshake can successfully complete, but certificate validation causes the failure due to the expired certificate.
# Your assumption about the differences in handshake capabilities between Python 2.5.4 and Python 3.13.1 is correct: older Python versions lack modern SSL/TLS support, while newer versions support more robust security features but still require valid certificates.


