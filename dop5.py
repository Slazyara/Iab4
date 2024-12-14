import json

with open('schedule.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

with open('timetable.csv', 'w', encoding='utf-8') as f:
    f.write('День;Пара;Предмет;Время;Недели;Преподаватель;Здание;Кабинет;Формат\n')
    for day_name, day_data in data['timetable'].items():
        for order, lesson in day_data['lessons'].items():
            f.write(
                f"{day_name};{order};{lesson['subject']};{lesson['time']};{lesson['weeks']};{lesson['teacher']};{lesson['building']};{lesson['room']};{lesson['format']}\n")

print("Конвертация завершена. Результат сохранен в 'timetable.csv'.")
