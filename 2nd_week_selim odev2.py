for x in range(10):
    print("turkiye turklerindir")

e = 0
while e < 10:
    print("turkiye turklerindir")
    e += 1
    

e = int(input("euro kac tl?.."))
while e > 10:
    e = int(input("yaktin bizi tayyip, peki simdi kac tl?.."))
    print(e)
    if e < 10:
        break
print("turkiye turklerindir")
