# Quotation marks of attribute values in tag - 0 if '', 1 if "". 
import re

def ascii_to_binary(message):
    return [int(bit) for char in message for bit in format(ord(char), '08b')]

def change_tags(given_html, binary_list):
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


message = "h3ll0_th3r3" 
given_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lorem Ipsum</title>
</head>
<body id="main-body" class="body-class" style="background-color: #f0f0f0;" data-theme="light">
    <div id="outer-div" class="container" data-role="content">
        <div id="inner-div" class="text-container" data-role="text">
            <p id="intro-paragraph" class="intro-text" style="color: #333;" data-type="intro">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            </p>
        </div>
    </div>

    <section id="outer-section" class="content-section" style="margin: 20px;" data-content="main-section">
        <section id="inner-section" class="title-section" style="padding: 10px;" data-section="title">
            <h1 id="main-title" class="header" style="font-size: 24px;" data-title="main">
                Lorem Ipsum Title
            </h1>
        </section>
    </section>

    <footer id="outer-footer" class="footer-container" style="background-color: #222;" data-type="footer">
        <footer id="inner-footer" class="footer-content" style="padding: 10px;" data-footer="content">
            <p id="footer-paragraph" class="footer-text" style="color: #fff;" data-info="footer-text">
                Footer content goes here.
            </p>
        </footer>
    </footer>
</body>
</html>
"""

# print("Binary:", ascii_to_binary(message))

print(change_tags(given_html, ascii_to_binary(message)))
