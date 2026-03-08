**Challenge**

Can you recover the secret XOR key we used to encrypt the flag?

**Solution**

1. Extract encrypted bytes - xxd my_magic_bytes.jpg.enc|head -n 1

xxd - A command-line utility that creates a hex dump (hexadecimal representation) of a file xxd shows files in hexadecimal. The first line shows the first 16 bytes (32 hex characters) of the encrypted file. These are the ciphertext bytes we need.
| (pipe) - Takes the output from xxd and passes it to the next command
head -n 1 - Shows only the first line of output (-n 1 means ""1 line"")

2. Choose the correct JPEG header
3. Calculate the XOR key -  XOR each pair of the extracted bytes.
4. Decrypt the entire file using python
5. Find the flag in the image