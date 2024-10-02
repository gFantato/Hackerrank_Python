def calculos(n):
    i = 0
    while n > i:
        print(i**2)
        i= i + 1
        
def calculos2(n):
    
    for i in range(0,n):
        print(i**2)

def calculos3(n):
    
    lambida = [(i**2) for i in range(0,n)]
    print(lambida)
        
if __name__ == '__main__':
    n = int(input())
    calculos3(n)