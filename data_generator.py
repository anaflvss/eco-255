import pandas as pd
import numpy as np


def create_data(n=3, cesta=["arroz", "feijão", "carne"]):

    """Gera dados aleatórios para o cálculo dos índices de Laspeyres, Paasche e Fisher.
    ---
    Args:
    n: int
        Número de anos para o qual os dados devem ser gerados. Os anos são gerados a partir de 2018.

    cesta: list
        Lista dos itens que devem fazer parte da cesta de produtos.
    """

    data = pd.DataFrame(columns=["ANO", "PRODUTO", "QUANTIDADE", "PRECO"])

    np.random.seed(15)
    data["ANO"] = [x for x in range(2018, 2018 + n)] * len(cesta)
    data["PRODUTO"] = sorted(cesta * n)
    data["QUANTIDADE"] = sorted(np.random.randint(20, 40, size=n * len(cesta)))
    data["PRECO"] = sorted(np.random.randint(3, 20, size=n * len(cesta)))

    data.to_csv("dados_consumo.csv", index=False)


if __name__ == "__main__":
    create_data()
