def changeme( arg1 ):
   "This changes a passed list into this function"
   print("Value, id of arg1 inside the function before change: ",arg1,", ",id(arg1))
   arg1 = [1,2,3]
   # arg1[2] = 50
   print("Value, id of arg1 inside the function after change: ",arg1,", ",id(arg1))
   return

x = [10, 20, 30]
print("Value, id of x before function call: ",x,", ",id(x))
changeme( x )
print("Value, id of x after function call: ",x,", ",id(x))