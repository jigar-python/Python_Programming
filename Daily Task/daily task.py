
even=0
odd=0

for i in range(1,10):
    number=int(input(f"enter the number {i} :"))
    if (number%2) == 0:
        even += 1
    else:
        odd += 1
print("even number is",even)
print("odd number is",odd)

    
