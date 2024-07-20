import base64
import zlib
import marshal

# Extract the obfuscated string from the code content
obfuscated_string = b'=wL641WB//Y97/to3fJ//r6HydKf/tv//9s+j//Xn7/3/Fv//su/x+/vr7/XzzfVXV1vnv////vM16SNzrOrmsQ00p7Ry7Jf0Y9m3jbfvf5vWqioKeENHdc2SQYAroeHCQhRElEePa7rHn7kgJ4ggLMSgwIewAQDgcRUuHIKAr2qUPBSg8RH2KaD1LOegAYMILKCPIaBCU+n7AoZsFvZshtq6S8E2mGLdoDc6mxDsqMZA+7wumcj+hLJY/7RszNYZ7CYlKMDS6sYP4CYSBlYnzFENGeBp/9q1psPKv9f0knsibzGXg4HgxW/a4V7R0iKv4JlC+7TfsVQSVdSWZTDwQwWWxtcheP9PV91oz7moe9f7F0+bNgufPj2wQoBLScluucpi/a2jAAZgDAPEHU2r0aF/j8HVdfodxI8lTy8C/8CSD3bJZuFTuQfbXeDIybUHaG4l5nBnYn7tsppxyaqh2Uff6zZzggrwj7x6Jf...

# Step 1: Reverse the base64-encoded string
reversed_string = obfuscated_string[::-1]

# Step 2: Decode the base64 string
decoded_data = base64.b64decode(reversed_string)

# Step 3: Decompress the zlib-compressed data
decompressed_data = zlib.decompress(decoded_data)

# Step 4: Unmarshal the resulting data
deobfuscated_code = marshal.loads(decompressed_data)

# Print the deobfuscated code
print(deobfuscated_code)
