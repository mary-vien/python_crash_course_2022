# Chapter 1
 
## Ex 1-1

Simple **text**

Another *paragraph*

```
git push origin master

print('hello, world")
```

~~~
git push origin master

print('hello, world")
~~~

![cat.jpg](screenshots/cat.jpg)

[Погода в Києві на 10 днів](https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D1%97%D0%B2/10-%D0%B4%D0%BD%D1%96%D0%B2/)


## EX 1-1
***Визначення де ти знаходишся***
```
PS D:\python-crash-course-2022> dir 


    Directory: D:\python-crash-course-2022


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        16.08.2022     22:37                chapter_1
-a----        16.08.2022     22:30             23 .gitignoredir

```

***Після того як бачиш в якій папці, вводиш python назва папки/назва файлу.py***
```
PS D:\python-crash-course-2022> python chapter_1/hello.py
hello, world
```
## EX 1-2
```
print (''hello, world'')
```

```
File "D:\python-crash-course-2022\chapter_1\hello.py", line 1
    print (''hello, world'')
             ^
SyntaxError: invalid syntax
```

## EX 1-3
я б хотіла зробити програму, яка збирає всі паспортні дані на прикордонних пунктах (ПІБ, дата народження, громадянство, термін дії т.д.). після того, як програма відскановує паспорт русні, то з гучномовця починає грати пісня "Доброго вечора, ми з України", а термін дії паспорту русні автоматично закінчується. як результат - русня без паспорта - під варту - і назад в болото гнити)