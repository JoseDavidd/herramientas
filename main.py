import pide_un_numero
import config_listas
import elegir_lista

lista = elegir_lista.elegir_valor_aleatorio(config_listas.listas)

print(pide_un_numero.pide_un_numero())
print(elegir_lista.elegir_valor_aleatorio(lista))
print(elegir_lista.elegir_indice(lista))
print(elegir_lista.elegir_valor(lista))
