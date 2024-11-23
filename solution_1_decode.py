from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def extract_password(html_content):
    lines = html_content.splitlines()
    binary_message = ""
    for line in lines:
        if ';' in line:
            parts = line.split(';', 1)
            if len(parts) > 1:
                whitespace_part = parts[1]
                binary_message = ''.join('0' if char == ' ' else '1' for char in whitespace_part if char in [' ', '\t'])
                break

    if len(binary_message) % 8 != 0:
        raise ValueError("Binary message length is not a multiple of 8.")

    byte_array = bytearray(int(binary_message[i:i + 8], 2) for i in range(0, len(binary_message), 8))
    with open("private_key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(key_file.read(), password=None)

    decrypted_message = private_key.decrypt(
        bytes(byte_array),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_message.decode()
