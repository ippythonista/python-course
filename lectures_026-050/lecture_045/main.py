print(' DATA TYPE: LIST '.center(50, '='))

print('\n' + ' LIST (LIST) '.center(50, '~'))
empty_list1 = list()
empty_list2 = []
mix_list = [123, True, 'Paula', 3.14159, [2.71828]]

print(f'{empty_list1=} - {type(empty_list1)=}')
print(f'{empty_list2=} - {type(empty_list2)=}')
print(f'{mix_list=}')
print(f'{bool(empty_list1)=} - {bool(mix_list)=}')

print('\n' + ' INDEXING '.center(50, '~'))
print(mix_list[0], mix_list[-5])
print(mix_list[4], list[-1])
print()

print(f'{mix_list[2]=} - {type(mix_list[2])=}')
print()

mix_list[-3] = 'Paula Rodrigues'
print(f'{mix_list=}')

# IndexError
# print(f'{mix_list[-6]=}')
# print(f'{mix_list[5]=}')

print('\n' + ' CRUD '.center(50, '~'))
print('\n' + ' CREATE '.center(50, '-'))
array = [10, 20, 40]
print(f'{array=}')

print('\n' + ' READ '.center(50, '-'))
print(f'{array=}')

print('\n' + ' UPDATE '.center(50, '-'))
array[-1] = 30
print(f'{array=}')

print('\n' + ' DELETE '.center(50, '-'))
del array[1]
print(f'{array=}')

print('\n' + ' METHODS '.center(50, '~'))
array = []
print(f'{array=}')

print('\n' + ' APPEND '.center(50, '-'))
array.append(1)
array.append(2)
array.append(3)
array.append(4)
print(f'{array=}')

print('\n' + ' POP '.center(50, '-'))
print(f'{array.pop()=} {array=}')
print(f'{array.pop(0)=} {array=}')

print('\n' + ' INSERT '.center(50, '-'))
array.insert(0, 'x')
array.insert(10, 'y')

print(f'{array=}')

print('\n' + ' CLEAR '.center(50, '-'))
array.clear()
print(f'{array=}')

print('\n' + ' EXTEND '.center(50, '-'))
array.extend([1, 2, 3, 4, 5, 6])
print(f'{array=}')

print('\n' + ' CONCATENATION '.center(50, '~'))
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
list4 = list2 + list1

print(f'{list3=}')
print(f'{list4=}')

print('\n' + ' MUTABILITY '.center(50, '~'))
list1 = [1, 2, 3]
list2 = list1
list3 = list1.copy()

list1[0] = 0
print(f'{list1=}')
print(f'{list2=}')
print(f'{list3=}')

print('\n' + ' FOR '.center(50, '~'))
names = ['Mirilaine', 'Charles', 'Fernanda', 'Paula', 'Wagner']
for name in names:
    print(name)
