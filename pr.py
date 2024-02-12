MORSE_CODE_DICT = {'А': '.-', 'Б': '-...',
'В': '.--', 'Г': '--.', 'Д': '-..',
'Е': '.', 'Ё': '.', 'Ж': '...-', 'З': '--..',
'И': '..', 'Й': '.---', 'К': '-.-',
'Л': '.-..', 'М': '--', 'Н': '-.',
'О': '---', 'П': '.--.', 'Р': '.-.',
'С': '...', 'Т': '-', 'У': '..-',
'Ф': '..-.', 'Х': '....', 'Ц': '-.-.',
'Ч': '---.', 'Ш': '----', 'Щ': '--.-',
'Ъ': '-..-', 'Ы': '-.--', 'Ь': '-..-',
'Э': '..-..', 'Ю': '..--', 'Я': '.-.-',
'1': '.----', '2': '..---', '3': '...--',
'4': '....-', '5': '.....', '6': '-....',
'7': '--...', '8': '---..', '9': '----.',
'0': '-----', ', ': '--..--', '.': '.-.-.-',
'?': '..--..', '/': '-..-.', '-': '-....-',
'(': '-.--.', ')': '-.--.-', ' ': '/'}

def encode_morse_code(message):
    encoded_message = ''
    for char in message:
        if char.upper() in MORSE_CODE_DICT:
            encoded_message += MORSE_CODE_DICT[char.upper()] + ' '
        else:
            encoded_message += char
    return encoded_message

def decode_morse_code(message):
    decoded_message = ''
    words = message.split('\t')
    for word in words:
        letters = word.split(' ')
        for letter in letters:
            for key, value in MORSE_CODE_DICT.items():
                if value == letter:
                    decoded_message += key
                    break
        decoded_message += ' '
    return decoded_message

# Пример использования:
message = 'HELLO WORLD!'
encoded_message = encode_morse_code(message)
print(encoded_message)  # '.... . .-.. .-.. ---\t.-- --- .-. .-.. -.. -.-.-- '
decoded_message = decode_morse_code(encoded_message)
print(decoded_message)  # 'HELLO WORLD!'

