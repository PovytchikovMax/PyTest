# my_list = ['a', 'b', [1, 2, 3], 'd']
# for i in (my_list[2]):
#     print(i)

# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# sum1 = 0
# for i in list_1:
#     if type(i) == int:
#         sum1 = sum1 + i
# print(sum1)

# cort = ['cat', 'dpg', 'horse', 'cow']
# print(type(tuple(cort)))
# print(tuple(cort))

# family_1 = ['father', 'grandmother']
# family_2 = ['father', 'sun', 'grandmother']
#
# family_1 = input("Введите данные первой семьи").split(',')
# family_2 = input("Введите данные второй семьи").split(',')
# # print(len(family_1))
# if len(family_1) > len(family_2):
#     print("Family one is biggest")
# elif len(family_1) < len(family_2):
#     print("Family two is biggest")
# else:
#     print("Equal")
#
# film = {
#     "title": 'Jon Uik',
#     "director": 'JMax',
#     "year": '2020',
#     "budget": 'budget ',
#     "main_actor": 'kianu rives ',
#     "slogan": 'Y are not have kill me',
# }
#
# print(film.keys())
# print(film.values())
# print(film.items())
# from functools import reduce
#
# my_dictionary = {
#     'num': 1,
#     'num1': -1,
#     'num2': 1,
#     'num3': 1,
#     'num4': 1,
#     'num5': 1,
#     'num6': -1,
#
# }
# print(reduce((lambda x, y: x + y), my_dictionary.values()))
# dict = [1, 2, 3, 1, 3, 3, 5, 4, 1]
# print(set(dict))
# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, '100', 'b'}
#
# print(set1.union(set2))
# print(set1.difference(set2))
# print(set1.issubset(set2))
# print(set1.isdisjoint(set2))
# print(set1.discard(set2))
# print(set1.intersection(set2))
