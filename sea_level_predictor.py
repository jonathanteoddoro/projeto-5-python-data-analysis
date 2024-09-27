import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Lê os dados do arquivo CSV
    df = pd.read_csv('epa-sea-level.csv')

    # Cria o gráfico de dispersão (scatter plot)
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])  

    # Cria a primeira linha de melhor ajuste (tendência linear com base em todos os dados)
    slope, y_intercept, r, p, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])  # Calcula a regressão linear
    X = range(df['Year'].min(), 2051)
    y = [y_intercept + slope * x for x in X]
    plt.plot(X, y, 'r')  

    # Cria a segunda linha de melhor ajuste (apenas para os dados a partir de 2000)
    anos_maiores_que_2000 = df[df['Year'] >= 2000]  
    slope, y_intercept, r, p, std_err = linregress(anos_maiores_que_2000['Year'], anos_maiores_que_2000['CSIRO Adjusted Sea Level'])   
    X = range(anos_maiores_que_2000['Year'].min(), 2051)  
    y = [y_intercept + slope * x for x in X]  
    plt.plot(X, y, 'g')  

    # Adiciona rótulos aos eixos e título ao gráfico
    plt.xlabel("Year")  
    plt.ylabel("Sea Level (inches)")  
    plt.title("Rise in Sea Level")  
    
    
    plt.savefig('sea_level_plot.png')  
    return plt.gca()  
