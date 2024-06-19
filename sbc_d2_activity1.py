word = "summer bootcamp"
add = ""

for i in word:
    if i == "s":
        
        add += i.upper()
    elif i == "p":
        add += i.upper()
        
        
    else:
        add += i.lower()

print(add)
word1 = word.replace("b" , "L")
print(word1[7:11])
word2 = word.replace("p" , "E")
print(word2[-4:])
word3 = word.replace("su","AR")
print(word3[0:2])
word3 = word.replace(" ", "")
wordxx = word3.isalpha()

print(wordxx)