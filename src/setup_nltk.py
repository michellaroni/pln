import os
import nltk

# Caminho absoluto para a pasta do projeto
caminho_projeto = r'C:\projetos\python\cefet\tcc\pln'

# Caminho fixo para salvar os dados do NLTK dentro do projeto
caminho_nltk = os.path.join(caminho_projeto, 'nltk_data')

# Atualiza os caminhos do NLTK para usar só esse diretório
nltk.data.path = [caminho_nltk]

# Confirma que o caminho foi ajustado
print(f"Diretório NLTK configurado para: {nltk.data.path}")
