# С помощью какой библиотеки в Python 3 можно работать с JSON файлами?
#с помощью библиотеки json
# Импортируйте необходимые библиотеки

# import 
import json
# pprint позволяет в понятном для человека виде форматировать 'сложные' структуры данных 
from pprint import pprint 

filename = 'data.json'

try:

    with open(filename, encoding='utf-8') as data_file:
        
        data = json.load (data_file)

except ErrorFileNotFound:

    print("Файл не найден! Файл должен называться: {}".format(filename))
    
    status = 'Файл не найден'


pprint(data)

# Вывести в форматированном виде поля: 

# company, email, phone, address
for tmp in data:
	print("company: {}".format(tmp["company"]))
	print("email: {}".format(tmp["email"]))
	print("phone: {}".format(tmp["phone"]))
	print("address: {}".format(tmp["address"]))