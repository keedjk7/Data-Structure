class translator:

    def deciToRoman(self, num):
        listRoman = []

        if num ==0 :
            listRoman.append("0")
        elif num < 0 :
            listRoman.append("-")
            num *= -1

        while(num!=0):
            if num >= 1000 :
                listRoman.append("M")
                num -= 1000
            elif num >= 900 :
                listRoman.append("CM")
                num -= 900 
            elif num >= 500 :
                listRoman.append("D")
                num -= 500 
            elif num >= 400 :
                listRoman.append("CD")
                num -= 400 
            elif num >= 100 :
                listRoman.append("C")
                num -= 100 
            elif num >= 90 :
                listRoman.append("XC")
                num -= 90 
            elif num >= 50 :
                listRoman.append("L")
                num -= 50 
            elif num >= 40 :
                listRoman.append("XL")
                num -= 40 
            elif num >= 10 :
                listRoman.append("X")
                num -= 10 
            elif num >= 9 :
                listRoman.append("IX")
                num -= 9
            elif num >= 5 :
                listRoman.append("V")
                num -= 5 
            elif num >= 4 :
                listRoman.append("IV")
                num -= 4 
            elif num >= 1 :
                listRoman.append("I")
                num -= 1 
      
        stringRoman = ""
        for item in listRoman :
            stringRoman += item
        return stringRoman         


    def romanToDeci(self, s):
        number = 0
        listNumber = []
        for element in s :
            listNumber.append(element)

        Size = len(s)   
        
        i=0
        while(i<Size):
            if s[i] == 'M' :
                number += 1000
            elif i+1<Size and s[i] =='C' and s[i+1] == 'M':
                number +=900
                i+=1
            elif s[i] == 'D' :
                number += 500
            elif i+1<Size and s[i] == 'C' and s[i+1] =='D':
                number += 400
                i+=1 
            elif s[i] == 'C' :
                number +=100
            elif i+1<Size and s[i] =='X' and s[i+1] =='C':
                number +=90 
                i+=1
            elif s[i] =='L':
                number +=50
            elif i+1<Size and s[i] =='X' and s[i+1] == 'L':
                number +=40
                i+=1
            elif s[i] == 'X':
                number +=10
            elif i+1<Size and s[i] == 'I' and s[i+1] == 'X':
                number +=9
                i+=1
            elif s[i] == 'V':
                number +=5
            elif i+1<Size and s[i] == 'I' and s[i+1] == 'V':
                number +=4
                i+=1
            elif s[i] == 'I':
                number +=1
            i+=1

        if listNumber[0] == '-':
            s.replace('-', '')
            number *=-1

        return number

num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))