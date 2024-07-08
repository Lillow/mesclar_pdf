from PyPDF2 import PdfMerger
from os import listdir

def mesclar_pdf():
    merger = PdfMerger() # Criar objeto mesclador
    lista_arquivos = listdir('arquivos_entrada') # Listar arquivos no diretório de entrada
    lista_arquivos.sort() # Ordenar arquivos

    try:
        for arquivo in lista_arquivos:
            if arquivo.endswith('.pdf'):  # Verificar se o arquivo é PDF
                merger.append(f'arquivos_entrada/{arquivo}')  # Adicionar arquivo ao mesclador
        merger.write('arquivos_saida/arquivo_final.pdf')  # Salvar arquivo mesclado
        print('Arquivos mesclados com sucesso.')
    except Exception as e:
        print(f'Ocorreu um erro ao mesclar os arquivos PDF: {str(e)}')
    finally:
        merger.close()  # Fechar o objeto mesclador

mesclar_pdf()  # Chamar a função principal
