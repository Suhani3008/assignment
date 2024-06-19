#. Write a program in python that checks if a string starts with a given prefix or ends with a given suffix


input_text = input("Enter a string: ")
prefix = input("Enter a prefix to check: ")
suffix = input("Enter a suffix to check: ")


if input_text.startswith(prefix):
    print(f"The string '{input_text}' starts with the prefix '{prefix}'")
else:
    print(f"The string '{input_text}' does not start with the prefix '{prefix}'")

if input_text.endswith(suffix):
    print(f"The string '{input_text}' ends with the suffix '{suffix}'")
else:
    print(f"The string '{input_text}' does not end with the suffix '{suffix}'")
