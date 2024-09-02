min_lista = ['a','b','c']
#             0   1   2
print(min_lista[0])
print(min_lista[1])
print(min_lista.remove('b'))
# print(min_lista[2])
mitt_popade_värde = min_lista.pop(1)
print(mitt_popade_värde)
print(min_lista)


min_super_lista = [[1,2,3], [4,5,6]]
print(min_super_lista[0])
min_super_lista.append([7,8,9])
# [[1,2,3], [4,5,6], [7,8,9]]
print(min_super_lista)
min_super_lista[0].append('Hejsan!')
# [[1,2,3,'Hejsan!'], [4,5,6], [7,8,9]]
print(min_super_lista)
print(min_super_lista[0][0])
print(min_super_lista[1][0])
print(min_super_lista[2][0])

hej = min_super_lista[0][3][0:3]

print(f'{hej=}')

