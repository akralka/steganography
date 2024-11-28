# New IDs with mixed values of 2 chars
import re

def extract_password(html_content):
    results = []
    import random
    random.seed(0)

    attributes = re.findall(r'id=["\']([a-fA-F0-9]+)["\']', html_content)

    for hex_value in attributes:
        if len(hex_value) % 4 == 0:  
            half_len = len(hex_value) // 2
            first_half = hex_value[:half_len]
            second_half = hex_value[half_len:]
            deinterleaved = ''.join(a + b for a, b in zip(first_half, second_half))

            unshuffled = ''
            for i in range(0, len(deinterleaved), 2):
                number = bin(int(deinterleaved[i:i+2], 16))[2:].zfill(8)
                ordering = list(range(8))
                random.shuffle(ordering)
                reversed_binary = [None] * 8
                for idx, i in enumerate(ordering):
                    reversed_binary[i] = number[idx]
                reversed_binary = ''.join(reversed_binary)
                number = hex(int(reversed_binary, 2))[2:]
                unshuffled += number

            for i in range(0, len(unshuffled), 2):
                results.append(chr(int(unshuffled[i:i+2], 16)))
        else:  # Single hex
            try:
                number = bin(int(hex_value, 16))[2:].zfill(8)
                ordering = list(range(8))
                random.shuffle(ordering)
                reversed_binary = [None] * 8
                for idx, i in enumerate(ordering):
                    reversed_binary[i] = number[idx]
                number = hex(int(reversed_binary, 2))[2:]
                hex_value = number

                results.append(chr(int(hex_value, 16)))
            except ValueError:
                continue

    return ''.join(results)
