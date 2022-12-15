def Hello(name):
    print("Hello " + name)

Hello("User")

def pack(a,b,c):
    return [a,b,c]

print(pack("hi","hello","welcome"))

def lunchpack(lunch):
    if len(lunch) == 0:
        print("We are empty!")
    else:
        for i in range(len(lunch)):
            if i == 0:
                print(f"First I eat {lunch[0]}")
        else:
             print(f"Next I eat {lunch[i]}")

lunchpack(["cheeseburger", "hotdog", "Munchkin"])