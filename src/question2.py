class Orders:

    """
    Classe para combinar requisições de agencias de carros-forte.
    """
    @staticmethod
    def combine_orders(requests, n_max):
        """
        Calcula o número minimo de viagens necessárias para levar o dinheiro para as agencias.
        Args:
        requests (list): Lista de inteiros, representando o valor monetário requisitado por uma agência.
        n_max (int): O valor máximo que pode ser levado em uma única viagem.

        Returns:
            int: O número minimo de viagens necessárias para levar o dinheiro para as agencias.
        """

        requests.sort(reverse=True)

        num_trips = 0
        remaining_requests = requests.copy()

        while remaining_requests:
            current_trip_total = remaining_requests.pop(0)

            for request in remaining_requests:
                if current_trip_total + request <= n_max:
                    remaining_requests.remove(request)
                    break

            num_trips += 1

        return num_trips
