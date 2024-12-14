with open('schedule.json', encoding='utf-8') as f:
    json_array = [line.rstrip() for line in f.readlines()]

#yaml_rez = open('scedule1.yaml')

outfile = open("schedule1.yaml", 'w', encoding='utf-8')

for x in json_array:
    a=x.split(":")
    if len(a)>1:
        a[0]=a[0].replace('"','')
        a[1]=a[1].replace('"','')
        #print(a[1][-1])
        if a[1][-1]==',' or a[1][-1]=='{' or a[1][-1]=='[':
            a[1]=a[1][:-1]
        outfile.write(a[0]+':'+a[1]+"\n")
print("Конвертация завершена. Результат сохранен в 'scedule1.yaml'.")
