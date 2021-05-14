def translate(param1, param2):
    text1 = text.replace(param1, param2)
    return text1


def include(param1):
    if param1 in text:
        return True
    else:
        return False


def start_with(param1):
    return text.startswith(param1)

def find_last_index(string, x):
    for i in range(0, len(string)):
        if string[i] == x:
            index = i
    return index


def remove(start, stop):
    return text[0: start] + text[stop:]


text = input()

cmd = input()

while not cmd == "End":
    cmd = cmd.split()
    if cmd[0] == "Translate":
        text = translate(cmd[1], cmd[2])
        print(text)
    elif cmd[0] == "Includes":
        print(include(cmd[1]))
    elif cmd[0] == "Start":
        print(start_with(cmd[1]))
    elif cmd[0] == "Lowercase":
        text = text.lower()
        print(text)
    elif cmd[0] == "FindIndex":
        print(find_last_index(text, cmd[1]))
    elif cmd[0] == "Remove":
        print(remove(int(cmd[1]), int(cmd[1])+int(cmd[2])))

    cmd = input()