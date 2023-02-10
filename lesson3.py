#Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
#В результирующем списке не должно быть дубликатов.

double_list=[1,2,3,4,5,6,7,8,9,3,4,5,6]
eggs_list=[]
new_list=[]
for i in double_list:
    if i not in eggs_list:
        eggs_list.append(i)
    else:
        new_list.append(i)
print(f'{double_list = }')
print(f'{new_list = }')

#В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
#Не учитывать знаки препинания и регистр символов. 
#За основу возьмите любую статью из википедии или из документации к языку.

words_list=input('inter text: ').split()
my_dictionary={}
for i in words_list:
    my_dictionary.setdefault(words_list.count(i),i)
sort_list=(sorted(my_dictionary.items())[::-1])
for i in sort_list[:9:]:
    print(f'word:"{i[1]}" count: {i[0]}')

#Cоздайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
#Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
#Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

equipment = dict(tent = 3,axe = 2,bowler_hat = 1, cloth = 4,food = 5)
MAX_WEIGHT = 8
weight=0
eggs={v: k for k, v in equipment.items()}
sort_equipment = (sorted(eggs.items())[::-1])
list1=[]
len_eq=len(sort_equipment)
while len_eq>0:
    for i in sort_equipment:
        if weight+i[0]>MAX_WEIGHT:
            continue
        else:
            list1.append(i)
            weight+=i[0]
    for i in list1:
        print(i[1])
    print('*'*25)
    if len(list1)==0:
        break
    sort_equipment.pop(0)
    weight=0
    list1.clear()
#Решение представляет несколько вариантов комплектации рюкзака,но не все. На все не хватило мозгов=)







        

    
