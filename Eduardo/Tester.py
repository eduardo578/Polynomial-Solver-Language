from Polynomial import Polynomial
# = TheClass()

coefficients = [10, 3, 3, 4]
coefficients1 = [1, 5, 2]
coefficients2 = [1, 5]
c = Polynomial(coefficients)
d = Polynomial(coefficients1)
e = Polynomial(coefficients2)
print(c.tostr())
print(d.tostr())
print("_________________")
print("Eval: " + str(c.eval(2)))
print("Sum :" + str(c.addition(d).tostr()))
print("Sub: " + c.substraction(d).tostr())
print("Mult: " + c.multiplication(d).tostr())
#print("Div: " + c.division(d).tostr())
print("Deri: " + e.differentiate().tostr())