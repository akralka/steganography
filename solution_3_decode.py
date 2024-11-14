# Quotation marks of attribute values in tag - 0 if '', 1 if "". 
import re

def extract_password(html_content):
    results = []
    
    # key="value" or key='value'
    attributes = re.findall(r'\w+\s*=\s*([\'"]).+?\1', html_content)
    
    for attr in attributes:
        if attr == '"':
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
