input()
nombres = [int(elem) for elem in input().split()]

cost = 0
while len(nombres) > 1:
    # pop the two smalest numbers
    p = nombres.pop(nombres.index(min(nombres)))
    g = nombres.pop(nombres.index(min(nombres)))
    # insert the cost in the fisrt element of list
    nombres.insert(0, p + g)
    # add the cost of the operation to the total cost
    cost += nombres[0]
    
print(cost)