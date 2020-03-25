# for x in range(10):
#     print("turkiye turklerindir")


# euro = float(input("euro bugun kac TL? "))
# while euro > 10:
#     print("yaktin bizi tayyip")
# else:print("turkiye turklerindir")



euro = float(input("euro bugun kac TL"))
while euro > 10:
    print(input("yaktin bizi tayyip peki simdi kac TL? "))
### Eger 10> bir deger verirsen tekrar sora sora gidiyor 
### Fakat bu sefer 10< bir deger verirsem loop un disina cikmiyor 
### Loop un icine nasil tekrar condition ekleyebilirim?
### salakca bir soruysa kusura bakma simdiden :P    
for x in range(10):
    print("turkiye turklerindir")

