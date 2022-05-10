import re
from subprocess import run, PIPE
import datetime

process_info = run(["ps", "aux"], stderr=PIPE, stdout=PIPE).stdout.decode("utf-8")
process_info_string = process_info.split("\n")
del process_info_string[0]
del process_info_string[-1]

formatted_users = ''
data = {"USERS": {},
        "%MEM": 0,
        "%CPU": 0,
        "MAX_MEM": [],
        "MAX_CPU": [],
        "PROCESS_COUNTER": len(process_info_string)}

for string in process_info_string:
    data_string = re.sub(r"\s+", " ", string).split(" ")
    user = data_string[0]
    memory = float(data_string[3])
    cpu = float(data_string[2])
    process = " ".join(data_string[10:])

    if user not in data['USERS']:
        data['USERS'][user] = 0

    data["USERS"][user] += 1
    data["%MEM"] += memory
    data["%CPU"] += cpu

    if not data["MAX_MEM"]:
        data["MAX_MEM"] = (memory, process)
    if memory > data["MAX_MEM"][0]:
        data["MAX_MEM"] = (memory, process)

    if not data["MAX_CPU"]:
        data["MAX_CPU"] = (cpu, process)
    if cpu > data["MAX_CPU"][0]:
        data["MAX_CPU"] = (cpu, process)

users_list = list(data['USERS'].items())
users = sorted(users_list, key=lambda i: i[1], reverse=True)
for j in users:
    formatted_users += '\n{}: {}'.format(j[0], j[1])

system_info = (f'Отчёт о состоянии системы:'
          f'\nПользователи системы: {", ".join(data["USERS"])}'
          f'\nПроцессов запущено: {data["PROCESS_COUNTER"]}'
          f'\nПользовательских процессов: {formatted_users}' 
          f'\nВсего памяти используется: {data["%MEM"]:.1f}%'
          f'\nВсего CPU используется: {data["%CPU"]:.1f}%'
          f'\nБольше всего памяти использует:  {data["MAX_MEM"][0]:.1f}% - {data["MAX_MEM"][1][:20]}'
          f'\nБольше всего CPU использует: {data["MAX_CPU"][0]:.1f}% - {data["MAX_CPU"][1][:20]}')

print(system_info)

file_name = datetime.datetime.now().strftime("%d-%m-%Y-%H:%M") + "-scan.txt"
with open(f'{file_name}', "w", encoding='UTF-8') as f:
    f.write(system_info)


