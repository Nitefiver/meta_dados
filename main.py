from pathlib import Path
from datetime import datetime

# Selecionando o arquivo no diretório data
path = Path('data', 'teste.txt')

# Coletando a data que o arquivo foi criado
stats = path.stat()
second_created = stats.st_birthtime

# Deixando a data mais legível
date_created = datetime.fromtimestamp(second_created)
# Formato em que a data e hora irão aparecer
date_created_str = date_created.strftime("%Y-%m-%d_%H_%M_%S")

print(date_created_str)

# Output:
# 2024-05-02_12_16_56
