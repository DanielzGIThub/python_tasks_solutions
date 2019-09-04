from decimal import Decimal

start = 2
end = 5.5
interval = 0.5
rlist=[]

def dec_list(num1, num2, inter): 
    i = Decimal(num1)
    while i < num2:
        i += Decimal(inter)
        rlist.append(i)
    return rlist

print(dec_list(start, end, interval))

    