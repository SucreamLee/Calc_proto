def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("연산 선택.")
print("1. 덧셈")
print("2. 뺄셈")
print("3. 곱셈")
print("4. 나눗셈")
print("0. 나가기")

while(True):
  choice = input("선택 (1/2/3/4/0): ")
  if choice == '0':
    print('종료하기')
    break

  n1 = float(input("첫 번째 숫자 입력: "))
  n2 = float(input("두 번째 숫자 입력: "))

  if choice == '1':
      print(n1, "+", n2, "=", add(n1,n2))

  elif choice == '2':
      print(n1, "-", n2, "=", subtract(n1,n2))

  elif choice == '3':
      print(n1, "*", n2, "=", multiply(n1,n2))

  elif choice == '4':
      print(n1, "/", n2, "=", divide(n1,n2))
      
  else:
      print("잘못된 입력입니다.")
  print()