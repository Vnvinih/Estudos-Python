arquivo = open('arText.txt', 'w')

arquivo.write('Curso Python \n')
arquivo.write('Aula Prática')
arquivo.close()

#Leitura do arquivo texto

leitura = open('arText.txt', 'r')
print(leitura.read())
leitura.close()