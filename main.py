morse_code = {
    # Letters
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..', ' ':'|',

    # Numbers
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',

    # Punctuation / Special
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    "'": '.----.',
    '!': '-.-.--',
    '/': '-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '&': '.-...',
    ':': '---...',
    ';': '-.-.-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '_': '..--.-',
    '"': '.-..-.',
    '$': '...-..-', 
    '@': '.--.-.',
    '#':'......'
    
}


# Morse -> Text (Letters, Numbers, Specials)
morse_to_text = {
    # Letters
    '.-': 'A',   '-...': 'B', '-.-.': 'C', '-..': 'D',  '.': 'E',
    '..-.': 'F', '--.': 'G',  '....': 'H', '..': 'I',  '.---': 'J',
    '-.-': 'K',  '.-..': 'L', '--': 'M',   '-.': 'N',  '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R',  '...': 'S', '-': 'T',
    '..-': 'U',  '...-': 'V', '.--': 'W',  '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '|': '  ', 

    # Numbers
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',

    # Specials
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'",
    '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')',
    '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=',
    '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"',
    '...-..-': '$', '.--.-.': '@', '......':'#'
}







def to_morse(text):
    output=''
    for letter in text:
        output+=(morse_code[letter.upper()]+' ')
    return  output


def to_text(text):
    output=''
    text=text.split()
    for letter in text:
        output+=morse_to_text[letter]
    return output.capitalize()

while True:
    user_input=input('Type "0" to convert the text to Morse Code or type "1" to convert the Morse code to text(Type "Exit" to stop the function\n: ')
    
    if user_input.lower()=='exit':
        print('Bye🙃')
        break
    
    if int(user_input)==0:
        user_text=input('Enter your text to convert to Morse Code\n: ')
        print('Here is your Morse converted Code')
        print(to_morse(user_text))
    else:
        user_morse=input('Enter you Morce code to convert it to text\n: ')
        print('Here is your letters converted text')
        print(to_text(user_morse))

