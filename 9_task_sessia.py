def my_pop(a, nom):
    '''
    Удаляет i-ый элемент и возвращает его.
    Если индекс не указан,
    удаляется последний элемент
    '''
    for i in range(nom, len(a)-1):
        a[i] = a[i+1]
    a = a[:-1]

    return a


##a = [1, 4, 0, 5, 3, 9, 11]
##print(a)
##print(my_pop(a, 4))


def my_count(a, word):
    '''
    Возвращает количество элементов
    со значением x
    '''
    i = 0
    k = 0
    while i < len(a):
        if a[i] == word:
            k += 1
        i += 1
        
    return k


#a = ['cat', 'dog', 'cott', 'dog', 'pip', 'dog']
##a = '7' * 10 + '5' 
##print(a)
##word = '7'
##print('def_count >>> ', my_count(a, word))
##print('a.count >>> ', a.count(word))


def count_(a, s):
    len_ = len(s)
    i = 0
    k = 0
    while i < len(a):
        if a[i:i+len_] == s:
            k += 1
            i+=len_
        else:
            i+=1
    return k


##a = "yyaassa"
##simb = "y"
##print(a.count("y"))
##print(count_(a,simb))



def my_insert(index, elem, array):
    '''
    Вставляет на i-ый элемент значение x
    '''
    the_end = [elem]
    res = array[:index] + the_end + array[index:]

    return res


##a = [1, 45, 21, 87, 6, 0, 9]
##x = '4'
##print(my_insert(2, x, a))


def my_split(s, sep=' '):
    '''
    разбивает строку по указанному
    разделителю
    и возвращает список строк.
    '''
    a=[]
    if sep in s:
        list, index = [], 0
        while True:
            fnd = s.find(sep, index)
            if fnd == -1:
                list.append(s[index:])
                break
            list.append(s[index:fnd])
            index = fnd +1
    else:
        a.append(s)
        return a
    return list


##a = '1 23 2 4'
###a = 'Milk, Chicken, Bread, Butter'
##print(my_split(a))
##print(a.split())


def my_index(s, ch):
    '''
    Возвращает положение первого элемента
    со значением x
    (при этом поиск ведется
    от start до end)
    '''
    i=0
    while i<len(s)-1 and s[i]  != ch:
        i+=1
    if s[i]==ch:
        return i
    else:
        return 'элемента в списке нет'


##a = [1, 2, 5, 0, 56, 34, 1243, 9]
##print(my_index(a, 56))
##print(a.index(56))


def my_find(s, ch):
    '''
    Найти индекс первого совпадения
    подстроки в строке.
    Если символ или подстрока
    не найдены, find возвращает -1.
    '''
    if ch in s:
        i=0
        while i<len(s) and s[i]!=ch:
            i+=1
        return i
    else:
        return -1

#a = [1, 2, 5, 0, 56, 34, 1243, 9]
##a = 'welcome to my home'
##print(my_find(a, 'o'))
##print(a.find('o'))



def my_rfind(s, ch):
    '''
    Метод rfind() возвращает наивысший индекс
    подстроки (если найден).
    Если не найден, возвращается -1.
    '''
    if ch in s:
        i=len(s)-1
        while i>=0 and s[i]!=ch:
            i-=1
        return i
    else:
        return -1


##a = 'welcome to my home'
##print(my_rfind(a, 'o'))
##print(a.rfind('o'))



def my_replace(s, old, new):
    '''
    Метод replace() возвращает копию строки,
    в которой все вхождения подстроки
    заменяются другой подстрокой.
    '''
    i=0
    if len(old)>1:
        while old in s:
            if s[i:i+len(old)-1]==old:
                s=s[:i]+new+s[i+len(old):]
            i+=1
    else:
        while old in s:
            if s[i]==old:
                s[i]=new
    return s


##a = 'Del и del. Del или del'
##print(my_replace('del', a, 'space'))
##print(a.replace('del', 'space'))


def my_isdigit(s):
    '''
    Состоит ли строка
    из цифр
    '''
    i=0
    while i<len(s) and '0'<=s[i]<='9':
        i+=1
    return i==len(s)


##a = '125saaa3515'
##print(my_isdigit(a))
##print(a.isdigit())


def my_isalpha(s):
    '''
    Состоит  ли строка
    из букв
    '''
    i=0
    while i<len(s) and ('a'<=s[i]<='z' or 'A'<=s[i]<='Z'):
        i+=1
    return i==len(s)

##a = 'lol'
##print(my_isalpha(a))
##print(a.isalpha())


def my_isalnum(s):
    '''
    состоит ли строка
    из цифр или букв
    '''
    i=0
    while i<len(s) and ('a'<=s[i]<='z' or 'A'<=s[i]<='Z' or '0'<=s[i]<='9'):
        i+=1
    return i==len(s)

##a = '452sdafk'
##print(my_isalnum(a))
##print(a.isalnum())


def my_islower(s):
    '''
    состоит ли строка из символов
    в нижнем регистре
    '''
    i=0
    while i<len(s) and ('a'<=s[i]<='z' or '0'<=s[i]<='9'):
        i+=1
    return i==len(s)

