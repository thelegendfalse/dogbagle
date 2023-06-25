
# Debugger
dog = "image1", "image3", "image20"
bagle = "image2", "image5", "image10"

if bagle in dog:
    print("Error, Restarting")
    quit()
else:
    print("It worked!")

doglist = tuple([dog])
baglelist = tuple([bagle])
print(baglelist)
print(doglist)

if baglelist in doglist:
    print("Error Restarting")
    quit()

for i in doglist:
    print(i)

for x in baglelist:
    print(x,i)

quit()


