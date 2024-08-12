# 5)Faça um programa que gere as tabuadas do 1 até o 10.

for x in range(1, 11):
    print(f"Tabuada do {x}:")
    for y in range(1, 11):
        print(f"{x} x {y} = {x * y}")
    print("--------------------" ) 