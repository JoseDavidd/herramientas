import pide_un_numero
import config_listas
import elegir_lista

lista = elegir_lista.elegir_valor_aleatorio(config_listas.listas)

pide_numero = pide_un_numero.pide_un_numero()
print(pide_numero)

indice = elegir_lista.elegir_indice(lista)
print(f"elegir indice:{indice} pertenece al elemento {lista[indice]}")

indice_cpu = elegir_lista.elegir_indice_azar(lista)
print(f"indice cpu {indice_cpu}")

valor = elegir_lista.elegir_valor(lista)
print(f"elegir valor: {valor}")

valor_cpu = elegir_lista.elegir_valor_aleatorio(lista)
print(f"valor aleatorio es: {valor_cpu}")


#print(f"elegir indice:{elegir_lista.elegir_indice(lista)} pertenece al elemento: {elegir_lista.elegir_valor(lista)} ")

