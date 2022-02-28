def consat (*args: str, revers=False) -> str:
    if revers:
        args = reversed(args)
    result, *other = args
    for num in other:
        result += num
    return result

print (consat ('hello', ' ','world'))
print (consat ('hello', ' ','world', revers=True))

