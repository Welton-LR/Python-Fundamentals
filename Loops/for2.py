# Aqui usamos a instrução "continue" para pular um elemento
# na iteração

pedras = ("esmeralda","diamante","rubi","quartzo","safira")

for pedra in pedras:
    if pedra == "quartzo":
        continue
    print(pedra)
    