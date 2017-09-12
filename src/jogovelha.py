Python 3.5.4 (v3.5.4:3f56838, Aug  8 2017, 02:07:06) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def inicializar():
tab = [ ]
for i in range(3):
linha = [ ]
for j in range(3):
linha.append(".")
tab.append(linha)
return tab
def main( ):
jogo = inicializar( )
print (jogo)
if __name__ == "__main__":
main()
