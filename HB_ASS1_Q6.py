"""
multiplication table from 5 to 10
"""

for i in range(5, 11):
    print(f"Multiplication table for {i}:")
    for j in range(1, 11):
        result = i * j
        print(f"{i} x {j} = {result}")
    print()
