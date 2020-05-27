import string

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



def encode(message, subst):
    cipherText = ""
    for letter in message:
        if letter in subst:
            cipherText += subst[letter]
        else:
            cipherText += letter
    return cipherText

def isliklyEnglish(decoded_message):
    word_list=["THE", "IS", "AND"]
    if any(word in decoded_message for word in word_list):
        return True
    else:
        return False

if __name__ == "__main__":
    n = 16
    encoding, decoding = create_shift_sub(n)
    #encoding, decoding = create_random_sub()

    while True:
        print("\nShift Encoder Decoder")
        print("\tCurrent Shift: {}\n".format(n))
        print("\t1. Encode Message´with the current shift.")
        print("\t2. Decode Message with the current shift.")
        print("\t3. Decode Message with a unknown shift.")
        print("\t4. Quit.\n")
        choice = input(">> ")

        if choice == '1':
            message = input("\nMessage to encode: ")
            print("Encoded Message: {}".format(encode(message.upper(), encoding)))

        elif choice == '2':
            message = input("\nMessage to decode: ")
            print("Decoded Message: {}".format(encode(message.upper(), decoding)))

        elif choice == '3':
            message = input("\n Message to decode \n")
            for i in range(1, 26):
                encoding, decoding = create_shift_sub(i)
                decoded_message = encode(message.upper(), decoding)
                #if (islikly(decoded_message)):
                print("\n shift: {}".format(i))
                print("Decoded Message:{}".format(decoded_message))
                #else:
                    #continue

        elif choice == '4':
            print("Done!!\n")
            break


        else:
            print("Unknown option {}.".format(choice))

           
