def bon(w):
    keep_check = ''
    have_same_char = False
    for i in range(len(w)):
        if keep_check == w[i]:
            have_same_char = True
            break
        keep_check = w[i]

    num = 0
    if have_same_char == True:
        num += (ord(keep_check.lower())-96)*4

    return num
    
    
secretCode = input("Enter secret code : ")
print(bon(secretCode))