def capitalize_string(name):
    name = name.casefold()
    name = name.capitalize()
    result = name[0]
    list = []
    for j in name:
        list.append(j)
    for i in range(1,len(list)):
        if list[i-1] == " ":
            list[i] = list[i].upper()
        result += list[i]
    return result

print(capitalize_string("joao vITor netTo"))