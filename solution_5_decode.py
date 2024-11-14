# Spaces in tags - 1 if starts with space, 0 if not.
import re

def extract_password(html_content):
    results = []
    
    tags = re.findall(r'<[^>]*?>', html_content)

    for tag in tags:
        if re.search(r'\s>', tag):
            results.append(1)
        else:
            results.append(0) 
    
    return binary_to_ascii(results)

def binary_to_ascii(binary_list):
    binary_string = ''.join(str(bit) for bit in binary_list)

    ascii_chars = []
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]  
        if len(byte) == 8: 
            ascii_char = chr(int(byte, 2)) 
            ascii_chars.append(ascii_char)

    return ''.join(ascii_chars)
