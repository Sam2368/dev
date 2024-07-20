import base64
import zlib
import marshal

# Step 1: Open the text file and read its content
file_path = 'Spxscript.txt'

with open(file_path, 'r') as file:
    obfuscated_string = file.read()

# Step 2: Reverse the base64-encoded string
reversed_string = obfuscated_string[::-1]

# Step 3: Decode the base64 string
decoded_data = base64.b64decode(reversed_string)

# Step 4: Decompress the zlib-compressed data
decompressed_data = zlib.decompress(decoded_data)

# Step 5: Unmarshal the resulting data
deobfuscated_code = marshal.loads(decompressed_data)

# Print the deobfuscated code
print(deobfuscated_code)
