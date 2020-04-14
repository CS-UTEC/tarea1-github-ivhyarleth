num = int(input())
def Primo(num):
    if (num < 1):
        print("No es primo")
        return False
    elif (num == 2):
        print("Es primo")
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                print("No es primo")
                return False
        print("Es primo")
        return True

Primo(num)