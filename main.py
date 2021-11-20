#make by Otaros with Love <3 <3 <3
#just for learning purpose
#not for commerce
#pls use with love :> :3
#Improve the code plz
def encrypt(target: str, decode1: str, decode2: str, base_step: int, reset_step: int) -> str:
    #processing value
    step = base_step #save the step for the reset
    result = ""
    shift = 0
    count = 0       #counting for the reset
    for i in target:
        if i == " ":        #if the char is space just skip
            result += " "
            continue        #skip to next char
        if count == reset_step:     #check reset
            count = 0
            shift += 1
            step = base_step
        if shift % 2 == 1 and shift != 0:       #shifting the decode2 string
            decode2 += decode2[0]
            decode2 = decode2[1:len(decode2)]
        elif shift % 2 == 0 and shift != 0:     #shifting the decode1 string
            decode1 = decode1[len(decode1) - 1:len(decode1)] + decode1[0:len(decode1) - 1]
        pos = decode1.find(i)           #take position
        pos += step                     #plus step -> new position
        if (pos > len(decode2) - 1):    #roll back if pos is out of decode2 range
            pos = abs(len(decode2) - pos)       #just take abs to prevent negative value
        result += decode2[pos]          #take the encrypted char
        step += 1                       #increase the step
        count += 1                      #counting to reset
    return result


def decrypt(target: str, decode1: str, decode2: str, base_step: int, reset_step:int) -> str:
    #processing value
    step = base_step
    result = ""
    shift = 0
    count = 0
    for i in target:
        if i == " ":                #like encrypt just skip the space char
            result += " "
            continue
        if count == reset_step:     #checking reset
            count = 0
            shift += 1
            step = base_step
        if shift % 2 == 1 and shift != 0:       #shifting like encrypt
            decode2 += decode2[0]
            decode2 = decode2[1:len(decode2)]
        elif shift % 2 == 0 and shift != 0:
            decode1 = decode1[len(decode1) - 1:len(decode1)] + decode1[0:len(decode1) - 1]
        pos = decode2.find(i)               #find position
        pos -= step                         #minus step -> previous position
        if (pos < 0):                       #turn around if out of range
            pos = abs(len(decode1) + pos)   #same reason for decrypt
        result += decode1[pos]              #take the decrypted char
        step += 1                           #increase step
        count += 1                          #counting
    return result

#decrypting still in develope
#testing
#you can change two processing string to make the encrypting more security
str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
target = "HELLO WORLD"
init_step = 1
reset_step = 4
print(target)
en = encrypt(target, str1, str2, init_step,reset_step)
print(en) #IGOPQ AUZRL
de = decrypt(en, str1, str2, init_step,reset_step)
print(de)
