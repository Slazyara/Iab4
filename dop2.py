import re

with open('schedule.json', encoding='utf-8') as f:
    json_array = [line.rstrip() for line in f.readlines()]

outfile = open("schedule2.yaml", 'w', encoding='utf-8')

for x in json_array:
    x=x.replace(" ",'',2)
    a = re.split(r':', x, maxsplit=1)

    if len(a) > 1:
        a[0] = re.sub(r'"', '', a[0])

        a[1] = re.sub(r'"', '', a[1])
        a[1] = re.sub(r'[,\{[\][]', '', a[1])
        outfile.write(a[0] + ':' + a[1] + "\n")

outfile.close()
print("Конвертация завершена. Результат сохранен в 'schedule2.yaml'.")


