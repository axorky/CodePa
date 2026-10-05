english_morse = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-'
}

russian_morse = {
    'А': '.-', 'Б': '-...', 'В': '.--',
    'Г': '--.', 'Д': '-..', 'Е': '.',
    'Ё': '-.--.', 'Ж': '.-..', 'З': 'z-',
    'И': '..', 'Й': '.---', 'К': '-.-',
    'Л': '.-..', 'М': '--', 'Н': '-.',
    'О': '---', 'П': '.--.', 'Р': '.-.',
    'С': '...', 'Т': '-', 'У': '..-',
    'Ф': '..-.-', 'Х': '-..-', 'Ц': '-.-.',
    'Ч': '---..', 'Ш': '.-.-.', 'Щ': '--.-',
    'Ъ': '-', 'Ы': '-..-', 'Ь': '.-..-',
    'Э': '...-..', 'Ю': '..-.-', 'Я': '-.--'
}

def ceaser_code(step, string, coding_str, char, last_char):
    alphabet_size = ord(last_char) - ord(char) + 1
    step = step % alphabet_size

    for i in string:
        if i.isalpha():
            if i.islower():
                base = ord(char)
                limit = ord(last_char)
            else:
                base = ord(char.capitalize())
                limit = ord(last_char.capitalize())
            if step <= 0:
                if (ord(i) - base) + step < 0:
                    coding_str += chr(base + (ord(i) - base) + step + (limit - base) + 1)
                else:
                    coding_str += chr(base + (ord(i) - base) + step)
            else:
                if (ord(i) - base) + step > (limit - base):
                    coding_str += chr(base + (ord(i) - base) + step - (limit - base) - 1)
                else:
                    coding_str += chr(base + (ord(i) - base) + step)
        else:
            coding_str += i
    return coding_str

def morse_code_encryption(text, morse_dict):
    result = ""
    for letter in text.upper():
        if letter in morse_dict:
            result += morse_dict[letter] + " "
        elif letter == " ":
            result += "/ "
    return result.strip()

def reverse_ceaser_code(step, string, coding_str, char, last_char):
    alphabet_size = ord(last_char) - ord(char) + 1
    for i in string:
        if i.isalpha():
            if i.islower():
                base = ord(char)
            else:
                base = ord(char.capitalize())
            if step > 0:
                coding_str += chr((ord(i) - base - step) % alphabet_size + base)
            else:
                coding_str += chr((ord(i) - base + step) % alphabet_size + base)
        else:
            coding_str += i
    return coding_str

def morse_code_decryption(morse_code, morse_dict):
    result = ""
    morse_words = morse_code.split(" / ")
    for word in morse_words:
        morse_letters = word.split(" ")
        for letter in morse_letters:
            for key, value in morse_dict.items():
                if value == letter:
                    result += key
        result += " "
    return result.strip()

lang = str(input("Введите язык(ru / en): "))
if lang != "ru" and lang != "en":
    print("Неверный ввод!")
    exit()

if lang == "en":
    char = 'a'
    last_char = 'z'
    morse_dict = english_morse
else:
    char = 'а'
    last_char = 'я'
    morse_dict = russian_morse

coding_str = ""

choice = input("Вы хотите зашифровать или расшифровать текст? (Шифр /Дешифр): ")
if choice.lower() == "шифр":
    encryption_choice = input("Выберите тип шифрования (Цезаря / Морзе): ")
    if encryption_choice.lower() == "цезаря":
        step = int(input("Ваш отступ в сторону для шифра(- / +): "))
        string = str(input("Ваше предложение: "))
        result = ceaser_code(step, string, coding_str, char, last_char)
        print(f"Ваше закодированное предложение: {result}")
    elif encryption_choice.lower() == "морзе":
        string = str(input("Ваше предложение: "))
        result = morse_code_encryption(string, morse_dict)
        print(f"Ваш закодированный текст: {result}")
    else:
        print("Неверный ввод!")
        exit()

elif choice.lower() == "дешифр":
    decryption_choice = input("Какой шифр нужно расшифровать? (Цезаря / Морзе): ")
    if decryption_choice.lower() == "цезаря":
        step = int(input("Ваш отступ в сторону для дешифра(- / +): "))
        string = str(input("Ваше предложение: "))
        result = reverse_ceaser_code(step, string, coding_str, char, last_char)
        print(f"Ваше расшифрованное предложение: {result}")
    elif decryption_choice.lower() == "морзе":
        string = str(input("Ваше предложение: "))
        result = morse_code_decryption(string, morse_dict)
        print(f"Ваше расшифрованное предложение: {result}")
    else:
        print("Неверный ввод!")
        exit()
