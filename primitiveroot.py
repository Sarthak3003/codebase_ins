def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def find_primitive_root(number):
    required_factors = []
    phi = number - 1

    for i in range(2, phi + 1):
        if gcd(number, i) == 1:
            required_factors.append(i)

    for primitive_root in range(2, number):
        is_primitive_root = True
        for factor in required_factors:
            if pow(primitive_root, phi // factor, number) == 1:
                is_primitive_root = False
                break

        if is_primitive_root:
            return primitive_root

    return None


# Example usage:
number = 7

primitive_root = find_primitive_root(number)
if primitive_root is not None:
    print("Primitive Root of", number, "is", primitive_root)
else:
    print("No Primitive Root found for", number)