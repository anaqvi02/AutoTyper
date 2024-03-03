import keyboard
import time
import random


mistypes = {"a":["q","s","z"],"b":["g","n"],"c":["x","v","d","f"],"d":["s","e","f","c"],"e":["w","s","d","r"],"f":["d","r","t","g","v","c"],"g":["f","t","y","h","b","v"],"h":["g","y","u","j","n","b"],"i":["u","j","k","o"],"j":["h","u","i","k","m","n"],"k":["j","i","o","l","m"],"l":["k","o","p"],"m":["n","j","k","l"],"n":["b","h","j","m"],"o":["i","k","l","p"],"p":["o","l"],"q":["w","a"],"r":["e","d","f","t"],"s":["a","w","e","d","z","x"],"t":["r","f","g","y"],"u":["y","h","j","i"],"v":["c","f","g","b"],"w":["q","a","s","e"],"x":["z","s","d","c"],"y":["t","g","h","u"],"z":["a","s","x"]," ":["b","n","m"," "],"A":["Q","S","Z"],"B":["G","N"],"C":["X","V","D","F"],"D":["S","E","F","C"],"E":["W","S","D","R"],"F":["D","R","T","G","V","C"],"G":["F","T","Y","H","B","V"],"H":["G","Y","U","J","N","B"],"I":["U","J","K","O"],"J":["H","U","I","K","M","N"],"K":["J","I","O","L","M"],"L":["K","O","P"],"M":["N","J","K","L"],"N":["B","H","J","M"],"O":["I","K","L","P"],"P":["O","L"],"Q":["W","A"],"R":["E","D","F","T"],"S":["A","W","E","D","Z","X"],"T":["R","F","G","Y"],"U":["Y","H","J","I"],"V":["C","F","G","B"],"W":["Q","A","S","E"],"X":["Z","S","D","C"],"Y":["T","G","H","U"],"Z":["A","S","X"]}


wpm = random.randint(0,15)+80

accuracy = (-0.037*((wpm-80)*(wpm-80)))+100
print("accuracy:", accuracy, " | wpm:", wpm)
total_mistypes = 0
cpm=wpm*5

time.sleep(2)

total_a = 0

#500
for char in ('Hello World! I am a preprogramed typing algorithm. I am not typing this. Lol. Hi. Or something. e.'):
    if random.randint(0,100) >= accuracy:
        if char in mistypes:
            print("mistype")
            total_mistypes=total_mistypes+1
            keyboard.write(mistypes[char][random.randint(0,len(mistypes[char])-1)])
            time.sleep(cpm/1000)
            keyboard.press('delete')
            time.sleep(cpm/7500)
            keyboard.write(char)
    elif char == " ":
        time.sleep(cpm/4000)
        time.sleep(random.randint(1,3)/150)
        keyboard.write(" ")
    else:
        a = (((random.choice([-1, 1]))*random.randint(1,10))/600)
        total_a = total_a+a
        print(f"a offset: {a:.2f}", f"| cpm: {(cpm/6000):.2f}", f"total: {a+(cpm/6000):.2f}")
        time.sleep(cpm/6000 + a)
        keyboard.write(char)

print("mistypes: ", total_mistypes,"%")

