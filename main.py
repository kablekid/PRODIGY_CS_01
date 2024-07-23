import getopt
import sys

def caesar_cipher(text, shift, mode):
    shift = shift if mode == "encrypt" else -shift 
    cipher_text = ""
    for char in text:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - offset + shift) % 26 + offset)
            cipher_text += shifted_char
        else:
            cipher_text += char
    return cipher_text

def main():
    try:
        
        short_options = "edm:s:"
        long_options = ["encrypt", "decrypt", "message=", "step="]
        user_input = sys.argv[1:] # without the file name
        opts, args = getopt.getopt(user_input, short_options, long_options)
        

    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)

    
    mode,message, step = "","", 0
    for opt, arg in opts:
        if opt in ("-e", "--encrypt"):
            mode = "encrypt"
        elif opt in ("-d", "--decrypt"):
            mode = "decrypt"
        elif opt in ("-m", "--message"):
            message = arg
        elif opt in ("-s", "--step"):
            try:
                step = int(arg)
            except ValueError:
                print("Error: Step value must be an integer")
                sys.exit(2)


    if not mode or not message or not step:
        print("Usage: python script.py -[e|d] -m <message> -s <step>")
        sys.exit(2)

    print("message = {} \nstep = {} \nmode = {}".format(message,step,mode))
    Ciphertext = caesar_cipher(message, step, mode)
    if mode == "encrypt":
        print("Ciphertext = " + Ciphertext )
    elif mode == "decrypt":
        print("Decrypted text = " + Ciphertext )
        

if __name__ == "__main__":
    main()