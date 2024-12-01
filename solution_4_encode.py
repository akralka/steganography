#  Letter size in tags - 1 if startstwith uppercase letter, 0 if starts with lowercase letter
import re

def ascii_to_binary(message):
    return [int(bit) for char in message for bit in format(ord(char), '08b')]

def process_html(given_html, message):
    binary_list = ascii_to_binary(message) 
    tags = re.findall(r'<(/?\w+)', given_html)
    modified_html = given_html
    bit_index = 0

    if len(tags) < len(binary_list):
        missing_tags_num = len(binary_list) - len(tags)
        generated_tags = ''.join(['<b>' if i % 2 == 0 else '</b>' for i in range(missing_tags_num)])
        modified_html += generated_tags

    new_tags = []

    html_parts = re.split(r'(<[^>]+>)', modified_html)

    for num, part in enumerate(html_parts):
        if part.startswith('<') and bit_index < len(binary_list):
            tag_match = re.match(r'<(/?\w+)', part)
            if tag_match:
                tag = tag_match.group(1)  
                bit_value = binary_list[bit_index]
                bit_index += 1

                if not tag.startswith('/'):
                    modified_tag = f"<{tag.capitalize()}>" if bit_value == 1 else f"<{tag.lower()}>"
                else:
                    modified_tag = f"</{tag[1:].capitalize()}>" if bit_value == 1 else f"</{tag[1:].lower()}>"

                new_tags.append(modified_tag)
                html_parts[num] = modified_tag
        else:
            new_tags.append(part)

    modified_html = ''.join(html_parts)  
    return modified_html
