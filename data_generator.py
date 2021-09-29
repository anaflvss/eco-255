import sys
import pandas as pd
import numpy as np

# Determina que os valores padrão para o número de anos seja 3 e o gerador aleatório seja 15.
n = int(sys.argv[1]) if len(sys.argv) > 1 else 3
random_seed = int(sys.argv[2]) if len(sys.argv) > 2 else 15


def create_data(n=n, cesta=["arroz", "feijão", "carne"]):

    """Gera dados aleatórios para o cálculo dos índices de Laspeyres, Paasche e Fisher.
    ---
    Args:
    n: int
        Número de anos para o qual os dados devem ser gerados. Os anos são gerados a partir de 2018.

    cesta: list
        Lista dos itens que devem fazer parte da cesta de produtos.
    """

    data = pd.DataFrame(columns=["ANO", "PRODUTO", "QUANTIDADE", "PRECO"])

    np.random.seed(random_seed)
    data["ANO"] = [x for x in range(2018, 2018 + n)] * len(cesta)
    data["PRODUTO"] = sorted(cesta * n)
    data["QUANTIDADE"] = sorted(np.random.randint(20, 40, size=n * len(cesta)))
    data["PRECO"] = sorted(np.random.randint(3, 20, size=n * len(cesta)))

    data.to_csv("dados_consumo.csv", index=False)


if __name__ == "__main__":
    create_data()
