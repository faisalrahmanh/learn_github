# z='X'
# for baris in range(5):
#     print (z);
#     z += 'X'

# z='';
# for item in range(5):
#    for item1 in range(item-1,4):
#       z += ' X ';

# z='';
# for item in range(5):
#    for item1 in range(item-1,4):
#       z += ' X ';
#    z += '\n';
# print(z)

# z='X'
# for baris in range(5):
#     print (z);
#     z += 'X'
# for kolom in range(4):
#      for baris in range(4-kolom):
#           print ("X",end="");
          
#      print()   


# z = " * " * 5;
# for item in range(5):
#    print(z)   

# z = "";
# for item in range(5, 0, -1):
#    print(z * item)
#    z += " X " 

# z= '';
# for x in range(5, 0, -1):
#    for y in range(0, x):
#       z += ' * '
#    if x != 1:
#       z += '\n'
# print(z)            


# z = " * ";
# x = "   "
# y = " * "
# for item in range(5,0,-1):
#    print(item, x * item + z )
#    z += " *  * "
# for item1 in range(6):
#    print(item1, x + y )
#    x += "   "

# z = ' * '
# y = '   '
# for item in range(10):
#     if item < 5:
#         bintang = 2*item
#         spasi = 5 - item
#         print(item, y * spasi + z * bintang + z)
#     else :
#         bintang = 20-(2*item)-1
#         spasi = item - 4
#         print(item, y * spasi + z * bintang)   
   


# x = [40, 100, 1, 5, 25, 10]
# x_sort = []

# def fungsi() :

#     idx_min = 0
#     lowest_guess = x[idx_min] 
    
#     for idx in range(len(x)):
#         if x[idx] < lowest_guess:
#             lowest_guess = x[idx]
#             idx_min = idx

#     x_sort.append(lowest_guess)
#     x.pop(idx_min)
#     print(x_sort)

# for i in range(6):
#     fungsi()

# x.sort()
# x.sort(reverse = True)
# print(x)

# def iterasi(x,index,iter,stop=5):
#     while iter <= stop:
#         if x[index] > x[iter]:
#             temp = x[index];
#             x[index] = x[iter];
#             x[iter] = temp;
#         iter = iter + 1
#     return x


# x = [40, 100, 1, 5, 25, 10];
# index = 0;
# iter = 0;
# for item in range (5):
#     iterasi(x,index,iter);
#     index += 1;
#     iter += 1;
# print(x)



# data_list = [40, 100, 1, 5, 25, 10]
# new_list = []

# while data_list:
#     minimum = data_list[0]  # arbitrary number in list 
#     for x in data_list: 
#         if x < minimum:
#             minimum = x
#     new_list.append(minimum)
#     data_list.remove(minimum)    

# print(new_list)

# listNum = [ 1, 2, 3, 4, 5];
# listNum = [item * 2 for item in listNum];
# print(listNum);

# values = [2000, 3000, 4000, 7000, 8000]
# values1 =list(map(lambda item : item * 2, values))
# print(values1)

# players = ['ronaldo', 'messi', 'figo', 'mbape']
# player = input('series a player:')
# print(list(filter(lambda x : player in x  , players)))

# def func(var) :
#     if var == True :
#         return('abcdefg')    
#     return('XXXXX')    

# presents = [True, False, True, True, False]
# for item in presents:
#     print(list(func(item)))

# def fizzBuzz(num) :
#     for i in range(1,num+1) :
#         if (i % 2 == 0 and i % 7 == 0) :
#            print('FizzBuzz')
#         elif (i % 2 == 0) :
#            print('Fizz')
#         elif (i % 7 == 0) :
#            print('Buzz')
#         else :
#            print('No FizzBuzz');
# fizzBuzz(20);

# def fibo(urut) :
#     listData = [1,1,2];
#     for i in range(2,urut):
#         listData.append(listData[i-2] + listData[i-1]);
#     print(listData)    
#     return listData[urut-1];

# print(fibo(8));

import math;
def reverseList(theList) :
    for i in range(0, math.floor(len(theList)/2)) :
        tempList = theList[i];
        idx = len(theList) - 1 - i
        theList[i] = theList[idx];
        theList[idx] = tempList;
        
    return theList;
print(reverseList([1,2,3,4,5,6,7,8]));






