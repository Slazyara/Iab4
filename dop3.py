json_text = 'schedule.json'
def parcing(data, space=0):

    yaml = ""

    if type(data) is list:
        for item in data:
            yaml += " " * space + "- " + str(item) + "\n"
    if type(data) is dict:
        for key, value in data.items():
            yaml += " " * space + str(key) + ":"
            if type(value) in (dict, list):
                yaml += "\n" + parcing(value, space + 2)
            else:
                yaml += " " + str(value) + "\n"
    else:
        yaml += " " * space + str(data) + "\n"

    return yaml

def read_json(json_text):
    import json
    with open(json_text, 'r', encoding='UTF-8') as file:
        yaml = json.load(file)
        yaml_text = parcing(yaml)
        return yaml_text


with open("schedule4.yaml", 'w', encoding='UTF-8') as outfile:
    outfile.write(read_json(json_text))
    print("Конвертация завершена. Результат сохранен в 'schedule4.yaml'.")