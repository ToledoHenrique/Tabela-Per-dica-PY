from func import carregartabela, procurar, verificaElemento

resposta = input("""

████████╗░█████╗░██████╗░███████╗██╗░░░░░░█████╗░
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║░░░░░██╔══██╗
░░░██║░░░███████║██████╦╝█████╗░░██║░░░░░███████║
░░░██║░░░██╔══██║██╔══██╗██╔══╝░░██║░░░░░██╔══██║
░░░██║░░░██║░░██║██████╦╝███████╗███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝╚═╝░░╚═╝

██████╗░███████╗██████╗░██╗░█████╗░██████╗░██╗░█████╗░░█████╗░
██╔══██╗██╔════╝██╔══██╗██║██╔══██╗██╔══██╗██║██╔══██╗██╔══██╗
██████╔╝█████╗░░██████╔╝██║██║░░██║██║░░██║██║██║░░╚═╝███████║
██╔═══╝░██╔══╝░░██╔══██╗██║██║░░██║██║░░██║██║██║░░██╗██╔══██║
██║░░░░░███████╗██║░░██║██║╚█████╔╝██████╔╝██║╚█████╔╝██║░░██║
╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═╝░╚════╝░╚═════╝░╚═╝░╚════╝░╚═╝░░╚═╝

By: Carlos Eduardo Piva  &  Henrique da Costa Toledo

          Menu - escolha uma opção: 
[1] - Para listagem de elementos da Tabela Periódica. 
[2] - Para procurar todas as informações relacionadas aquele elemento. 
[3] - Para Procurar alguma informação especifica do elemento.
 \n""")

if resposta == '1':
    carregartabela()
elif resposta == '2':
    procurar()
elif resposta == '3':
    verificaElemento()