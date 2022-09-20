# Chapter 7
***
## ex_7-1
```python
message = input("Hello! What car would you like to rent? \n")
print(f'Let me see if I can find you a {message}.')
```
```
Hello! What car would you like to rent? 
Passat
Let me see if I can find you a Passat.
```
***
## ex_7-2
```python
number = input("Hello! How many seats do you need a table for? \n")
number = int(number)
if number > 8:
    print(f"Sorry, you'll have to wait.")
else:
    print(f"Come on in, your table is ready!")
```
```
Hello! How many seats do you need a table for? 
5
Come on in, your table is ready!
```
***
## ex_7-3
```python
number = input("Введіть число, будь ласка: ")
number = int(number)
if number % 10 == 0:
    print(f"Число кратне 10.")
else:
    print(f"Число не кратне 10.")
```
```
Введіть число, будь ласка: 84
Число не кратне 10
```
***
## ex_7-4
```python
