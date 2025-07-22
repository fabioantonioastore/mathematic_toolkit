def get_factors(n: int) -> list[int]:
    factors = [n, -n]
    for i in range(1, abs((n // 2) + 1)):
        if n % i == 0:
            factors.append(i)
            factors.append(-i)
    return factors


def polynomial_possibly_factors(first: int | float, last: int | float) -> set[int | float]:
    possibly_factors = set()
    first_factors = get_factors(first)
    last_factors = get_factors(last)
    for a in last_factors:
        for b in first_factors:
            possibly_factors.add(a / b)
    return possibly_factors


def polynomial_solver(terms: list[int | float]) -> list[int | float]:
    factors = []
    possibly_factors = polynomial_possibly_factors(terms[0], terms[-1])
    for factor in possibly_factors:
        result = synthetic_division(factor, terms)
        if result[-1] == 0:
            factors.append(factor)

    return factors


def synthetic_division(c: int | float, terms: list[int | float]) -> list[int | float]:
    result_row = []
    result_row.append(terms[0])
    for term in terms[1::]:
        result = (result_row[-1] * c) + term
        result_row.append(result)
    return result_row


terms = [
    12, -20, 1, 3
]
print(polynomial_solver(terms))