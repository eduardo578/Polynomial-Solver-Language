class Polynomial(object):

    def __init__(self,coeffs):
        self.coefficients = coeffs

    def degree(self):
        return len(self.coefficients)-1

    def eval(self, x):
        p = 0
        for i in range(self.degree(), -1, -1):
            p = p + self.coefficients[i]*(x**i)
        return p

    def addition(self, other):
        list = []
        d = max(self.degree(), other.degree()) + 1
        for i in range(0, d, 1):
            list.append(0)
        c = Polynomial(list)
        for i in range(0, (self.degree() + 1), 1):
            c.coefficients[i] += self.coefficients[i]
        for i in range(0, other.degree() + 1, 1):
            c.coefficients[i] += other.coefficients[i]
        return c

    def substraction(self, other):
        list = []
        d = max(self.degree(), other.degree()) + 1
        for i in range(0, d, 1):
            list.append(0)
        c = Polynomial(list)
        for i in range(0, (self.degree() + 1), 1):
            c.coefficients[i] += self.coefficients[i]
        for i in range(0, other.degree() + 1, 1):
            c.coefficients[i] -= other.coefficients[i]
        return c

    def multiplication(self, other):
        list = []
        d = self.degree() + other.degree() + 1
        for i in range(0, d, 1):
            list.append(0)
        c = Polynomial(list)
        for i in range(0, self.degree() + 1, 1):
            for j in range(0, other.degree() + 1, 1):
                c.coefficients[i+j] += (self.coefficients[i]*other.coefficients[j])
        return c

    def division(self, other):
        dividend = self
        divisor = other
        quotient_list = []
        temp_quotient = []
        new_dividend = []
        div_result = []
        if other.degree() == 0:
            return "Division by 0 error"
        for i in range(0, self.degree() - other.degree() + 1, 1):
            quotient_list.append(0)
        while dividend.degree() >= divisor.degree():
            quotient_list[dividend.degree()-divisor.degree()] = (dividend.coefficients[dividend.degree()])/(divisor.coefficients[divisor.degree()])
            for i in range(0, dividend.degree() - divisor.degree() + 1, 1):
                temp_quotient.append(0)
            temp_quotient[dividend.degree()-divisor.degree()] = quotient_list[dividend.degree()-divisor.degree()]
            quotient = Polynomial(temp_quotient)
            temp_quotient = []
            pol_subtract = divisor.multiplication(quotient)
            dividend = dividend.substraction(pol_subtract)
            if dividend.coefficients[dividend.degree()] == 0:
                for i in range(0, dividend.degree(), 1):
                    new_dividend.append(0)
                    new_dividend[i] = dividend.coefficients[i]
            dividend = Polynomial(new_dividend)
            new_dividend = []
        quotient = Polynomial(quotient_list)
        remainder = dividend
        div_result.append(quotient)
        if remainder.degree() != 0 or remainder.coefficients[0] != 0:
            div_result.append(divisor)
            div_result.append(remainder)
        return div_result


    def differentiate(self):
        list = []
        if self.degree() == 0:
            return Polynomial(list)
        for i in range(0, self.degree(), 1):
            list.append(0)
        c = Polynomial(list)
        for i in range(0, self.degree(), 1):
            c.coefficients[i] = (i+1)*self.coefficients[i+1]
        return c

    def tostr(self):
        if self.degree() == 0:
            return "" + str(self.coefficients[0])
        if self.degree() == 1:
            return str(self.coefficients[1]) + "x + " + str(self.coefficients[0])
        s = str(self.coefficients[self.degree()]) + "x^" + str(self.degree())
        for i in range(self.degree()-1, -1, -1):
            if self.coefficients[i] == 0:
                continue
            elif self.coefficients[i] > 0:
                s = s + " + " + str(self.coefficients[i])
            elif self.coefficients[i] < 0:
                s = s + " - " + str(-1*(self.coefficients[i]))
            if i == 1:
                s = s + "x"
            elif i > 1:
                s = s + "x^" + str(i)
        return s