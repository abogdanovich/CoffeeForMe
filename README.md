## CoffeeForMe
**CoffeeForMe is an interactive command-line tool to make your life better every day :)**

Разработать command line утилиту на Python, которая будет использоваться продавцами, мэнэджерами сети кофеин CoffeeForMe.
 
**Скрипт должен иметь возможность:**
1. Принимать следующие входные параметры:

- Имя пользователя
- Должность: продавец или мэнэджер
- Напиток – доступен только если должность продавец	
- Дополнительные ингредиенты для напитка: сахар, сливки, корица – доступен только если должность продавец
- Получить цену - доступен только если должность продавец
- Сохранить продажу - доступен только если должность продавец

2. Сохранять результаты продаж для каждого продавца
3. Предоставлять суммарные результаты продаж в виде таблицы при условии, что программу запускает мэнэджер:

(http://pix.toile-libre.org/upload/original/1523015167.jpg)
	
4. Возможность интерактивного ввода данных
5. Предоставлять возможность получать стоимость напитка продавцу
6. Предоставлять возможность сохранять проданную позицию продавцу
7. Отлавливать исключения при условии ввода неверных значений в качестве аргументов скрипту

**Приветствуется:**
1. Использование ООП
2. Использование паттернов проектирования
3. Работает с Python2.7, Python 3.6
4. Сохраняет результаты с базу данных
5. Программа ведет лог событий

**Tech stack**
```
- sqlite db 
- python 2.7 
- pytest 
- virtualenv
- bash scripting
```

**Checklist**
```
[x] param - name - checking (english alphabet only, exclude any numbers and system symbols)
[x] member checking: (barman, manager)
[x] manager: profit table reviews
[x] barman: drink options 
[x] barman: drink price 
[x] barman: save order functions
[x] barman: drink tips for common bank
[x] barman: daily tips \ check \ calc: total / number of barmans
[x] general: operations logging
[x] general: db testing \ table-insert-update-delete-close
[x] general: exception catch: no db \ wrong params \ etc....  
[x] ...
[x] ...
[x] ...
```