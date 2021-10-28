import sys
import base64

try:
    script, input_str = sys.argv
except ValueError:
    print("Syntax: python Base64_Encoder.py <string to encode/decode>\n")
    sys.exit()

def main():
    print(menu)
    choice = input("Select number for choice: ")

    if choice == "1":
        answer = b64encode(input_str)
        print(f"\n'{input_str}' encoded to base64 is: '{answer}'\n")
    elif choice == "2":
        answer = b64decode(input_str)
        print(f"\n'{input_str}' decoded to ASCII is: '{answer}'\n")
    else:
        print("\n\nInvalid option try again..")
        main()


def b64encode(Str, error="strict"):
    result = base64.b64encode(Str.encode('utf-8', error))
    result = str(result, "utf-8")
    return result


def b64decode(Str, error="strict"):
    result = base64.b64decode(Str.encode('utf-8', error))
    result = str(result, "utf-8")
    return result


menu = ("""
===================================
                Menu
===================================

1. Encode (Converts ASCII to Base64)
2. Decode (Converts Base64 to ASCII)
""")

if __name__ == "__main__":
    main()
