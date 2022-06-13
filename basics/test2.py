def calculate(a, b, operation):
   result = None
 
   if operation == '+':
       result = sum(a, b)
 
   elif operation == '-':
       result = subtract(a, b)
  
   elif operation == '/':
       result = divide(a, b)
 
   elif operation == '*':
       result = multiply(a, b)
 
  # Возведение в степень
   elif operation == '^' or operation == '**':
       result = pow(a, b)
 
   else:
       print('Неизвестная операция')
 
   return result