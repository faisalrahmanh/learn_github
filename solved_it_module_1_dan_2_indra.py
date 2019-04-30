##################### module_1 ############################

# # #solved_it_1
# nama = input("Nama kamu? : ");
# umur = input("Umur kamu? : ");
# kelamin = input("Kelamin kamu? : ");
# pekerjaan = input("Pekerjaan kamu? : ");

# print("Nama : " + nama);
# print("Umur : " + umur);
# print("Kelamin : " + kelamin);
# print("Pekerjaan : " + pekerjaan);

# # #solved_it_2
# import math
# x = 4;
# y = 3;
# z = 2;

# numerator = x+(y*z);
# denominator = x*y;
# w = (numerator/denominator)**2;

# print(w);

#solved_it_3
# number = int(input("Silahkan masukkan angka berapapun : "));
# print("Kuadrat dari " + str(number) + " adalah " + str(number**2));

# #solved_it_4
# import math

# awal_hari = 485;
# total_tahun = math.floor(awal_hari/360);
# sisa_hari = awal_hari - total_tahun * 360;
# total_bulan = math.floor(sisa_hari/30);
# sisa_hari -= total_bulan * 30;
# total_minggu = math.floor(sisa_hari/7);
# sisa_hari -= total_minggu * 7;
# print(str(awal_hari) + " hari sama dengan " 
#                      + str(total_tahun) + " tahun " 
#                      + str(total_bulan) + " bulan "
#                      + str(total_minggu) + " minggu " 
#                      + str(sisa_hari) + " hari.");

#solved_it_5

# """
#     jumlah_usia = 49
#     rasio_usia = 0.4
#     a + b = 49
#     a/b = 0.4
#     a = 0.4b
#     0.4b + b = 49
#     1.4b = 49
# """

# b = int(49/1.4);
# a = int(49 - b);
# print("Dua tahun lagi, usia Andi " + str(a+2) 
#                                    + " dan usia Budi " 
#                                    + str(b+2) 
#                                    + ".")

# # #solved_it_6
# x = "Halo Dunia";
# y = 'z';
# jumlah_char = len(x.split(y))-1;
# print("Jumlah karakter " + y 
#                          + " adalah " 
#                          + str(jumlah_char) 
#                          + " huruf.");

# x = "Halo Dunia"
# print(x.count('a'))

# # solved_it_7
# # s_a = 120 - x
# # s_b = x
# # v_a = 60
# # v_b = 40

# # t_a = t_b
# # s_a / v_a = s_b / v_b
# # (120 - x) / 60 = x / 40
# # (120 - x) / 3 = x / 2
# # 240 - 2x = 3x
# # 240 = 5x
# # x = 48

# # t_a = s_a / v_a
# import math
# jam_awal = 9
# t_a = (120 - 48) / 60;
# jam_akhir = jam_awal + math.floor(t_a)
# sisa_menit = math.ceil((t_a - math.floor(t_a)) * 60)
# print("A & B bertemu pada jam " + str(jam_akhir) + ":" + str(sisa_menit) + ".")




##################### module_2 ############################

# # solved_it_1
# number = int(input("Masukkan angka : "));
# if number%2 == 0:
#     print("Angka " + str(number) + " tergolong bilangan GENAP!");
# else:
#     print("Angka " + str(number) + " tergolong bilangan GANJIL!");

# solved_it_2
# import math
# massa = int(input("Masukkan Massa(kg) : "));
# tinggi = float(input("Masukkan Tinggi(cm) : "))/100;
# print("Massa " + str(massa) + " kg & tinggi " + str(tinggi) + " m");
# imt = massa/math.pow(tinggi,2);
# if imt < 18.5:
#     arti = "berat badan kurang!";
# elif (imt >= 18.5) & (imt <= 24.9):
#     arti = "berat badan ideal!";
# elif (imt >= 25.0) & (imt <= 29.9):
#     arti = "bb berlebih!";
# elif (imt >= 30.0) & (imt <= 39.9):
#     arti = "bb sangat berlebih!";
# elif imt > 39.9:
#     arti = "bb sangat berlebih!";

# print("IMT = " + str(imt) + ", " + arti.upper());





##################### module_3 ############################

# # solved_it_1
# num = 5
# z = ' * ' * num
# while z != '':
#     print(z)
#     num -= 1
#     z = ' * ' * num

# solved_it_2
# num = 5
# z = ' * ' * num
# limit = ' * '
# while z != limit:
#     if limit == ' * ':
#         print(z)
#         num -= 1
#         z = ' * ' * num
#     else:
#         print(z)
#         num += 1
#         z = ' * ' * num
#     if z == ' * ':
#         limit = ' * ' * 6

# # solved_it_3
# num = 1
# space = 11
# z = ' * ' * num
# limit = ' * ' * 20
# while z < limit:
#     if num % 2 == 1:
#         space -= 1
#         z = '   ' * (space) + ' * ' * num
#         print(z)
#     num += 1
    
# # solved_it_4
# num = 19
# space = 0
# z = ' * ' * num
# limit = len(z.split('*'))-1
# while limit > 1:
#     if num % 2 == 1:
#         z = '   ' * (space) + ' * ' * num
#         space += 1
#         print(z)
#     num -= 1
#     limit = len(z.split('*'))-1

# solved_it_3
space = 5
num = 0
limit = 0
end = 9
while limit != end:

    if end == 9:
        num += 1
        if num % 2 == 1:
            space -= 1
            z = '   ' * space + ' * ' * num
            print(z)
            limit = len(z.split('*'))-1
    else:
        num -= 1
        if num % 2 == 1:
            space += 1
            z = '   ' * space + ' * ' * num
            print(z)
            limit = len(z.split('*'))-1

    if limit == 9:
        print(z)
        num -= 1
        end = 1

##################### module_4 ############################

# # solved_it_1
# def sort_ascending(x):

#     val = []
#     for i in x:
#         val.append(i)

#     res = []
#     min_idx = 0
#     min_val = val[min_idx]

#     while len(res) < 6:
#         for i in range(0,len(val)):
#             if val[i] < min_val:
#                 min_idx = i
#                 min_val = val[i] 
        
#         res.append(min_val)
#         val[min_idx] = 1000
#         min_val = 1000

#     return res

# x = [40,100,1,5,25,10]
# sort_asc = sort_ascending(x)
# print(sort_asc)

# # solved_it_1
# def sort_descending(x):

#     val = []
#     for i in x:
#         val.append(i)

#     res = []
#     max_idx = 0
#     max_val = val[max_idx]
    
#     while len(res) < 6:
#         for i in range(0,len(val)):
#             if val[i] > max_val:
#                 max_idx = i
#                 max_val = val[i] 
        
#         res.append(max_val)
#         val[max_idx] = -1
#         max_val = -1

#     return res

# x = [40,100,1,5,25,10]
# sort_descending = sort_descending(x)
# print(sort_descending)
# print(sort_descending[0])
# print(sort_descending[-1])


