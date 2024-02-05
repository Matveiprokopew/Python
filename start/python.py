##вечный цикл
##Прокопьев Матвей
##Тестовая программа
t=0
while t==0:
   a=float(input("введите 1 число:"))
   b=float(input("введите 2 число:"))
   v=input('Что делаем? + - / *')
   if v=='+':
      summa=a+b

   elif v=='-':
      summa=a-b

   elif v=='/':
      summa=a/b

   elif v=='*':
      summa=a*b
   print("результат:", summa)

   