x = [ 1,2,3,2,5,2,7,2 ]
def getMean(list) :
    sum = 0;
    for item in list :
        sum += item;

    mean = sum / len(list);
    return mean;
print(getMean(x));
# Setelah dapat mean, masukan ke dalam rumus lambda
newlist = list(map(lambda num: num-3,x));
print(newlist);
newlist2 = list(map(lambda num1: num1**2,newlist));
print(newlist2)
# Untuk mencari jumlah angka-angka di dalam list yang baru
sum1 = 0
for num3 in newlist2:
    sum1 += num3;
print(sum1)    
# Untuk mengetahui berapa jumlah item di dalam list
print(len(newlist2))
# Rumus variance
variance = sum1/(len(newlist2)-1)
print(variance)
# Rumus standar deviasi
std = variance**0.5
print(std)
