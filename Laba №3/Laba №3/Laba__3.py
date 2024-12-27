#1)

x = open('Laba_3.txt')
a=x.read()
print(a)
x.close()

f = open('Laba_3.txt','a')
print(a)

#2)

text = input()
with open('Laba_3.txt','a') as file:
    file.writelines(f"{text} \n")

with open('Laba_3.txt','r') as file:
    k =file.read()
print(k)

#3)

p = input("Enter the file name: ")
try:
    with open(p, 'r') as file:
        l = file.read()
except FileNotFoundError:
    print('File not found, try again')
    exit()
print(l)