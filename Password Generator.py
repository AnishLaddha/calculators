import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
usrblock = int(input("Enter how many blocks: "))
blocknum = 0
passwordlist = []
def block():
    length = 4
    block1 = []
    i = 0
    while i <= length:
        uplow = random.randint(0,2)
        wordnum = random.randint(0,2)
        if wordnum == 0:
            x = random.randint(0,25)
            let = letters[x]
            if uplow == 0:
                let = let.upper()
                block1.append(let)
            else:
                block1.append(let)
            i = i+1
        else:
            num = random.randint(0,11)
            block1.append(str(num))
            i = i+1
    block1 = ''.join(block1)
    return block1
while blocknum <= usrblock:
    if blocknum == 0:
        passwordlist.append(block())
        blocknum = blocknum + 1
    else:
        passwordlist.append("-")
        passwordlist.append(block())
        blocknum = blocknum + 1
password = ''.join(passwordlist)
print(password)

