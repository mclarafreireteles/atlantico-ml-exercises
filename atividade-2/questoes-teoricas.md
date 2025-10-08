## 6. Como identificar e tratar outliers em uma coluna numérica usando desvio padrão ou quartis? 
- Desvio padrão:
Primeiro passo: calcular a média e o desvio padrão da coluna.Depois, definir um limite, por exemplo, valores fora do intervalo [μ - 3σ, μ + 3σ] são considerados outliers. Exemplo em python: 
```python
import pandas as pd

df = pd.DataFrame({'valor': [10, 12, 13, 11, 100, 12, 13, 11, 10]})

media = df['valor'].mean()
desvio = df['valor'].std()

limite_inferior = media - 3 * desvio
limite_superior = media + 3 * desvio

outliers = df[(df['valor'] < limite_inferior) | (df['valor'] > limite_superior)]

print("Outliers encontrados:\n", outliers)
```

- Quartis:
1. Calcular:
   - Q1: 1º quartil (25%)
   - Q3: 3º quartil (75%)
   - IQR = Q3 - Q1

2. Definir limites:
   - Inferior: Q1 - 1.5 * IQR
   - Superior: Q3 + 1.5 * IQR

3. Valores fora desse intervalo são considerados outliers.
Exemplo em python:
```python
Q1 = df['valor'].quantile(0.25)
Q3 = df['valor'].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers = df[(df['valor'] < limite_inferior) | (df['valor'] > limite_superior)]

print("Outliers encontrados:\n", outliers)
```

### Tratamento dos outliers:
As opções mais comuns:
- Remover (se for erro evidente ou valor absurdo)

- Substituir por:
Média ou mediana da coluna

- Manter (se for um valor válido e representativo, como vendas muito altas em uma data especial)

## 7. Como concatenar vários DataFrames (empilhando linhas ou colunas), mesmo que tenham colunas diferentes? Dica: Utiliza-se pd.concat() especificando axis=0 (linhas) ou axis=1 (colunas). Quando há colunas diferentes, os valores ausentes são preenchidos com NaN. 

oÉ possível concatenar múltiplos DataFrames usando `pd.concat()`, seja empilhando linhas ou colunas, mesmo que tenham colunas diferentes.

### Concatenar por **linhas** (axis=0)

- Cada DataFrame é empilhado verticalmente.
- Colunas ausentes em algum DataFrame serão preenchidas com `NaN`.

```python
import pandas as pd

df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'B': [5, 6], 'C': [7, 8]})

df_concat = pd.concat([df1, df2], axis=0, ignore_index=True)
print(df_concat)
```

### Concatenar por colunas (axis=1)
- Cada DataFrame é combinado lado a lado.
- Índices que não existem em algum DataFrame terão NaN.

```python
import pandas as pd

df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'B': [5, 6], 'C': [7, 8]})

df_concat_col = pd.concat([df1, df2], axis=1)
print(df_concat_col)
```

## 8. Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas? 


```python
import pandas as pd

# Leitura do arquivo CSV
df = pd.read_csv('dados.csv')

# Exibir as primeiras linhas
print(df.head())
```


## 9. Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição?
```python
import pandas as pd

df = pd.DataFrame({
    'Nome': ['Ana', 'Bruno', 'Carla', 'Daniel'],
    'Idade': [23, 35, 29, 40],
    'Cidade': ['SP', 'RJ', 'SP', 'MG']
})

idades = df['Idade']
print("Coluna Idade:\n", idades)

filtro = df[df['Idade'] > 30]
print("\nLinhas com Idade > 30:\n", filtro)
```
## 10. Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?
```python
import pandas as pd
import numpy as np

# Exemplo de DataFrame com valores ausentes
df = pd.DataFrame({
    'Nome': ['Ana', 'Bruno', 'Carla', 'Daniel'],
    'Idade': [23, np.nan, 29, 40],
    'Cidade': ['SP', 'RJ', None, 'MG']
})

# 1️⃣ Identificar valores ausentes
print(df.isna())         # Mostra True onde há NaN
print(df.isna().sum())   # Contagem de NaN por coluna

# 2️⃣ Remover linhas com NaN
df_sem_nan = df.dropna()
print(df_sem_nan)

# 3️⃣ Substituir valores ausentes por um valor específico
df_preenchido = df.fillna({'Idade': df['Idade'].mean(), 'Cidade': 'Desconhecida'})
print(df_preenchido)
```


