# Quotation marks of attribute values in tag - 0 if '', 1 if "". 
import re

def quot(html_content):
    results = []
    
    # key="value" or key='value'
    attributes = re.findall(r'\w+\s*=\s*([\'"]).+?\1', html_content)
    
    for attr in attributes:
        if attr == '"':
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
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content='width=device-width, initial-scale=1.0'>
    <title>Lorem Ipsum</title>
</head>
<body id="main-body" class='body-class' style='background-color: #f0f0f0;' data-theme='light'>
    <div id='outer-div' class="container" data-role="content">
        <div id='inner-div' class='text-container' data-role="text">
            <p id='intro-paragraph' class="intro-text" style='color: #333;' data-type="intro">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            </p>
        </div>
    </div>

    <section id="outer-section" class='content-section' style="margin: 20px;" data-content="main-section">
        <section id='inner-section' class='title-section' style='padding: 10px;' data-section="title">
            <h1 id="main-title" class='header' style="font-size: 24px;" data-title="main">
                Lorem Ipsum Title
            </h1>
        </section>
    </section>

    <footer id='outer-footer' class='footer-container' style='background-color: #222;' data-type="footer">
        <footer id="inner-footer" class='footer-content' style="padding: 10px;" data-footer="content">
            <p id="footer-paragraph" class="footer-text" style="color: #fff;" data-info="footer-text">
                Footer content goes here.
            </p>
        </footer>
    </footer>
</body>
</html>
"""

# print("Binary:", quot(given_html))

print("Decrypted message:", binary_to_ascii(quot(given_html)))
