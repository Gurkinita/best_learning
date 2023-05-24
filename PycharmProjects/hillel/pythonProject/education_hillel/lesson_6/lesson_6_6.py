def sum_range(start, end):
    if start > end:
        start, end = end, start
    total = 0
    for num in range(start, end + 1):
        total += num
    return total

start = int(input("Input the start number: "))
end = int(input("Input the end number: "))
result = sum_range(start, end)
print("Sum:", result)
