# pseudo-random-generator
Pseudo random number generators algorithms

## Algorithms

### Middle Square
- About:  
  In mathematics, the middle-square method is a method of generating pseudorandom numbers. In practice it is not a good method, since its period is usually very short and it has some severe weaknesses; repeated enough times, the middle-square method will either begin repeatedly generating the same number or cycle to a previous number in the sequence and loop indefinitely. [by wikipedia](https://en.wikipedia.org/wiki/Middle-square_method)

- Code:
  ```python
  >>> from psrandom import PseudoRandom
  
  >>> pr = PseudoRandom(34895434567898765456)
  >>> for _ in range(10):
  >>>   print(pr.middle_square(5))
  17691
  12971
  68246
  57516
  8090
  65448
  83440
  62233
  72946
  21118
  ```

### Linear Congruential

- About:  
  A linear congruential generator (LCG) is an algorithm that yields a sequence of pseudo-randomized numbers calculated with a discontinuous piecewise linear equation. The method represents one of the oldest and best-known pseudorandom number generator algorithms. The theory behind them is relatively easy to understand, and they are easily implemented and fast, especially on computer hardware which can provide modulo arithmetic by storage-bit truncation.  [by wikipedia](https://en.wikipedia.org/wiki/Linear_congruential_generator)
  
- Code:
  ```python
  >>> from psrandom import PseudoRandom
  
  >>> pr = PseudoRandom(34895434567898765456)
  >>> for _ in range(10):
  >>>   print(pr.linear_congruential(2 ** 31, 1103515245, 12345))
  1049396617
  58378638
  1451574703
  1179921852
  858714437
  954069146
  116035019
  521431464
  1406295233
  119176294
  ```
