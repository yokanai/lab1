# python_basics.py

def count_vowels(data):
    """Считает количество гласных букв (a, e, i, o, u) в строке."""
    text = data.value if hasattr(data, 'value') else data
    vowels = set('aeiou')
    return sum(1 for ch in text.lower() if ch in vowels)


def has_unique_characters(data):
    """Проверяет, все ли символы в строке уникальны."""
    text = data.value if hasattr(data, 'value') else data
    return len(text) == len(set(text))


def count_one_bits(data):
    """Считает количество единиц в двоичном представлении числа."""
    number = data.value if hasattr(data, 'value') else data
    return bin(number).count('1')


def multiplicative_persistence(data):
    """Возвращает мультипликативную устойчивость числа."""
    number = data.value if hasattr(data, 'value') else data
    count = 0
    while number >= 10:
        product = 1
        for digit in str(number):
            product *= int(digit)
        number = product
        count += 1
    return count


def mse(data):
    """Средняя квадратичная ошибка между predicted и expected."""
    predicted = data.predicted
    expected = data.expected
    n = len(predicted)
    if n == 0:
        return 0.0
    total = 0.0
    for p, e in zip(predicted, expected):
        total += (p - e) ** 2
    return total / n


def prime_factorization(data):
    """Возвращает строку с разложением числа на простые множители."""
    number = data.value if hasattr(data, 'value') else data
    n = number
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            power = 0
            while n % d == 0:
                n //= d
                power += 1
            factors.append((d, power))
        d += 1 if d == 2 else 2
    if n > 1:
        factors.append((n, 1))
    parts = []
    for base, power in factors:
        if power == 1:
            parts.append(f"({base})")
        else:
            parts.append(f"({base}**{power})")
    return "".join(parts)


def pyramid(data):
    """Проверяет, можно ли сложить пирамиду из n кубиков."""
    n = data.value if hasattr(data, 'value') else data
    total = 0
    k = 0
    while total < n:
        k += 1
        total += k * k
    if total == n:
        return k
    return "It is impossible"


def is_balanced_number(data):
    """Проверяет, является ли число сбалансированным."""
    number = data.value if hasattr(data, 'value') else data
    s = str(number)
    length = len(s)
    if length % 2 == 0:
        # Чётная длина: просто делим пополам
        left = s[:length // 2]
        right = s[length // 2:]
    else:
        # Нечётная длина: пропускаем центральную цифру
        mid = length // 2
        left = s[:mid]
        right = s[mid + 1:]
    return sum(int(c) for c in left) == sum(int(c) for c in right)