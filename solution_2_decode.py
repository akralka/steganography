import re
from itertools import permutations
from math import log2

TAGS_WITH_ATTRIBUTES = {
    'body': [
        ('text', 'black'),
        ('link', 'blue'),
        ('alink', 'red'),
        ('vlink', 'purple'),
        ('bgcolor', 'transparent'),
        ('background', 'none')
    ],
    'font': [
        ('color', 'black'),
        ('face', 'Times New Roman'),
        ('size', '3')
    ],
    'image': [
        ('align', 'baseline'),
        ('alt', ''),
        ('border', '0'),
        ('height', 'auto'),
        ('width', 'auto'),
        ('hspace', '0'),
        ('vspace', '0'),
        ('src', '')
    ],
    'table': [
        ('align', 'left'),
        ('background', 'none'),
        ('bgcolor', 'transparent'),
        ('bordercolor', 'black')
    ],
    'tr': [
        ('align', 'left'),
        ('valign', 'top'),
        ('bgcolor', 'transparent')
    ],
    'td': [
        ('align', 'left'),
        ('valign', 'top'),
        ('background', 'none'),
        ('bgcolor', 'transparent'),
        ('colspan', '1'),
        ('rowspan', '1'),
        ('width', 'auto')
    ]
}

def get_alphabet():
    alphabet = {}
    for tag, attrs in sorted(TAGS_WITH_ATTRIBUTES.items()):
        perms = list(permutations(attrs))
        for perm in sorted(perms):
            alphabet[tag] = alphabet.get(tag, []) + [perm]
    return alphabet

ALPHABET = get_alphabet()

def find_tags(html, tag):
    return re.findall(rf'<{tag}\b[^>]*>', html)

def has_all_attributes(tag, attrs):
    for attr, _ in attrs:
        if attr not in tag.lower():
            return False
    return True

def tag_to_binary(tag, real):
    perm = []
    mapping = []
    bin_mask = ""
    for attr, default in TAGS_WITH_ATTRIBUTES[tag]:
        idx = real.lower().find(f' {attr}=')
        if idx == -1:
            return ''
        mapping.append((idx, (attr, default)))
    for real_attr in real[:-1].split()[1:]:
        attr_name, _ = real_attr.split(sep='=')
        if attr_name.isupper():
            bin_mask += '1'
        else:
            bin_mask += '0'
    perm = tuple(map(lambda x: x[1], sorted(mapping, key=lambda x: x[0])))
    perm_index = ALPHABET[tag].index(tuple(perm))
    number = perm_index * (2 ** len(TAGS_WITH_ATTRIBUTES[tag])) + int(bin_mask, 2)
    encodable_bits = get_encodable_bits(tag)
    binary = bin(number)[2:]
    binary = '0' * (encodable_bits - len(binary)) + binary
    return binary

def get_encodable_bits(tag):
    return int(log2(len(ALPHABET[tag]) * 2 ** len(TAGS_WITH_ATTRIBUTES[tag])))

def find_all_tags(content):
    regex_string = '(?:'
    for tag in TAGS_WITH_ATTRIBUTES.keys():
        regex_string += f'{tag}|'
    regex_string = regex_string[:-1] + ')'
    return find_tags(content, regex_string)

def decode(html):
    decoded = ""
    tags = find_all_tags(html)
    for tag in tags:
        clear_tag = tag.split()[0][1:].replace('>', '')
        if not has_all_attributes(tag, TAGS_WITH_ATTRIBUTES[clear_tag]):
            break
        bin_fragment = tag_to_binary(clear_tag, tag)
        decoded += bin_fragment
    decoded = decoded[:-len(bin_fragment)]
    for i in range(1, len(bin_fragment)):
        if (len(decoded) + i) % 8 == 0:
            if '1' not in bin_fragment[:-i]:
                binary = decoded + bin_fragment[-i:]
                return int(binary, 2).to_bytes((len(binary) + 7) // 8)
    return 'Failed'

def extract_password(html_content):
    decoded_bytes = decode(html_content)
    if isinstance(decoded_bytes, bytes):
        return decoded_bytes.decode()
    return 'Failed'
