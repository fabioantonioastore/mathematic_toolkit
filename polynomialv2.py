def factors(n: int) -> set[int]:
    n = abs(n)
    factors = set()
    sqrt = int(n ** (1 / 2))
    if n % 2 == 0:
        for i in range(1, sqrt + 1):
            if n % i == 0:
                factors = factors.union({n // i, -(n // i), i, -i})
        return factors
    for i in range(1, sqrt + 1, 2):
        if n % i == 0:
            factors = factors.union({n // i, -(n // i), i, -i})
    return factors


def polynomial_possible_factors(an: int, a0: int) -> set[int]:
    possible_factors = set()
    for a0_factor in factors(a0):
        for an_factor in factors(an):
            possible_factors.add(a0_factor / an_factor)
    return possible_factors


def synthetic_division(
    c: int | float, coefficients: list[int | float]
) -> list[int | float]:
    result_row = []
    result_row.append(coefficients[0])
    for coefficient in coefficients[1::]:
        result = (result_row[-1] * c) + coefficient
        result_row.append(result)
    return result_row


def quadratic_solver(
    a: int | float, b: int | float, c: int | float
) -> set[int | float]:
    delta = (b**2) - (4 * a * c)
    if delta == 0:
        return {-b / (2 * a)}
    if delta < 0:
        return set()
    sqrt = delta ** (1 / 2)
    return {(-b + sqrt) / (2 * a), (-b - sqrt) / (2 * a)}


def polynomial_solver(coefficients: list[int | float]) -> set[int | float]:
    solutions = set()
    possible_factors = polynomial_possible_factors(coefficients[0], coefficients[-1])
    for factor in possible_factors:
        result = synthetic_division(factor, coefficients)
        if result[-1] == 0:
            solutions.add(factor)
            coefficients = result[:-1:]
    if len(coefficients) > 3:
        while True:
            change = False
            for factor in possible_factors:
                result = synthetic_division(factor, coefficients)
                if result[-1] == 0:
                    solutions.add(factor)
                    coefficients = result[:-1:]
                    change = True
            if not change:
                break
    if len(coefficients) == 3:
        quadratic_result = quadratic_solver(
            coefficients[0], coefficients[1], coefficients[2]
        )
        for solution in quadratic_result:
            solutions.add(solution)
    return solutions
