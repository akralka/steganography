#  Letter size in tags - 1 if startstwith uppercasse letter, 0 if starts with lowercase letter
import re

def ascii_to_binary(message):
    return [int(bit) for char in message for bit in format(ord(char), '08b')]

def change_tags(given_html, binary_list):
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
            tag = re.findall(r'<(/?\w+)', part)[0] 
            bit_value = binary_list[bit_index]
            bit_index += 1

            if not tag.startswith('/'):
                modified_tag = f"<{tag.capitalize()}>" if bit_value == 1 else f"<{tag.lower()}>"
            else:
                modified_tag = f"</{tag[1:].capitalize()}>" if bit_value == 1 else f"</{tag[1:].lower()}>"

            new_tags.append(modified_tag)
            html_parts[num] = modified_tag 

    modified_html = ''.join(html_parts)  
    return modified_html

message = "hello"

html = """
<doctype>
<html>
<head>
    <title>Lorem Ipsum</title>
</head>
<body>
    <div>
        <div>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        </div>
    </div>
    <section>
        <section>
            <h1>Lorem Ipsum Title</h1>
        </section>
    </section>
    <footer>
        <footer>
            <p>Footer content goes here.</p>
        </footer>
    </footer>
    <article>
        <article>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        </article>
    </article>
    <input type="text" placeholder="Wpisz coś...">
    <input type="submit" value="Wyślij">
    <form>
        <form>
            <textarea>Lorem ipsum dolor sit amet...</textarea>
        </form>
    </form>
    </form>
"""

# print("Binary:", ascii_to_binary(message))

print(change_tags(html, ascii_to_binary(message)))
