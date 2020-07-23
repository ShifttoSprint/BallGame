import random

class Random:
    def Choice(a,b):
        file=open("rand.txt","w+")
        temp=file.read()
        lastx=temp.strip("\n")
        x=random.randint(a,b)
        while lastx==x:
            x=random.randint(a,b)
        lastx=str(x)
        file.seek(0)
        file.write(lastx)
        file.flush()
        file.close()
        return x


