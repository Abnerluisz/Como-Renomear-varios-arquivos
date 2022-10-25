import os #ela é uma biblioteca de comandos do sistema operacional que vai te auxiliar a fazer algumas operações dentro do seu computador


lugar_que_vai_ser_renomeado = 'C:\\Users\\Pasta\\Desktop\\Nova Pasta' # Variavel lugar de destino

path = os.chdir (lugar_que_vai_ser_renomeado)

lugarnome = os.listdir # é usado para obter a lista de todos os arquivos e diretórios no diretório especificado.
i = 0

for file in os.listdir(path): 
    new_file_name = "RENOMEARAQUI {}.png".format(i) # Só Renomear  ali RENOMEARAQUI .png(pode ser outro formato exemplo .doc)
    os.rename(file, new_file_name)
    i = i + 1

Numero_incial = 0
for file in os.listdir(path):
    print(file)
    Numero_incial += 1


print(f'\nTotal de arquivos {Numero_incial}\n\nTerminado\n')  #Printando os arquivos gerais renomeados e totalizando-os eles.
