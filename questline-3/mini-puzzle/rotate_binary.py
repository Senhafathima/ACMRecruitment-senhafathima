# rotate_binary.py

def rotate_binary(bin_str: str, k: int) -> int:
    """
    Rotates a binary string k steps to the right and converts it to decimal.

    :param bin_str: The binary string (e.g., "1011")
    :param k: Number of rotation steps
    :return: Decimal value of the rotated binary string
    """
    n = len(bin_str)
    k = k % n  # handle cases where k > n
    rotated = bin_str[-k:] + bin_str[:-k]
    return int(rotated, 2)


# Example usage
if __name__ == "__main__":
    binary = "1011"
    steps = 2
    print(f"Original binary: {binary}")
    print(f"Rotated by {steps} steps → Decimal: {rotate_binary(binary, steps)}")

    # Another test
    print(rotate_binary("1101", 1))  # should give 11
    print(rotate_binary("1000", 3))  # should give 1
