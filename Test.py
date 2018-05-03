print('Hello World')
print('can do this'+'yes')
print('1+3=',1+3)
example=print('toto')
example

i=1
while i<10:
    print(i)
    if i== 2:
        print('i=2')
    i+=1

MyList=[1,3,6,3,2,]

for i in MyList:
    print(i)
    print('a')
print('end')

for i in range(2,23,5):
    print(i)


x = 5
y = 5
z = 6

if x > y:
    print(x,'>',y)
elif x== y:
    print(x,'=',y)
else:
    print(x,'<=',y)

def myfunction(param):
    i=1
    while i<param:
        print(i)
        if i== 10:
            print('dix')
        elif i==20:
            print('vingt')
        else:
            print('autre')
        i+=1
    return(param+100)

myvar=myfunction(21)
print(myvar)

mytext='Ligne 1\nLigne2\nLigne3'
myfile=open('MyFichier.txt','w')
myfile.write(mytext)
myfile.close()
