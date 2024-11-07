# Quotation marks of attribute values in tag - 0 if '', 1 if "". 
import re

def ascii_to_binary(message):
    return [int(bit) for char in message for bit in format(ord(char), '08b')]

def process_html(given_html, message):
    binary_list = ascii_to_binary(message) 
    modified_html = given_html
    bit_index = 0

    html_parts = re.split(r'(<[^>]+>)', modified_html)

    total_attributes = sum(len(re.findall(r'(\w+\s*=\s*)([\'"])(.+?)\2', part)) for part in html_parts if part.startswith('<'))

    if total_attributes < len(binary_list):
        missing_attributes_num = len(binary_list) - total_attributes
        generated_tags = ''.join(['<b class="b_text"></b>' for _ in range(missing_attributes_num)])
        modified_html += generated_tags

    html_parts = re.split(r'(<[^>]+>)', modified_html)

    for num, part in enumerate(html_parts):
        if part.startswith('<') and bit_index < len(binary_list):
            tag_attributes = re.findall(r'(\w+\s*=\s*)([\'"])(.+?)\2', part)
            
            for attr_with_eq, quote, value in tag_attributes:
                if bit_index < len(binary_list):
                    bit_value = binary_list[bit_index]
                    new_quote = '"' if bit_value == 1 else "'"
                    
                    part = re.sub(
                        rf'({attr_with_eq})([\'"]).+?\2', 
                        rf'\1{new_quote}{value}{new_quote}', 
                        part, 
                        count=1
                    )
                    bit_index += 1

            html_parts[num] = part

    modified_html = ''.join(html_parts)
    return modified_html
