class Prime:
    def __init__(self, max_num=None, primes=None):
        self.max_num = max_num if max_num is not None else 0
        self.primes = primes if primes is not None else []

    def crivo(self):
        is_prime = [True] * (self.max_num + 1)
        primes = []

        for num in range(2, self.max_num):
            if is_prime[num]:
                primes.append(num)

                for j in range(2 * num, self.max_num, num):
                    is_prime[j] = False

        return primes

    def sum_digits(self, number):
        return sum([int(digit) for digit in str(number)])

    def filter_type_sum(self, num):
        new_primes = []

        for prime in self.primes:
            sum_d = self.sum_digits(prime)

            if sum_d == num:
                new_primes.append(prime)

        return new_primes

    def filter_type_mod(self, num):
        new_primes = []

        for prime in self.primes:
            if prime % num == 1:
                new_primes.append(prime)

        return new_primes

    def multi_digits(self, number):
        result = 1

        for digit in str(number):
            if digit != '0':
                result *= int(digit)

        return result

    def filter_type_multi(self, num):
        new_primes = []

        for prime in self.primes:
            multi = self.multi_digits(prime)

            if multi == num:
                new_primes.append(prime)

        return new_primes
