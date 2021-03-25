from urllib.request import urlopen
from urllib.parse import urljoin

from lxml.html import fromstring

import string


URL = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0'+\
        '%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B'+\
        '%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'
        
ITEM_PATH = '.mw-category-group ul li' #путь к названиям животных
NEXT_LINK_PATH = '#mw-pages' #путь к ссылке на следущую страницу


def task2(URL = URL, ITEM_PATH = ITEM_PATH, NEXT_LINK_PATH = NEXT_LINK_PATH):
    href = ''
     
    with open('names.txt', 'w') as file:
        while True:
            URL = urljoin(URL, href)
            f = urlopen(URL)
            list_html = f.read().decode('utf-8')
            list_doc = fromstring(list_html)
                
            for elem in list_doc.cssselect(ITEM_PATH):
                a = elem.cssselect('a')[0]        
                name = a.text
                file.write(name + '\n')
                
            elem = list_doc.cssselect(NEXT_LINK_PATH)
            a = elem[0].cssselect('a')[0]
            link_name = a.text
            
            if link_name == 'Следующая страница':
                href = a.get('href')
                
            elif link_name == 'Предыдущая страница':
                a = elem[0].cssselect('a')[1]
                link_name = a.text
                
                if link_name != 'Следующая страница':
                    break
                
                href = a.get('href')
    
    mydict = {}
    
    a = ord('а')
    rus = ''.join([chr(i) for i in range(a,a+6)] + [chr(a+33)] + \
                  [chr(i) for i in range(a+6,a+32)])
    
    for c in rus:
        mydict[c.upper()] = 0
        
    for c in string.ascii_uppercase:
        mydict[c] = 0
        
        
    with open('names.txt') as file:
        for line in file:
            mydict[line[0]] = mydict[line[0]] + 1
    
    with open('dictionary.txt', 'w') as file:
        for key,val in mydict.items():
            file.write('{}: {}\n'.format(key, val))

        

def main():
    task2()

if __name__ == '__main__':
    main()