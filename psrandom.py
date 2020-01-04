import time


class PseudoRandom:

    def __init__(self, seed=None):
        if not seed:
            seed = str(time.time()).split('.')[-1]

        self._seed = int(seed)

    @property
    def seed(self) -> int:
        return self._seed

    @seed.setter
    def seed(self, value: int) -> None:
        self._seed = int(value)

    def middle_square(self, n: int) -> int:
        rand = str(self._seed * self._seed).rjust(n * 2, "0")
        half = n // 2
        self._seed = int(rand[half:half + n])
        return self._seed

    def middle_square_float(self, n: int) -> float:
        return self.middle_square(n) / int(''.ljust(n, '9'))


pr = PseudoRandom()
for _ in range(20):
    print(pr.middle_square(4))
