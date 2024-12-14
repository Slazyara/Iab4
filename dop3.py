import json

ww = '{}'
# a = 0
# c = 0
json_text = 'schedule.json'


def parcer(data, h, space=0):
    yaml = ""
    if type(data) is dict:
        for key, value in data.items():
            if key == h:
                yaml += " " * (space-2) + "- " + str(key) + ":"
            else:
                yaml += " " * space + str(key) + ":"
            if type(value) in (dict, list):
                yaml += "\n" + parcer(value, h, space + 2)
            else:
                yaml += " " + str(value) + "\n"
    elif type(data) is list:
        for item in data:
            if type(item) in (list, dict):
                c = next(iter(data[0]))
                print(c)
                yaml += parcer(item, c, space + 2)
    else:
        yaml += " " * space + str(data) + "\n"

    return yaml


def parser_array(data, space, a, yaml):
    for item in data:
        if type(item) in (list, dict):
            print(next(iter(data[0])))
            if item == data[0]:
                yaml += " " * (space - 2) + '-' + str(data) + "\n"
            else:
                yaml += parcer(item, space + 2)


def read_json(json_text):
    with open(json_text, 'r', encoding='UTF-8') as file:
        yaml = json.load(file)
        yaml_text = parcer(yaml, ww)
        return yaml_text


with open("schedule4.yaml", 'w', encoding='UTF-8') as outfile:
    outfile.write(read_json(json_text))
    print("Конвертация завершена. Результат сохранен в 'schedule4.yaml'.")