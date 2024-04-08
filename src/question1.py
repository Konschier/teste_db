class Contract:
    """Representa um contrato com um id único e um valor de divida"""

    def __init__(self, id, debt):
        """
        Inicializa um objeto Contract.

        Args:
            id (int): Id único do contrato
            debt (int): Valor de divida do contrato
        """
        self.id = id
        self.debt = debt

    def __str__(self):
        """
        Retorna uma representação em string do objeto Contract.

        Returns:
            str: Representaçao em string do objeto.
        """
        return 'id={}, debt={}'.format(self.id, self.debt)


class Contracts:
    """Representa uma coleção de contratos e fornece operações relacionadas aos contratos"""

    def get_top_n_open_contracts(self, open_contracts, renegotiated_contracts, top_n):
        """
        Obtém os N maiores devedores que ainda não possuem seus débitos renegociados.

        Args:
            open_contracts (list[Contract]): Uma lista em que cada elemento é uma instância de Contract.
            renegotiated_contracts (list[int]): Uma lista de numeros inteiros representando os identificadores dos associados que já renegociaram seus débitos.
            top_n (int): Um inteiro com a quantidade de devedores que devem ser retornados pelo método.

        Returns:
            list[int]: Uma lista com o id dos N maiores devedores.
        """
        open_contracts_not_renegotiated = [contract for contract in open_contracts if
                                           contract.id not in renegotiated_contracts]

        sorted_contracts = sorted(open_contracts_not_renegotiated, key=lambda x: x.debt, reverse=True)

        top_n_debtors = [contract.id for contract in sorted_contracts[:top_n]]

        return top_n_debtors
