# Chapter 2
 ***
## ex_2-1

```
message = "Hello Python world!"
print(message)
```
```
PS D:\python-crash-course-2022> python chapter_2/ex_2-1.py
Hello Python world!
```
***
## ex_2-2
```
message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)
```
```
PS D:\python-crash-course-2022> python chapter_2/ex_2-1.py
Hello Python world!
Hello Python Crash Course world!
```
***


***.title()*** - функція(?), яка робить першу букву великою, а інші малими

***.upper()*** - виводить весь текст великими буквами

***.lower()*** - виводить весь текст малими буквами

```
name = "AdA lOvELacE"
print(name.title())
print(name.upper())
print(name.lower())
```
```
PS D:\python-crash-course-2022> python chapter_2/name.py
Ada Lovelace
ADA LOVELACE
ada lovelace
```
***
```
first_name = "ada"
last_name = "lovelace"
full_name  = first_name + " " + last_name
print('Hello, ' + full_name.title() + '!')
```

```
PS D:\python-crash-course-2022> python chapter_2/name.py
Hello, Ada Lovelace!
```
***
***\n*** - новий абзац;

***\t*** - ставиться типу Tab, пропуск
```
print("Languages:\n\tPython\n\tC\n\tJavaScript")
```

```
Languages:
        Python
        C
        JavaScript
```
***
***.rstrip()*** - видаляє пропуски з правого краю

***.lstrip()*** - видаляє пропуск з лівого краю

***.strip()*** - видаляє пропуски з обох сторін
```
favorite_language = ' python '
print(favorite_language.rstrip() + '!')
print(favorite_language.lstrip() + '!')
print(favorite_language.strip() + '!')
```

```
PS D:\python-crash-course-2022> python chapter_2/whitespace.py
 python!
python !
python!
```
***

## ex_2-3

```
name = 'Діма'
print('Привіт, '+name.title() + ', дивись, я роблю домашку!!') 
```

```
PS D:\python-crash-course-2022> python chapter_2/ex_2-3.py
Привіт, Діма, дивись, я роблю домашку!!
```

## ex_2-4

```
name = 'mariia valeriivna popach'
print(name.lower())
print(name.upper())
print(name.title())
```

```
PS D:\python-crash-course-2022> python chapter_2/ex_2-4.py
mariia valeriivna popach
MARIIA VALERIIVNA POPACH
Mariia Valeriivna Popach
```
***
## ex_2-5
```
name = 'тарас шевченко'
quote = 'Борітеся – поборете! Вам Бог помагає! За вас правда, за вас слава! І воля святая!'
print(name.title() + ' колись казав, "' + quote + '"')
```

```
PS D:\python-crash-course-2022> python chapter_2/ex_2-5.py
Тарас Шевченко колись казав, "Борітеся – поборете! Вам Бог помагає! За вас правда, за вас слава! І воля святая!"
```

***
## ex_2-6
```
first_name = 'тарас'
last_name = 'шевченко'
full_name = first_name + ' ' + last_name
message_1 = 'Борітеся – поборете!'
message_2 = 'Вам Бог помагає!'
message_3 = 'За вас правда, за вас слава'
message_4 = 'І воля святая!'
print(full_name.title() + ' колись казав, "' + message_1 + '\n' + message_2 + '\n' + message_3 + '\n' + message_4 + '"')
```

```
PS D:\python-crash-course-2022> python chapter_2/ex_2-6.py
Тарас Шевченко колись казав, "Борітеся – поборете!
Вам Бог помагає!
За вас правда, за вас слава
І воля святая!"
```
***
## ex_2-7
знак "!" тут для розуміння кількості пропусків
```
name = '\n\t\t\tmariia\t\t\t'
print(name.title()+ '!')
print(name.title().rstrip() + '!')
print(name.title().lstrip() + '!')
print(name.title().strip() + '!')
```

```
PS D:\python-crash-course-2022> python chapter_2/ex_2-7.py

                        Mariia                  !

                        Mariia!
Mariia                  !
Mariia!
~~~