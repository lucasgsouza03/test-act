class Contract(object):

    def __init__(self, id, debt) -> None:
        
        self.id = id
        self.debt = debt


def get_top_N_open_contracts(contracts, renegotiated, top_n):

    try:
        contracts = [contract for contract in contracts if contract.id not in renegotiated]

        sorted_contracts = sorted(contracts, key=lambda x: x.debt, reverse=True)[:top_n]

        return [contract.id for contract in sorted_contracts]
    
    except IndexError:
        raise BaseException('Quantidade de debtors solicitada maior que lista de debtors validos disponíveis!')

if __name__ == "__main__":

    contracts = [
        Contract(1, 1),
        Contract(2, 2),
        Contract(3, 3),
        Contract(4, 4),
        Contract(5, 5)
    ]
    renegotiated = [3]
    top_n = 3

    actual_open_contracts = get_top_N_open_contracts(contracts, renegotiated, top_n)

    expected_open_contracts = [5, 4, 2]
    assert expected_open_contracts == actual_open_contracts


    contracts = [
        Contract(1, 12),
        Contract(2, 5),
        Contract(3, 14),
        Contract(4, 40),
        Contract(5, 70),
        Contract(6, 7),
        Contract(7, 90),
        Contract(8, 10)
    ]
    renegotiated = [3, 4, 7]
    top_n = 5

    actual_open_contracts = get_top_N_open_contracts(contracts, renegotiated, top_n)

    expected_open_contracts = [5, 1, 8, 6, 2]
    assert expected_open_contracts == actual_open_contracts
