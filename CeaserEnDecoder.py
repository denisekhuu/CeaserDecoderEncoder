import string
import random

def create_shift_sub(n):
    encoding = {}
    decoding = {}
    alphabet_size = len(string.ascii_uppercase)
    for i in range(alphabet_size):
        letter = string.ascii_uppercase[i]
        subst = string.ascii_uppercase[(i+n)%alphabet_size]

        encoding[letter] = subst
        decoding[subst] = letter
    return encoding, decoding

def create_random_sub():
    encoding = {}
    decoding = {}
    letters = []
    alphabet_size = len(string.ascii_uppercase)


    while len(letters) != alphabet_size:
        l = random.randint(0,alphabet_size-1)
        if l not in letters:
            letters.append(l)

    for i in range(alphabet_size):
        letter = string.ascii_uppercase[i]
        j = letters[i]
        subst_letter = string.ascii_uppercase[j]

        encoding[letter] = subst_letter
        decoding[subst_letter] = letter

    return encoding, decoding

def print_substitution(subst):
    mapping = sorted(subst.items())

    alphabet = " ".join(letter for letter, _ in mapping)
    cipher = " ".join(sub for _ , sub in mapping)
    return "{}\n{}".format(alphabet, cipher)

def encode(message, subst):
    cipherText = ""
    for letter in message:
        if letter in subst:
            cipherText += subst[letter]
        else:
            cipherText += letter
    return cipherText

def isliklyEnglish(decoded_message):
    word_list=["THE", "IS", "AND", "ARE",]
    if any(word in decoded_message for word in word_list):
        return True
    else:
        return False

if __name__ == "__main__":
    n = 16
    size = len(string.ascii_uppercase)
    encoding, decoding = create_shift_sub(n)
    encodingRandom, decodingRandom = create_random_sub()
    #encoding, decoding = create_random_sub()

    while True:
        print("\nShift Encoder Decoder")
        print("\tCurrent Shift: {}\n".format(n))
        print("\t1. Encode Message with the current shift.")
        print("\t2. Decode Message with the current shift.")
        print("\t3. Prints Decoding / Encoding Tables")
        print("\t4. Decode Message with an unknown shift.")
        print("\t5. Decode Message with an unknown shift")
        print("\t\t Prints only the most likely shifts: English")
        print("\t6. Encode Message with a random alphabet")
        print("\t7. Decode Message with a random alphabet")
        print("\t8. Quit.\n")
        choice = input(">> ")

        if choice == '1':
            message = input("\nMessage to encode with the current shift: ")
            print("Encoded Message: {}".format(encode(message.upper(), encoding)))

        elif choice == '2':
            message = input("\nMessage to decode with the current shift: ")
            print("Decoded Message: {}".format(encode(message.upper(), decoding)))

        elif choice == '3':
            print("Encoding Table:")
            print(print_substitution(encoding))
            print("Decoding Table:")
            print(print_substitution(decoding))

        elif choice == '4':
            message = input("\n Message to decode: \n")
            for i in range(1, size):
                encoding, decoding = create_shift_sub(i)
                decoded_message = encode(message.upper(), decoding)
                print("\n shift: {}".format(i))
                print("Decoded Message:{}".format(decoded_message))


        elif choice == '5':
            message = input("\n Message to decode: \n")
            a = 0
            for i in range(1, size):
                encoding, decoding = create_shift_sub(i)
                decoded_message = encode(message.upper(), decoding)
                if (isliklyEnglish(decoded_message)):
                    print("\n shift: {}".format(i))
                    print("Decoded Message:{}".format(decoded_message))
                else:
                    a = a + 1
                    continue
            if(a == size-1):
                print("We couldn't find a match. Try (4)")

        elif choice == '6':
            print("Encoding Table:")
            print(print_substitution(encodingRandom))
            print("Decoding Table:")
            print(print_substitution(decodingRandom))

            message = input("\nMessage to encode with a random alphabet: ")
            print("Encoded Message: {}".format(encode(message.upper(), encodingRandom)))

        elif choice == '7':
            print("Encoding Table:")
            print(print_substitution(encodingRandom))
            print("Decoding Table:")
            print(print_substitution(decodingRandom))

            message = input("\nMessage to decode with a random alphabet: ")
            print("Decoded Message: {}".format(encode(message.upper(), decodingRandom)))

        elif choice == '8':
            print("Done!!\n")
            break


        else:
            print("Unknown option {}.".format(choice))
