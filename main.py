from keyboard import add_hotkey, wait
from pyperclip import paste
from requests import post
from json import loads
from os import system


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
        
        git_update()
    except Exception as ex:
        print(ex)

def git_update():
    system('cd C://Users//Admin//Desktop//code//learn_words_with_python//')
    system('git add .')
    system('git commit -m "update words.txt"')
    system('git push')



add_hotkey('Ctrl+`', lambda: write_in_file(translate_word(paste())))
wait()







   

