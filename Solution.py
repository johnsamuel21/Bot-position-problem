input1 = int(input())
input2 = int(input())
input3 = input()
input4 = input()
flag = True
def findnext(pos):
    if pos[2] == "E":
        return (str(int(pos[0])+1),pos[1])
    if pos[2] == "W":
        return (str(int(pos[0])-1),pos[1])
    if pos[2] == "N":
        return (pos[0],str(int(pos[1])+1))
    if pos[2] == "S":
        return (pos[0],str(int(pos[1])-1))
    if pos[2] == "SE":
        return (str(int(pos[0])+1),str(int(pos[1])-1))
    if pos[2] == "SW":
        return (str(int(pos[0])-1),str(int(pos[1])-1))
    if pos[2] == "NE":
        return (str(int(pos[0])+1),str(int(pos[1])+1))
    if pos[2] == "NW":
        return (str(int(pos[0])-1),str(int(pos[1])-1))

def direction(bot,com):
    dir = {"E":360,"N":90,"W":180,"S":270,"NE":45,"NW":135,"SW":225,"SE":315}
    final = {0:"E",1:"NE",2:"N",3:"NW",4:"W",5:"SW",6:"S",7:"SE"}
    val = dir[bot]
    if com =="R":
        val = val-90
    elif com == "r":
        val = val-45
    elif com == "L":
        val = val+90
    elif com =="l":
        val = val+45
    val = (val//45)%8
    return final[val]

position = input3.split("-")
command = input4.split()
for i in command:
    if i=="M":
        position[0],position[1] = findnext(position)
        if int(position[0])>input1:
            position[0] = str(int(position[0])-1)
            print("-".join(position)+"-ER")
            flag = False
            break
        if int(position[1])>input2:
            position[1] = str(int(position[1])-1)
            print("-".join(position)+"-ER")
            flag = False
            break
    else:
        position[2] = direction(position[2],i)


if flag:
    print("-".join(position))
