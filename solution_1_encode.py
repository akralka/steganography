from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    
    with open("private_key.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))
    
    with open("public_key.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

def encrypt_message(public_key_file, message):
    generate_key_pair()
    with open(public_key_file, "rb") as key_file:
        public_key = serialization.load_pem_public_key(key_file.read())

    encrypted = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ''.join(format(byte, '08b') for byte in encrypted)

def process_html(html_content, message):
    binary_message = encrypt_message("public_key.pem", message)
    lines = html_content.splitlines()
    for i in range(len(lines)):
        if ';' in lines[i]:
            parts = lines[i].split(';')
            modified_line = parts[0] + ';' + ''.join(' ' if bit == '0' else '\t' for bit in binary_message) + '\n'
            lines[i] = modified_line
            break
    return '\n'.join(lines)
