my_list = [4, 1, 15, 54, 3, 7, 16, 11, 20, 5]
new_list = [el for num, el in enumerate(my_list) if my_list[num-1] < my_list[num]]
print(f'Начальный список : {my_list}')
print(f'Новый список: {new_list}')