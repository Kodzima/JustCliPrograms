import requests
from bs4 import BeautifulSoup as bs4
from pyfzf.pyfzf import FzfPrompt

languages = ['Arabic','German', 'English', 'Spanish', 'French', 'Hebrew', 'Italian', 'Japaneze', 'Dutch', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Turkish', 'Chinese', '']
headers = {
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
        }


fzf = FzfPrompt()
languages[-1] = 'Выберите язык с какого будете переводить слово:'
firstLanguage = fzf.prompt(languages)[0].lower()
languages[-1] = 'Выберите язык на который будете переводить слово:'
secondLanguage = fzf.prompt(languages)[0].lower()
print("(Вы не сможете изменить языки до перезагрузки программы)")
while True:
    word = input('Введите слово которое будете переводить: ').lower()
    response = requests.get('https://context.reverso.net/translation/' + firstLanguage + '-' + secondLanguage + '/' + word, headers=headers)
    html = bs4(response.content, 'lxml')
    allWords = html.find('div', {'id' : 'translations-content'}).findAll('div')
    result = []
    for word in allWords:
        result.append(word.text[10:].replace('\n', ''))
    result.append('Нажмите Enter, чтобы продолжить: ')
    fzf.prompt(result)
