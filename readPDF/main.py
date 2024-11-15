import pdfplumber
import pandas as pd
import camelot

path_pdf = "./readPDF/resultado-atualizado.pdf"
data = []

# ler pdf
with pdfplumber.open(path_pdf) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        data.append(text)

print(data)

# exportar para excel

# Suponha que 'data' seja uma lista de textos ou tabelas que você extraiu do PDF.
# Aqui, estamos criando um DataFrame de exemplo para exportar.
df = pd.DataFrame(data, columns=["Texto da Página"])  # Ajuste conforme necessário

# Para Excel
df.to_excel("output.xlsx", index=False)

# tabelas no pdf
tables = camelot.read_pdf(path_pdf, pages="all")
for i, table in enumerate(tables):
    table.to_excel(f"table_{i}.csv")  # Salva cada tabela em um arquivo excel