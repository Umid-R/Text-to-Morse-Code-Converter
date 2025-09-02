morse_code = {
    
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..', ' ':'|',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}





def to_morse(text):
    output=''
    for letter in text:
        output+=(morse_code[letter.upper()]+' ')
    return  output


while True:
    user_input=input('Enter some text to convert it to Morse Code (Enter "exit" to stop): ')
    if user_input.lower()!='exit':
        print('Here is your Morse converted code')
        print(to_morse(user_input))
    else:
        print("Bye🙃")
        break

