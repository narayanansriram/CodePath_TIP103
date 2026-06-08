def tiggerfy(word):
    result = ""
    i = 0
    while i<(len(word)):
        if i<(len(word)-1) and (word[i:i+2].lower() == "gg" or word[i:i+2].lower() == "er"):
            i+=2
            continue
        elif word[i].lower() == "t" or word[i].lower() == "i":
            i+=1
            continue
        result+=word[i].lower()
        i+=1
    return result

word = "Trigger"
print(tiggerfy(word))
assert "r"==tiggerfy(word),"Trigger expect r"

word = "eggplant"
print(tiggerfy(word))
assert "eplan"==tiggerfy(word),"eggplant expect eplan"

word = "Choir"
print(tiggerfy(word))
assert "chor"==tiggerfy(word),"Choir expect chor"
