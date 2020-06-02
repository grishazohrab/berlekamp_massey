from polynomial import Polynomial


class BerlekampMassey:
    def __init__(self, mod=2):
        self.mod = mod
        self.C = Polynomial(mod=self.mod, coefficients=[1])
        self.C_star = Polynomial(mod=self.mod, coefficients=[1])
        self.delta_star = 1
        self.L = 0
        self.n = 0
        self.m = 1

    def __call__(self, *args, **kwargs):
        seq = list(args[0])
        for ii, s in enumerate(seq):
            print(f"Element {ii} _ value {s}")
            if self.mod:
                delta = (s + sum([seq[jj] * self.C.coefficients[ii - jj] for jj in range(ii - 1, -1, -1)
                                  if ii - jj < self.C.degree()], 0)) % self.mod
            else:
                delta = (s + sum([seq[jj] * self.C.coefficients[ii - jj] for jj in range(ii - 1, -1, -1)
                                  if ii - jj < self.C.degree()], 0))
            print(f"Delta is {delta}")
            if delta == 0:
                self.m += 1
                self.n += 1
                print(f"n is {self.n}")
                print(f"m is {self.m}")
            else:
                temp_T = self.C
                temp_m_c = [0 for _ in range(self.m)]
                if self.mod:
                    temp_m_c.append((delta / self.delta_star) % self.mod)
                else:
                    temp_m_c.append(int(delta / self.delta_star))
                self.C = self.C - (Polynomial(self.mod, temp_m_c) * self.C_star)
                print(f"C is {self.C}")
                if 2 * self.L <= self.n:
                    self.L = self.n + 1 - self.L
                    print(f"L is {self.L}")
                    self.m = 1
                    print(f"m is {self.m}")
                    self.C_star = temp_T
                    print(f"C_star is {self.C_star}")
                    self.delta_star = delta
                    print(f"delta_star is {self.delta_star}")
                else:
                    self.m += 1
                    print(f"m is {self.m}")
                self.n += 1
                print(f"n is {self.n}")
        return self.L



