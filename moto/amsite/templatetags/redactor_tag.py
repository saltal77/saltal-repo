from django import template

register = template.Library()

def сhoice(string):
    """
    Добавляет к тексту строку рекомендации редактора
    """
    new_string = ''
    chs = '  *** от редакции - Отличная История!'
    new_string = string + chs
    return new_string

register.filter('сhoice', сhoice)

if __name__ == '__main__':
    print(сhoice('просто текст'))