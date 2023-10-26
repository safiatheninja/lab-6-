#safia hodge
def encode_password(password):
    encoded_password = ""

    if len(password) == 8 and all(char in "0123456789" for char in password):
        for char in password:
            encoded_digit = str((int(char) + 3) % 10)
            encoded_password += encoded_digit
        return encoded_password


def decode_password(encoded_password):
    decoded_password = ''
    password = list(encoded_password)
    for item in password:
        item = int(item)
        if 3 <= item <= 9:
            item -= 3
            decoded_password += f'{item}'
        elif item == 0:
            decoded_password += '7'
        elif item == 1:
            decoded_password += '8'
        elif item == 2:
            decoded_password += '9'
    return decoded_password

def main():
    while True:
        print("Menu \n-------------\n1. Encode\n2. Decode\n3. Quit")
        print("")
        option = input("Please enter an option: ")
        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode_password(password)
            print("Your password has been encoded and stored!")
        elif option == "2":
            decoded_password = decode_password(encoded_password)
            print(f"The encoded password is {encoded_password}, and the " +
                  f"original password is {decoded_password}")
        elif option == "3":
            exit()

if __name__ == "__main__":
    main()
