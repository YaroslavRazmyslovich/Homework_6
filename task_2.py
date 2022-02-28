def fibonachi (num: int) -> int:
    if num == 1 or num ==2:
        return 1
    else:
        result = fibonachi (num - 1) + fibonachi (num - 2)
    return  result
        
print (fibonachi (14))