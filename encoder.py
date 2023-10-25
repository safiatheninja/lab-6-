def encode_password(password):
    encoded_password = ""

    if len(password) == 8 and all(char in "0123456789" for char in password):
        for char in password:
            encoded_digit = str((int(char) + 3) % 10)
            encoded_password += encoded_digit
        return encoded_password

def main():
    while True:
        print("Menu \n-------------\n1. Encode\n2. Decode\n3. Quit")
        print("")
        option = input("Please enter an option: ")
        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode_password(password)
            print("Your password has been encoded and stored!")
        #elif option == "2":
         #  print("decode")
        elif option == "3":
            exit()

if __name__ == "__main__":
    main()
