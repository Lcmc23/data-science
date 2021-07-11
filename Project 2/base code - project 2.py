import pandas as pd
import plotly.express as px # Install this package with 'pip install plotly'

# Step 1: Import the database
tabela = pd.read_csv("telecom_users.csv")
display(tabela)

# Step 2
# 'Unnamed' column is useless -> delete!
tabela = tabela.drop("Unnamed: 0", axis=1)
display(tabela)

# Columns with numeric characteristic being treated as text
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
# Empty value (NaN) in Code column
# Completely empty columns
tabela = tabela.dropna(how="all", axis=1)
# empty lines
tabela = tabela.dropna(how="any", axis=0)
print(tabela.info())

# Step 3 - How are our cancellations?
display(tabela["Churn"].value_counts())
display(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

# Step 4

for coluna in tabela:
    grafico = px.histogram(tabela, x=coluna, color="Churn")
    grafico.show()
