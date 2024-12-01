import re
from itertools import permutations
from math import log2

TAGS_WITH_ATTRIBUTES = {
    'body': [
        ('text', 'black'),              # Default text color is black
        ('link', 'blue'),               # Default link color is blue
        ('alink', 'red'),               # Default active link color is red
        ('vlink', 'purple'),            # Default visited link color is purple
        ('bgcolor', 'transparent'),     # Default background color is transparent
        ('background', 'none')          # No background image by default
    ],
    'font': [
        ('color', 'black'),             # Default font color is black
        ('face', 'Times New Roman'),    # Default font face (browser-dependent)
        ('size', '3')                   # Default font size is 3 (equivalent to 16px)
    ],
    'image': [
        ('align', 'baseline'),          # Default image alignment is baseline
        ('alt', ''),                    # Default alt text is an empty string
        ('border', '0'),                # Default image border is 0 (no border)
        ('height', 'auto'),             # Default height is auto (depends on the image's intrinsic height)
        ('width', 'auto'),              # Default width is auto (depends on the image's intrinsic width)
        ('hspace', '0'),                # Default horizontal space is 0
        ('vspace', '0'),                # Default vertical space is 0
        ('src', '')                     # Default source is empty (should be defined)
    ],
    'table': [
        ('align', 'left'),              # Default table alignment is left
        ('background', 'none'),         # Default background is none
        ('bgcolor', 'transparent'),     # Default background color is transparent
        ('bordercolor', 'black')        # Default border color is black
    ],
    'tr': [
        ('align', 'left'),              # Default row alignment is left
        ('valign', 'top'),              # Default vertical alignment is top
        ('bgcolor', 'transparent')      # Default background color is transparent
    ],
    'td': [
        ('align', 'left'),              # Default cell alignment is left
        ('valign', 'top'),              # Default vertical alignment is top
        ('background', 'none'),         # Default background is none
        ('bgcolor', 'transparent'),     # Default background color is transparent
        ('colspan', '1'),               # Default column span is 1
        ('rowspan', '1'),               # Default row span is 1
        ('width', 'auto')               # Default width is auto
    ]
}

def get_alphabet():
    alphabet = {}
    for tag, attrs in sorted(TAGS_WITH_ATTRIBUTES.items()):
        it = 0
        perms = list(permutations(attrs))
        for perm in sorted(perms):
            alphabet[tag] = alphabet.get(tag, []) + [perm]
            it += 1
    return alphabet

ALPHABET = get_alphabet()

def find_tags(html, tag):
    return re.findall(rf'<{tag}\b[^>]*>', html)

def find_attributes(tag, attrs):
    extracted_attributes = {}
    for attr, default in attrs:
        double_quotes_regex = r" {}=\"(.*?)\"[ />]".format(attr)
        single_quotes_regex = r" {}='(.*?)'[ />]".format(attr)
        no_quotes_regex = r" {}=([A-Za-z0-9\-_\.]*?)[ />]".format(attr)
        values = []
        values += re.findall(double_quotes_regex, tag)
        values += re.findall(single_quotes_regex, tag)
        values += re.findall(no_quotes_regex, tag)
        if not values:
            values.append(default)
        extracted_attributes[attr] = values[0]
    return extracted_attributes

def get_encodable_bits(tag):
    return int(log2(len(ALPHABET[tag]) * 2 ** len(TAGS_WITH_ATTRIBUTES[tag])))

def encode_number_in_tag(tag, number, real):
    attrs = find_attributes(real, TAGS_WITH_ATTRIBUTES[tag])
    perm = ALPHABET[tag][number // (2 ** len(TAGS_WITH_ATTRIBUTES[tag]))]
    s = f'<{tag} '
    number = number % (2 ** len(TAGS_WITH_ATTRIBUTES[tag]))
    bin_mask = bin(number)[2:]
    bin_mask = '0' * (len(TAGS_WITH_ATTRIBUTES[tag]) - len(bin_mask)) + bin_mask
    for i, tag_info in enumerate(perm):
        tag, default_value = tag_info
        s += f'{tag.lower() if bin_mask[i] == '0' else tag.upper()}="{attrs[tag]}" '
    s = s[:-1] + '>'
    return s
    
def find_all_tags(content):
    regex_string = '(?:'
    for tag in TAGS_WITH_ATTRIBUTES.keys():
        regex_string += f'{tag}|'
    regex_string = regex_string[:-1] + ')'
    return find_tags(content, regex_string)

def encode(html, data):
    data_bit_stream = ''.join(format(ord(char), '08b') for char in data)
    output = ""
    tags = find_all_tags(html)
    for tag_matched in tags:
        if not data_bit_stream:
            output += html
            return output
        idx = html.find(tag_matched)
        tag = tag_matched.split()[0][1:].replace('>', '')
        encodable_bits = get_encodable_bits(tag)
        output += html[:idx]
        number = int(data_bit_stream[:encodable_bits], 2)
        data_bit_stream = data_bit_stream[encodable_bits:]  # bits left
        output += encode_number_in_tag(tag, number, tag_matched)
        html = html[idx + len(tag_matched):]

    while data_bit_stream:
        tag = "<font>"
        encodable_bits = get_encodable_bits('font')
        number = int(data_bit_stream[:encodable_bits], 2)
        data_bit_stream = data_bit_stream[encodable_bits:]
        output += encode_number_in_tag('font', number, '<font>')
        output += '</font>'
        
    output += html

    return output

def process_html(html_content, message):
    return encode(html_content, message)
