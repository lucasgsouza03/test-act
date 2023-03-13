class Orders(object):

    def combine_orders(self, orders, n_max):
        expected_orders = 0
        return self.calc_order(orders, expected_orders, n_max)

    def calc_order(self, orders, expected_orders, n_max):
        
        sum = orders.pop(0) 
        expected_orders += 1
        for idx, order in enumerate(orders):
            if sum + order > n_max:
                continue
            else:
                orders.pop(idx)
                break
        
        if len(orders):
            return self.calc_order(orders, expected_orders, n_max)
        else:
            return expected_orders
        
if __name__ == "__main__":
    orders = [70, 30, 10]
    n_max = 100
    expected_orders = 2

    how_many = Orders().combine_orders(orders, n_max)

    assert how_many == expected_orders

    orders = [70, 30, 10, 50, 30]
    n_max = 70
    expected_orders = 4

    how_many = Orders().combine_orders(orders, n_max)

    assert how_many == expected_orders

