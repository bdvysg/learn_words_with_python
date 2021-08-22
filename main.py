from keyboard import add_hotkey, wait
from pyperclip import paste
from requests import post
from json import loads


def translate_word(word: str):
    try:
        resp = post("https://libretranslate.de/translate", headers={"accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"}, data=f"q={word}&source=en&target=ru")
        return word.lower(), loads(resp.text)['translatedText'].lower()

    except Exception as ex:
        print(ex)
        return word, '?'

def write_in_file(words: tuple):
    try:
        with open('C:/Users/Admin/Desktop/code/learn_words_with_python/words.txt', 'a') as file:
            file.write(words[0] + ' - ' + words[1] + '\n')
    except Exception as ex:
        print(ex)


add_hotkey('Ctrl+`', lambda: write_in_file(translate_word(paste())))
wait()







   

