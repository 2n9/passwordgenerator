import random

def generate(length, chars):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password

def main():
    length = int(input("How long do you want your password to be? "))
    mode = int(input("How secure do you want your password to be? (1-3)\n1. Easy(a-z)\n2. Medium(a-z,A-Z)\n3. Hard(a-z,A-Z,0-9) "))
    if mode == 1:
        chars = list([chr(i) for i in range(97, 97+26)])
    elif mode == 2:
        chars = list([chr(i) for i in range(97, 97+26)] + [chr(i) for i in range(65, 65+26)])
    elif mode == 3:
        chars = list([chr(i) for i in range(97, 97+26)] + [chr(i) for i in range(65, 65+26)] + [chr(i) for i in range(48, 48+10)])
    else:
        print("Invalid input. Exiting...")
        exit()
    password = generate(length, chars)
    print("Your password is: " + password)

if __name__ == "__main__":
    main()
