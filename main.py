# EX 1
from functools import cache

@cache
def is_in_fibo(num: float):
    a, b = 0, 1
    while b < num:
        b, a = a + b, b
    return num == a or num == b

# EX 2
def count_a(text: str):
    return text.lower().count('a')

# EX 3
"""
K => SOMA
1 => 1
2 => 3
3 => 6
4 => 10
5 => 15
6 => 21
7 => 28
8 => 36
9 => 45
10 => 55
11 => 66

R.: 66
"""

# EX 4
"""
a) 1, 3, 5, 7, ___
1 + 2 = 3
3 + 2 = 5
5 + 2 = 7
7 + 2 = 9
R.: 9

b) 2, 4, 8, 16, 32, 64, ____
2 * 2 = 4
4 * 2 = 8
8 * 2 = 16
16 * 2 = 32
32 * 2 = 64
64 * 2 = 128
R.: 128

c) 0, 1, 4, 9, 16, 25, 36, ____
0 * 0 = 0
1 * 1 = 1
2 * 2 = 4
3 * 3 = 9
4 * 4 = 16
5 * 5 = 25
6 * 6 = 36
7 * 7 = 49
R.: 49

d) 4, 16, 36, 64, ____
2 * 2 = 4
4 * 4 = 16
6 * 6 = 36
8 * 8 = 64
9 * 9 = 81
R.: 81

e) 1, 1, 2, 3, 5, 8, ____
1 + 0 = 1
1 + 1 = 2
2 + 1 = 3
3 + 2 = 5
5 + 3 = 8
5 + 8 = 13
R.: 13

f) 2, 10, 12, 16, 17, 18, 19, ____
2 = [D]ois
10 = [D]ez
12 = [D]oze
16 = [D]ezesseis
17 = [D]ezessete
18 = [D]ezoito
19 = [D]ezenove
200 = [D]uzentos
R.: 200
"""

# EX 5
"""
Ligue o primeiro interruptor por alguns minutos e depois desligue-o. Em seguida, ligue o segundo interruptor e vá até a sala das lâmpadas. A lâmpada que estiver acesa é controlada pelo segundo interruptor. A lâmpada apagada, mas quente, é controlada pelo primeiro interruptor. A lâmpada apagada e fria é controlada pelo terceiro interruptor, que você não usou.
"""