def knapsack(restaurantes, orcamento, felicidade, repeticoes):
    if len(restaurantes) == 0 or orcamento == 0:
        return [0, []]
    
    rest = restaurantes[-1]
    if rest["preco"] > orcamento:
        return knapsack(restaurantes[:-1], orcamento, felicidade, 1)
    
    else:
        pegou = knapsack(restaurantes, orcamento-rest["preco"], felicidade+(rest["felicidade"]/repeticoes), repeticoes+1)
        n_pegou = knapsack(restaurantes[:-1], orcamento, felicidade, 1)
        if pegou[0]+(rest["felicidade"]/repeticoes)>n_pegou[0]:
            return [pegou[0]+(rest["felicidade"]/repeticoes), pegou[1] +[rest["nome"]]]
        else:
            return n_pegou


def ler_csv(caminho):
    with open(caminho, "r") as fp:
        linha = fp.readlines()
    return linha

def processa(linhas):
    if len(linhas) == 0:
        return []
    dicionario = {}
    lista = linhas[-1][:-1].split(",")
    dicionario["nome"] = lista[0]
    dicionario["felicidade"] = int(lista[1])
    dicionario["preco"] = int(lista[2])
    return processa(linhas[:-1]) + [dicionario]



if __name__ == "__main__":
    restaurantes = processa(ler_csv(input("qual o caminho do arquivo: ")))
    orcamento = int(input("qual o orçamento disponível? "))
    print(knapsack(restaurantes, orcamento, 0, 1))
