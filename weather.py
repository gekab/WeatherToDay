import modules.modul as m

try:
    with open("./inbox/input.txt", 'r', encoding='utf-8') as file:
        temp = file.read()
    temp = int(temp[0:-1])
    f = m.weather(temp)
    print(f)
except Exception:
    print("Plaese re-check result in 5 mins")


