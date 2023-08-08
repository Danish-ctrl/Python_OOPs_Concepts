relative_list = ['Danish', 'Adil', 'Rashid']
relative_list.insert(0, 'Azeem')
relative_list.insert(2, 'Azad')
relative_list.append('Adi')
for i in range(0, len(relative_list)):
    if relative_list[i] == 'Adil':
        relative_list[i] = 'Ali'
        print(f"Hello {relative_list[i]}, I want to invite you for the dinner")
    else:
        print(f"Hello {relative_list[i]}, I want to invite you for the dinner")

print(f'I am removing {relative_list.pop(0)} from the list')
print("Adil can't make it to the dinner")
print(len(relative_list))
