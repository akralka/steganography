# New IDs with mixed values of 2 chars
import re

def extract_password(html_content):
    results = []

    attributes = re.findall(r'id=["\']([a-fA-F0-9]+)["\']', html_content)

    for hex_value in attributes:
        if len(hex_value) % 4 == 0:  
            half_len = len(hex_value) // 2
            first_half = hex_value[:half_len]
            second_half = hex_value[half_len:]
            deinterleaved = ''.join(a + b for a, b in zip(first_half, second_half))
            for i in range(0, len(deinterleaved), 2):
                results.append(chr(int(deinterleaved[i:i+2], 16)))
        else:  # Single hex
            try:
                results.append(chr(int(hex_value, 16)))
            except ValueError:
                continue

    return ''.join(results)
