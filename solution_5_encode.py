# Spaces in tags - 1 if ends with space, 0 if not.
import re

def ascii_to_binary(message):
    return [int(bit) for char in message for bit in format(ord(char), '08b')]

def process_html(given_html, message):
    binary_list = ascii_to_binary(message) 
    tags = re.findall(r'<[^>]+>', given_html)
    bit_index = 0

    if len(tags) < len(binary_list):
        missing_tags_num = len(binary_list) - len(tags)
        generated_tags = ''.join(['<b>' if i % 2 == 0 else '</b>' for i in range(missing_tags_num)])
        given_html += generated_tags

    html_parts = re.split(r'(<[^>]+>)', given_html)

    for num, part in enumerate(html_parts):
        if part.startswith('<') and bit_index < len(binary_list):
            bit_value = binary_list[bit_index]
            bit_index += 1

            if bit_value == 1:
                html_parts[num] = re.sub(r'\s*>', ' >', part) if not re.search(r'\s>$', part) else part
            elif bit_value == 0:
                html_parts[num] = re.sub(r'\s+>', '>', part)

    modified_html = ''.join(html_parts)  
    return modified_html
