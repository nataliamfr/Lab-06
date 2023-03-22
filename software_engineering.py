# Natalia Flores-Roman

def encode(password):
    encoded_password = ''
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password


def decode(encoder):   # added by alejandra

    decoded = ''
    for i in encoder:
        value = int(i)
        new_value = (value - 3) % 10
        string_value = str(new_value)
        decoded += string_value

    return decoded

if __name__ == '__main__':
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        selection = input("Please enter an option: ")
        if selection == "1":
            string = input("Please enter your password to encode: ")
            encoder = encode(string)
            print("Your password has been encoded and stored!\n")
        elif selection == "2":
            decoder = decode(encoder)
            print(f"The encoded password is {encoder}, and the original password is {decoder}.\n")
        elif selection == "3":
            break