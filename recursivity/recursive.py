# Etape 1 : Somme d'une liste de nombres

def sumList(l) :
    if len(l)==1:
        return l[0]
    return l[0]+sumList(l[1:])

print(sumList([8,5,9]))


# Etape 2 : Factoriel

def fact(n):
  if n==0 or n==1:
    return 1
  return n*fact(n-1)

print(fact(3))


# Etape 3 : Fibonacci

def fibonacci(n):
    if n==0 or n==1:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(3))