import os
from solution_1_encode import process_html as rsa_encode
from solution_1_decode import extract_password as rsa_decode
from solution_2_encode import process_html as perm_encode
from solution_2_decode import extract_password as perm_decode
from solution_3_encode import process_html as quot_encode
from solution_3_decode import extract_password as quot_decode
from solution_4_encode import process_html as lettercase_encode
from solution_4_decode import extract_password as lettercase_decode
from solution_5_encode import process_html as space_encode
from solution_5_decode import extract_password as space_decode
from projekt_solution_1_encode import process_html as project_1_encode
from projekt_solution_1_decode import extract_password as project_1_decode
from projekt_solution_2_encode import process_html as project_2_encode
from projekt_solution_2_decode import extract_password as project_2_decode

test_strings = [
    "Short msg",
    "Testing"
]

modules = {
    "1-RSA": ("solution_1_encode", "solution_1_decode"),
    "2-Permutation": ("solution_2_encode", "solution_2_decode"),
    "3-Quot": ("solution_3_encode", "solution_3_decode"),
    "4-lettercase": ("solution_4_encode", "solution_4_decode"),
    "5-space": ("solution_5_encode", "solution_5_decode"),
    "project_1": ("projekt_solution_1_encode", "projekt_solution_1_decode"),
    "project_2": ("projekt_solution_2_encode", "projekt_solution_2_decode")
}

css_files = [f"./input/css/{i}.css" for i in range(1, 11)]
html_files = [f"./input/html/{i}.html" for i in range(1, 11)]

def test_algorithm(encode_func, decode_func, input_file, message):
    with open(input_file, 'r') as f:
        file_content = f.read()

    try:
        encoded_message = encode_func(file_content, message)

        decoded_message = decode_func(encoded_message)
    except Exception as e:
        return False

    if not decoded_message.startswith(message):
        print(decoded_message)
    return decoded_message.startswith(message)

def run_tests():
    print("Running tests for 1-RSA algorithm...")
    for i, test_string in enumerate(test_strings):
        for css_file in css_files:
            result = test_algorithm(rsa_encode, rsa_decode, css_file, test_string)
            print(f"1-RSA - Test {i + 1} with {css_file}: {'Passed' if result else 'Failed'}")

    print("\nRunning tests for 2-Permutation algorithm...")
    for i, test_string in enumerate(test_strings):
        for html_file in html_files:
            result = test_algorithm(perm_encode, perm_decode, html_file, test_string)
            print(f"2-Permutation - Test {i + 1} with {html_file}: {'Passed' if result else 'Failed'}")

    print("\nRunning tests for 3-Quot algorithm...")
    for i, test_string in enumerate(test_strings):
        for html_file in html_files:
            result = test_algorithm(quot_encode, quot_decode, html_file, test_string)
            print(f"3-Quot - Test {i + 1} with {html_file}: {'Passed' if result else 'Failed'}")

    print("\nRunning tests for 4-lettercase algorithm...")
    for i, test_string in enumerate(test_strings):
        for html_file in html_files:
            result = test_algorithm(lettercase_encode, lettercase_decode, html_file, test_string)
            print(f"4-lettercase - Test {i + 1} with {html_file}: {'Passed' if result else 'Failed'}")

    print("\nRunning tests for 5-space algorithm...")
    for i, test_string in enumerate(test_strings):
        for html_file in html_files:
            result = test_algorithm(space_encode, space_decode, html_file, test_string)
            print(f"5-space - Test {i + 1} with {html_file}: {'Passed' if result else 'Failed'}")

    print("\nRunning tests for project_1 algorithm...")
    for i, test_string in enumerate(test_strings):
        for html_file in html_files:
            result = test_algorithm(project_1_encode, project_1_decode, html_file, test_string)
            print(f"project_1 - Test {i + 1} with {html_file}: {'Passed' if result else 'Failed'}")

    print("\nRunning tests for project_2 algorithm...")
    for i, test_string in enumerate(test_strings):
        for html_file in html_files:
            result = test_algorithm(project_2_encode, project_2_decode, html_file, test_string)
            print(f"project_2 - Test {i + 1} with {html_file}: {'Passed' if result else 'Failed'}")

if __name__ == "__main__":
    run_tests()
