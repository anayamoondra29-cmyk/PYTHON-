start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

squares = []
even_squares = []
odd_squares = []

for num in range(start, end + 1):
    sq = num ** 2   
    if sq % 2 == 0:
        even_squares.append(sq)
    else:
        odd_squares.append(sq)

print("All square values:", squares)
print("Even square values:", even_squares)
print("Odd square values:", odd_squares)