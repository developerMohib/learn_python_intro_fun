def filledOrders(order, k):
    order.sort()
    fulfilledOrder = 0
    for getOrder in order:
        if getOrder <= k:
            k = k - getOrder
            fulfilledOrder = fulfilledOrder + 1
        else:
            break

    return fulfilledOrder


order = [5, 3, 7, 9, 4]
k = 20
print(filledOrders(order, k))
