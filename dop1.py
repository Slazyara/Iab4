import json
import yaml
def convert_json_to_yaml(json_file, yaml_file):
    with open("schedule.json", 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    with open("schedule1dop.yaml", 'w', encoding='utf-8') as f:
        yaml.dump(json_data, f, allow_unicode=True)
json_file = 'schedule.json'
yaml_file = 'schedule1dop.yaml'
convert_json_to_yaml(json_file, yaml_file)
print(f'Конвертация завершена: {json_file} -> {yaml_file}')