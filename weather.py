def weather(t):
    if t in range(-50, 51):
        if t in range(-50, 0):
            return "It's super cold today. Be sure you dress well!"
        elif t in range(0, 11):
            return "It's windy outside, but we sure you will enjoy your day!"
        elif t in range(11, 31):
            return "It's time for outdoor walking!"
        elif t in range(31, 41):
            return "It's so hot outside!"
        elif t in range(41, 51):
            return "Welcome to hell!"
    else:
        return "Plaese re-check result in 5 mins"


try:
    with open("./inbox/input.txt", 'r', encoding='utf-8') as file:
        temp = file.read()
    temp = int(temp[0:-1])
    f = weather(temp)
    print(f)
except Exception:
    print("Plaese re-check result in 5 mins")


