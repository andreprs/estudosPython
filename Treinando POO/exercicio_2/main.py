import ingresso
import ingresso_vip

ingresso_1 = ingresso.Ingresso(50)
ingresso_2 = ingresso_vip.IngressoVip(50, 20)

print('O ingresso normal custa: R$', end='')
ingresso_1.imprimir_valor()

print('O ingresso VIP custa: R$', end='')
ingresso_2.imprimir_valor()
