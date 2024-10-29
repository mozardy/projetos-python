def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida


# Teste com uma string qualquer
string_teste = str(input('Digite uma palavra: '))
print("Palavra invertida:", inverter_string(string_teste))
