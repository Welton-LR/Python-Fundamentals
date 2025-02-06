# Adicionando elemento em uma lista

# Ao final da lista
olimpianos = ["Zeus","Posseidon","Hera"]

print(olimpianos)
print(len(olimpianos)) # Verificando o tamanho da lista
olimpianos.append("Afrodite") # Adicionando um novo elemento à lista
print(olimpianos)
print(len(olimpianos))

# Adicionando elemento em qualquer lugar da lista
olimpianos.insert(2,"Hermes")
print(olimpianos)
print(len(olimpianos))

print("Todos reunidos no Monte Olimpo!")