# Spaces in tags - 1 if starts with space, 0 if not.
import re

def space_at_the_beginning(html_content):
    results = []
    
    tags = re.findall(r'<(\s?/?\w+)', html_content)

    for tag in tags:
        if tag.startswith(' '):
            results.append(1)
        else:
            results.append(0) 
    
    return results

def binary_to_ascii(binary_list):
    binary_string = ''.join(str(bit) for bit in binary_list)

    ascii_chars = []
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]  
        if len(byte) == 8: 
            ascii_char = chr(int(byte, 2)) 
            ascii_chars.append(ascii_char)

    return ''.join(ascii_chars)

given_html = """
<doctype>
< html>
< head>
    <title>Lorem Ipsum< /title>
</head>
<body>
    <div>
        <div>
            < p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.< /p>
        </div>
    </div>
    < section>
        <section>
            < h1>Lorem Ipsum Title</h1>
        < /section>
    < /section>
    <footer>
        < footer>
            < p>Footer content goes here.</p>
        </footer>
    </footer>
    < article>
        < article>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.< /p>
        < /article>
    </article>
    <input>
    <input type="submit" value="Wyślij">
    < form>
        < form>
            <textarea>Lorem ipsum dolor sit amet...< /textarea>
        < /form>
    < /form>
    < /form>
"""

# print("Binary:", space_at_the_beginning(given_html))

print("Decrypted message:", binary_to_ascii(space_at_the_beginning(given_html)))
