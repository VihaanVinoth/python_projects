def approx_pi(n):
    denominator = 1
    numerator = 1
    den = 0
    total = 0


    for i in range(1, n + 1):
        num1 = i * 2
        num2 = (i + 1) * 2
        den = 2 * i + 1

        numerator *= num1 * num2
        denominator *= den ** 2

    total = 4 * (numerator / denominator)
    print("Approximation:", total)

approx_pi(int(input("Enter Product: ")))