from itertools import zip_longest


def sign(t):
    if t < 0:
        return -1
    else:
        return 1


class Polynomial:

    def __init__(self, mod, coefficients):
        """ input: coefficients are in the form a_n, ...a_1, a_0
        """
        self.coefficients = list(coefficients)  # tuple is turned into a list
        self.mod = mod

    def __repr__(self):
        """
        method to return the canonical string representation
        of a polynomial.

        """
        return "Polynomial" + str(self.coefficients)

    def __call__(self, x):
        res = 0
        for coeff in self.coefficients:
            if self.mod:
                res = (res * x + coeff) % self.mod
            else:
                res = res * x + coeff
        return res

    def degree(self):
        return len(self.coefficients)

    def __add__(self, other):
        c1 = self.coefficients
        c2 = other.coefficients
        if self.mod:
            res = [sign(sum(t)) * (abs(sum(t)) % self.mod) for t in zip_longest(c1, c2, fillvalue=0)]
        else:
            res = [sum(t) for t in zip_longest(c1, c2, fillvalue=0)]
        return Polynomial(self.mod, res)

    def __sub__(self, other):
        c1 = self.coefficients
        c2 = other.coefficients

        if self.mod:
            res = [sign(t1 - t2) * (abs(t1 - t2) % self.mod) for t1, t2 in zip_longest(c1, c2, fillvalue=0)]
        else:
            res = [(t1 - t2) for t1, t2 in zip_longest(c1, c2, fillvalue=0)]
        return Polynomial(self.mod, res)

    def __mul__(self, other):
        _s = self.coefficients
        _o = other.coefficients
        res = [0] * (len(_s) + len(_o) - 1)
        for selfpow, selfco in enumerate(_s):
            for valpow, valco in enumerate(_o):
                res[selfpow + valpow] += selfco * valco
                if self.mod:
                    res[selfpow + valpow] = sign(res[selfpow + valpow]) * (abs(res[selfpow + valpow]) % self.mod)

        return Polynomial(self.mod, res)

