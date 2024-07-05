import random
n = random.randint(1,100)
a=-1
guesses =0
while(a!=n):
    guesses+=1
    a=int(input("guess the number :"))
    if(a<n):
        print("higher number plese!")
    else:
        print("lower number plese!")

print(f"you have gussed the number : {n} correctly in {guesses}")