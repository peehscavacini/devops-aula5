Python 3.5.4 (v3.5.4:3f56838, Aug  8 2017, 02:07:06) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Import jogovelha
import sys
erroInicializar = False
jogo = jogovelha.inicializar()
if len(jogo) != 3:
erroInicializar = True
else:
for linha in jogo:
if len(linha) != 3:
erroInicializar = True
else:
for elemento in linha:
if elemento != '.':
erroInicializar = True
if erroInicializar:
sys.exit(1)
else:
sys.exit(0)
