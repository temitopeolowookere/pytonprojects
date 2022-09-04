# cont = []
#
# # for i in range(1,11):
# #     cont.append(i)
# #
# # cont = [num for num in range(1,11)]
# #
# # print(cont)

# squares = []
#
# # for i in range(1,11):
# #     squares.append(i **2)
# squares = [num **2 for num in range(1,11)]
# print(squares)

# names = ['bimpe', ' Banke', 'abimbola', 'james', 'Olalekan', 'Racheal']
# my_names = [name for name in names if name.istitle()]
# number_of_times = int(input("how many names will you like to enter"))
# input_names = [input(f"{i+1}.name?") for i in range(number_of_times)]
# my_names = []
# for name in names:
#     if name.istitle():
#         my_names.append(name)
# print(my_names)

cont = []
cont = [num for num in range(1,11)]

even = [even for even in range(1,11) if even %2 ==0]
even_squared_odd_cubed = [num ** 2 if num % 2 == 0 else num ** 3 for num in range(1,11)]
print(even_squared_odd_cubed)



print(even)

print(cont)


