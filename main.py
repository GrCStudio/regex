from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re


with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  raw_contacts_list = list(rows)
#pprint(raw_contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
row_count = 0
new_list = []
pattern_phone = re.compile(r"(\+7|8)?\s*\(*(495)\)*\s*[-]*(\d{3})[-]*(\d{2})[-]*(\d{2})\s*\(*(доб.)*\s*(\d{4})*")

for i in raw_contacts_list:
    inner_list = []
    lfs = i[0] + ' ' + i[1] + ' ' + i[2]
    lfs_new = lfs.split()
    if len(lfs_new) == 2:
        lfs_new.append('')
    lfs_new.append(i[3])
    lfs_new.append(i[4])
    clear_phone = pattern_phone.sub(r"+7(\2)\3-\4-\5 \6\7", i[5])
    lfs_new.append(clear_phone)
    lfs_new.append(i[6])
    inner_list.extend(lfs_new)
    new_list.append(inner_list)
    row_count += 1

#pprint(new_list)
contacts_list = []
contacts_list.append(new_list[0])
#pprint (contacts_list)
for i in range(1,len(new_list)):
    match_found = 0
    for el in range(2, len(new_list)):
        if el <= i:
            continue
        #print ('поиск совпадения для ', new_list[i][0])
        if new_list[i][0] == new_list[el][0] and new_list[i][1] == new_list[el][1]:
            match_found = 1
            print ("Совпадение найдено, ", new_list[el][0], ", обработка")
            for ch_el in range(2, len(new_list[el])):
                if new_list[el][ch_el] == "":
                    new_list[el][ch_el] = new_list[i][ch_el]

    if match_found == 0:
        contacts_list.append(new_list[i])
#pprint(contacts_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8', newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list)