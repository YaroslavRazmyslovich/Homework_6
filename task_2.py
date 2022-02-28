def fibonachi (num: int) -> int:
    if num == 1 or num ==2:
        return 1
    else:
        result = fibonachi (num - 1) + fibonachi (num - 2)
    return  result
        
print (fibonachi (14))

def fibonachi_2 (num: int) -> int:
    row = [1, 1]
    if num == 1 or num ==2:
        return 1
    else:
        for item in range (num - 2):
            row[0], row[1] = row[1], row[0] + row[1]
    return row[1]

print (fibonachi_2 (14))