def encrypt(target: str, decode1: str, decode2: str, base_step: int, reset_step: int) -> str:
    step = base_step 
    result = ""
    shift = 0
    count = 0       
    for i in target:
        if i == " ":       
            result += " "
            continue        
        if count == reset_step:    
            count = 0
            shift += 1
            step = base_step
        if shift % 2 == 1 and shift != 0:     
            decode2 += decode2[0]
            decode2 = decode2[1:len(decode2)]
        elif shift % 2 == 0 and shift != 0:    
            decode1 = decode1[len(decode1) - 1:len(decode1)] + decode1[0:len(decode1) - 1]
        pos = decode1.find(i)           
        pos += step                     
        if (pos > len(decode2) - 1):    
            pos = abs(len(decode2) - pos)       
        result += decode2[pos]          
        step += 1                       
        count += 1                      
    return result


def decrypt(target: str, decode1: str, decode2: str, base_step: int, reset_step:int) -> str:
    #processing value
    step = base_step
    result = ""
    shift = 0
    count = 0
    for i in target:
        if i == " ":                
            result += " "
            continue
        if count == reset_step:     
            count = 0
            shift += 1
            step = base_step
        if shift % 2 == 1 and shift != 0:      
            decode2 += decode2[0]
            decode2 = decode2[1:len(decode2)]
        elif shift % 2 == 0 and shift != 0:
            decode1 = decode1[len(decode1) - 1:len(decode1)] + decode1[0:len(decode1) - 1]
        pos = decode2.find(i)               
        pos -= step                         
        if (pos < 0):                       
            pos = abs(len(decode1) + pos)   
        result += decode1[pos]              
        step += 1                           
        count += 1                          
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
