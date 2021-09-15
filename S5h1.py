#parisa najari ghahremani thursday 14-18 class
#yek list mive az karbar begirad va mivehaye tekrari ra hazf namayad
#va tedad mivehaye monhaser be fard ra khoroji bedahad

fruits=input('please enter a fruts lists:\n').split()
print('fruits_list:',fruits)
fruits=set(fruits)
print('fruits_set:',fruits)
print('len:',len(fruits))



#barnameiy ke 2 ta list mive az migire va anhara jam mikone va
#tekrari haro hazf mikonad va tedad mivehaye monhaser be fard ra
#midahad
fruits1=input('please enter list fruit1:\n').split()
print('fruits1:',fruits1)
fruits2=input('please enter list fruit2:\n').split()
print('fruits2:',fruits2)
fruits1.extend(fruits2)
fruits1=set(fruits1)
print('sum fruits1:',fruits1)
print('len',len(fruits1))


#barnameiy ke yek list mive az karbar migirad va dar list
#peymayesh mikonad agar da list mive appel bod matn delkhah
#ra namayesh midahad
fruits1=input('please enter list fruit1:\n').split()
print('fruits1:',fruits1)
if 'apple' in fruits1:

    print('enjoy your meal')
else:
    print('eat an apple to stay healthy')
