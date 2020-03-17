import webbrowser
address = input("type your address here: ")
address = address.split()

j = 1
name = ""

for i in address:
    if j == 1:
        name = i
    else:
        name = name + f"+{i}"
    j += 1

webbrowser.open(f'http://google.com/maps/place/{name}')
