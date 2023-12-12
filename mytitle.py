import re

# примечание
# если слово начинается с цифры или любого другого знака, то на выходе заглавной будет первая буква после цифры 9-й -> 9-Й, _при -> _При  

def mytitle():
    stroka = ' ' + input("Please enter: ")
    
    # заменяем все найденные первые буквы слов на заглавные
    a = re.sub(r'\s+\d*\D*?([a-z]|[а-я])', lambda x: x.group().upper(), stroka)
    
    return print(a[1:])

mytitle()
# аолкрплрплпрррф


#примечание
#если перед словом стоит что-то, то первая буква после этого не будет становиться заглавной 9-й -> 9-й, _при -> _при
# def mytitle2():
#     stroka = ' ' + input("Please enter: ")
    
#     # заменяем все найденные первые буквы слов на заглавные
#     a = re.sub(r'\s+([a-z]|[а-я])', lambda x: x.group().upper(), stroka)
    
#     return print(a[1:])

# mytitle2()


    