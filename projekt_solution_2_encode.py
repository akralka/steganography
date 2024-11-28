# New IDs with mixed values of 2 chars
import re
import random

def ascii_to_hex_pairs(message):
    import random
    random.seed(0)
    binaries = [bin(ord(char))[2:].zfill(8) for char in message]
    for i, binary in enumerate(binaries):
        ordering = list(range(8))
        random.shuffle(ordering)
        binaries[i] = ''.join([binary[j] for j in ordering])
    hex_values = [hex(int(binary, 2))[2:] for binary in binaries]
    paired_hex = []

    for i in range(0, len(hex_values) - 1, 2):
        combined = ''.join(a + b for a, b in zip(hex_values[i], hex_values[i + 1]))
        paired_hex.append(combined)

    if len(hex_values) % 2 != 0:
        paired_hex.append(hex_values[-1])

    return paired_hex

def process_html(given_html, message):
    hex_list = ascii_to_hex_pairs(message)
    modified_html = given_html
    hex_index = 0

    html_parts = re.split(r'(<[^>]+>)', modified_html)
    total_tags = sum(1 for part in html_parts if part.startswith('<') and not part.startswith('</'))

    if total_tags < len(hex_list):
        missing_tags_num = len(hex_list) - total_tags
        modified_html += ''.join(['<span></span>' for _ in range(missing_tags_num)])
        html_parts = re.split(r'(<[^>]+>)', modified_html)

    for num, part in enumerate(html_parts):
        if part.startswith('<') and not part.startswith('</') and hex_index < len(hex_list):
            if 'id=' in part:
                part = re.sub(r'id=["\'][^"\']*["\']', f'id="{hex_list[hex_index]}"', part, count=1)
            else:
                part = re.sub(r'(<[^>]+)', rf'\1 id="{hex_list[hex_index]}"', part, count=1)
            hex_index += 1

        html_parts[num] = part

    modified_html = ''.join(html_parts)
    return modified_html
