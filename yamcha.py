

class MCD:
    @staticmethod
    def _euclid(n1, n2):
        return MCD._euclid(n2, n1 % n2) if n2 else n1

    @staticmethod
    def euclid(n1, n2):
        n1, n2 = sorted([abs(n1), abs(n2)])
        return MCD._euclid(n1, n2)

    @staticmethod
    def _bezout(n1, n2):
        if n1 == 0:
            return n2, 0, 1
        else:
            gcd, b_const_l, b_const_r = MCD._bezout(n2 % n1, n1)
            return gcd, b_const_r - (n2 // n1) * b_const_l, b_const_l

    @staticmethod
    def bezout(n1, n2):
        n1, n2 = sorted([abs(n1), abs(n2)])
        return MCD._bezout(n1, n2)
