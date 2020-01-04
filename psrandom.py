import time


class PseudoRandom:

    def __init__(self, seed=None):
        if not seed:
            seed = str(time.time()).split('.')[-1]

        self._seed = int(seed)

    @property
    def seed(self) -> int:
        """ seed getter

        :return: self._seed
            :type: int
        """

        return self._seed

    @seed.setter
    def seed(self, value: int) -> None:
        """ seed setter

        :param value: new seed value
            :type: int
        :return: self._seed
            :type: int
        """

        self._seed = int(value)

    def middle_square(self, n: int) -> int:
        """ Middle Square Random Function

        :param n: maximum random number length
            :type: int
        :return: random number
            :type: int
        """

        rand = str(self._seed * self._seed).rjust(n * 2, "0")
        half = n // 2
        self._seed = int(rand[half:half + n])
        return self._seed

    def linear_congruential(self, modulus: int, multiplier: int, increment: int) -> int:
        """ Linear Congruential Random Function

        :param modulus: modulus number (m)
            :type: int
            :example: 2 ** 31
        :param multiplier: multiplier number (a)
            :type: int
            :example: 1103515245
            :note: the length of the multiplier is the same as n param of middle_square method
        :param increment: increment number (c)
            :type: int
            :example: 12345
        :return: random number
            :type: int
        """

        self._seed = (multiplier * self._seed + increment) % modulus
        return self._seed
