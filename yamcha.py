from math import sqrt, gcd


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


class PRIME:
    @staticmethod
    def is_prime(n):
        if n < 2:
            return False

        for k in range(2, int(sqrt(n)) + 1):
            if n % k == 0:
                return False

        return True

    @staticmethod
    def is_carmichael(n):
        for b in range(2, n):
            # b is relatively prime to n and pow(b, n-1) % n
            if gcd(b, n) == 1 and pow(b, n - 1, n) != 1:
                return False

        return True


class FACTORS:
    @staticmethod
    def prime_factors(n):
        list_pf = []
        if n >= 2:
            d = 2
            while d <= sqrt(n):
                if n % d == 0:
                    list_pf.append(d)
                    n /= d
                else:
                    d += 1
            list_pf.append(int(n))
        return list_pf
