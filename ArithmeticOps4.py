def calculos(n):
    i = 0
    while n > i:
        print(i**2)
        i= i + 1

if __name__ == '__main__':
    n = int(input())
    calculos(n)