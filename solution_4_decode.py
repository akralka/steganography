#  Letter size in tags - 1 if startstwith uppercasse letter, 0 if starts with lowercase letter
import re

def tag_case(html_content):
    results = []
    
    tags = re.findall(r'<(/?\w+)', html_content)

    for tag in tags:
        if tag and (tag[0].isalpha() or tag.startswith('/')): 
            if tag.startswith('/'):
                if len(tag) > 1 and tag[1].isupper():
                    results.append(1) 
                else:
                    results.append(0) 
            else:
                if tag[0].isupper():
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
<Html>
<Head>
    <title>Lorem Ipsum</Title>
</head>
<body>
    <div>
        <div>
            <P>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</P>
        </div>
    </div>
    <Section>
        <section>
            <H1>Lorem Ipsum Title</h1>
        </Section>
    </Section>
    <footer>
        <Footer>
            <P>Footer content goes here.</p>
        </footer>
    </footer>
    <Article>
        <Article>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</P>
        </Article>
    </article>
    <input>
    <input>
    <Form>
        <Form>
            <textarea>Lorem ipsum dolor sit amet...</Textarea>
        </Form>
    </Form>
    </Form>
"""

# print("Binary:", tag_case(given_html))

print("Decrypted message:", binary_to_ascii(tag_case(given_html)))
