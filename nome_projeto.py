from carregar_arquivo_versao_02 import carregar_e_exibir_csv

# Chama a interface gráfica e retorna o DataFrame
df = carregar_e_exibir_csv()

# Verifica o conteúdo do DataFrame
if df is not None:
    print("Dados carregados com sucesso!")
else:
    print("Nenhum arquivo foi carregado.")
