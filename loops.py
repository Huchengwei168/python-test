print("--- Break & Continue ---")
i = 0
while i < 10:
    i += 1
    if i == 3:
        continue 
    if i == 8:
        break 
    print(i, end=" ")
print()

print("\n--- Range ---")
print("range(5):", list(range(5)))
print("range(2, 5):", list(range(2, 5)))
print("range(2, 8, 2):", list(range(2, 8, 2)))

print("\n--- Right-angled Triangle ---")
rows = int(input("Enter Number of Rows: "))
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()  

print("\n--- Prime Numbers 1-50 ---")
n = 50
for num in range(2, n + 1):
    is_prime = True
    for d in range(2, int(num ** 0.5) + 1):
        if num % d == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()