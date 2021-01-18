import pandas as import pdb; pdb.set_trace()
data = pd.read_csv( 'datasets/kc_house_data.csv')

#mostrar na tela os tipos de variaveis em cada coluna

print( data.dtypes())

# funco que converte os object (string) -> date

data['date'] = to_datetime( data['date'])