##a = 'wsfagwSSAGDG'
##print(my_islower(a))
##print(a.islower())


def my_isupper(s):
    '''
    состоит ли строка из символов
    в верхнем регистре
    '''
    i=0
    while i<len(s) and 'A'<=s[i]<='Z':
        i+=1
    return i==len(s)

##a = 'SGAGQERGBWFGEWG'
##print(my_isupper(a))
##print(a.isupper())


def my_isspace(s):
    '''
    состоит ли строка из
    неотображаемых символов
    '''
    i=0
    while i<len(s) and s[i]==' ':
        i+=1
    return i==len(s)

##a = '  '
##print(my_isspace(a))
##print(a.isspace())


def my_istitle(s):
    '''
    начинаются ли слова в строке
    с заглавной буквы
    '''
    i=0
    flag=False
    while i<len(s):
        if (s[i]==' ' or i==0) and 'A'<=s[i+1]<='Z':
            flag=True
        else:
            flag=False
        i+=1
    return flag

##a = 'Ssgndsbh Dvdf'
##print(my_istitle(a))
##print(a.istitle())


def my_upper(s):
    '''
    преобразование строки к
    верхнему регистру
    '''
    a=''
    for elem in s:
        if 'a'<=elem<='z':
            a=a+chr(ord(elem)-32)
        else:
            a=a+elem
    return a

##a = 'welcome TTT EEE ho-ho-ho Epicai'
##print(my_upper(a))
##print(a.upper())


def my_lower(s):
    '''
    преобразование строки к
    нижнему регистру
    '''
    a=''
    for elem in s:
        if 'A'<=elem<='Z':
            a=a+chr(ord(elem)+32)
        else:
            a=a+elem
    return a

##a = 'SFDBGAS WAEGH ASFER $ sa'
##print(my_lower(a))
##print(a.lower())

            
def my_startswith(s, start):
    '''
    начинается ли строка S с
    шаблона str
    '''
    k=len(start)
    return s[:k]==start

##a = 'idy gulat'
##start = 'idy'
##print(my_startswith(a, start))
##print(a.startswith('idy'))


def my_endswith(s, end):
    '''
    заканчивается ли строка S
    шаблоном str
    '''
    k=len(end)
    return s[len(s)-k:]==end

##a = 'idy gulat'
##end = 'gulat'
##print(my_startswith(a, end))
##print(a.startswith('idy'))


def my_capitalize(s):
    '''
    Преобразование первого символа строки
    в верхний регистр, а всех
    остальных в нижний
    '''
    a=''
    if 'a'<=s[0]<='z':
        a=a+chr(ord(s[0])-32)
    i=1
    while i<len(s):
        if 'A'<=s[i]<='Z':
            a=a+chr(ord(s[i])+32)
        if ' ' == s[i]:
            a = a+chr(ord(s[i]))
        i+=1
    return a

##a = 'dDGW sSAHGSBS '
##print(my_capitalize(a))
##print(a.capitalize())


def my_lstrip(s):
    '''
    Удаление пробельных символов в
    начале строки
    '''
    i=0
    while i<len(s) and s[i]==' ':
        i+=1
    return s[i:]

##a = ' GErg ergq gergk'
##print(my_lstrip(a))
##print(a.lstrip())


def my_rstrip(s):
    '''
    Удаление пробельных символов в
    конце строки
    '''
    i=len(s)-1
    while i>0 and s[i]==' ':
        i-=1
    return s[:i+1]

##a = 'GRjnlkjb renljn  '
##print(my_rstrip(a))
##print(a.rstrip())


def my_strip(s):
    '''
    Удаление пробельных символов в начале
    и в конце строки
    '''
    i=0
    while i<len(s) and s[i]==' ':
        i+=1
    j=len(s)-1
    while j>0 and s[j]==' ':
        j-=1
    return s[i:j+1]

##a = ' GRjnlkjb renljn  '
##print(my_strip(a))
##print(a.strip())


def my_swapcase(s):
    '''
    Преобразование символов нижнего регистра
    в верхний,а верхнего в нижний
    '''
    a=''
    for elem in s:
        if 'a'<=elem<='z':
            a=a+chr(ord(elem)-32)
        else:
            a=a+chr(ord(elem)+32)
    return a

##a = 'Av;aABWsclv qgeqEAQGInvjdj'
##print(my_swapcase(a))
##print(a.swapcase())


def my_title(s):
    '''
    Преобразование первой буквы каждого символа
    в верхний регистр, а всех остальных в нижний
    '''
    a=''
    i=0
    while i<len(s):
        if (i==0 or s[i-1]==' ') and 'a'<=s[i]<='z':
            a=a+chr(ord(s[i])-32)
        elif 'A'<=s[i]<='Z':
            a=a+chr(ord(s[i])+32)
        else:
            a=a+s[i]
        i+=1
    return a

##a = 'dSGADASG AFfsdaf SFDAGGER'
##print(my_title(a))
##print(a.title())

































