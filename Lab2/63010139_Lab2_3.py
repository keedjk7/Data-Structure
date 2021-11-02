class TorKham:

	def __init__(self):

		self.words = []

	def restart(self):
            self.words.clear()

            return "game restarted"

	def play(self,word):
            self.words.append(word[2:])
            Size = len(self.words)
            if(Size>1):
                tempBefore = self.words[Size-2][-2:]
                tempAfter = word[2:4]
                
                #print(tempBefore)
                #print(tempAfter)
                if tempBefore.upper() == tempAfter.upper() :
                    return self.words
                else:
                    return "game over"
            else :
                return self.words



torkham = TorKham()

print("*** TorKham HanSaa ***")


S = input("Enter Input : ").split(',')

for i in range (len(S)):
    if(S[i][0]=='R'):
        print(torkham.restart())
    elif (S[i][0]=='P'):
        print("'"+S[i][2:] + "' ->" ,torkham.play(S[i]))
    elif (S[i][0]=='X'):
        break
    else :
        print("'"+S[i] +"' is Invalid Input !!!")
        break