
def discounted(price, discount, max_discount=20):        
    catcher = []
    test_int = [price, discount, max_discount]
    for val in range(len(test_int)):
        try:
            int(test_int[val])        
        except ValueError:
            catcher.append(test_int[val])
    else:
        if len(catcher) == 0:
            price = abs(float(price))
            discount = abs(float(discount))
            max_discount = abs(float(max_discount))
            if max_discount > 99:
                raise ValueError('Слишком большая максимальная скидка')
            if discount >= max_discount:
                return price
            else:
                return price - (price * discount / 100)
        else:
            raise ValueError("Некоторые переменные не являются строкой:\n"  + " ".join(map(str, catcher)))


discounted("10000", "six", "five")


