import json
import re


urlin = input("Введите путь до файла: ")



def json_report(urlin):
    
    #если путь берут из ос Windows, то надо заменить все слеши \ на /
    urlin = re.sub(r'\\', '/', urlin)
    urlout = re.search(r'(.+)(/.+$)', urlin) #выбираем из пути к файлу путь до папки, где содержится файл
    urlout = urlout.group(1)

    # открываем файл, получаем строку, преобразовываем в json 
    with open(urlin, 'r') as file:
        json_file = json.loads(file.read())
        
    list = []
    for i in json_file["site"][0]["alerts"]:
        list.append({"name": i["name"], "count": i["count"]})


    slovar = { 
                "vulnerabilities": list
            }

    slovar = json.dumps(slovar, indent=4) #Преобразуем наш словарь в json
    urlout = urlout + "/Report.json"
    with open(urlout, 'w') as file:
        file.write(slovar)
        
    return 0
    
json_report(urlin)