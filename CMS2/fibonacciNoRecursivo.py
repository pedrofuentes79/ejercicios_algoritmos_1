import sys

def fibonacciNoRecursivo(n: int) -> int:

  if n == 0:
    return 0
  elif n == 1:
    return 1

  anterior: int = 0
  actual: int = 1
   
  for i in range(2, n+1):
    #Usé la declaración en una sola línea pues se superponían los valores si lo hacía separado.
    #Podría haber usado otra variable para evitar esta declaración, pero me pareció mucho más entendible así.
  
    anterior, actual = actual, anterior+actual
  return actual


if __name__ == '__main__':
  x = int(input())
  print(fibonacciNoRecursivo(x))