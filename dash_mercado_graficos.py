import plotly.express as px
import plotly.graph_objects as go
from dash_mercado_estilos import Dash_mercado_estilos_01
class Dahs_mercado_graficos_01():
    def __init__(self):
        self.estilos = Dash_mercado_estilos_01()
 

    def grafico_1(self,t1):
        cores_personalizadas = ["#0000FF", "#00BFFF", "#191970", "#6959CD", "#2F4F4F"]
        grafico = go.Figure(data=[go.Pie(labels=t1["Gender"], values=t1["price"],title="SEXO",titlefont=dict(size=24, color="white"),marker=dict(colors=cores_personalizadas,line=dict(color="#09fd83", width=3)),textfont=dict(size=16), hole=.5)])
        fig = self.estilos.estilo_1(grafico)
        return fig
    
    def grafico_2(self,t1):
        cores_personalizadas = ["#0000FF", "#00BFFF", "#191970", "#6959CD", "#2F4F4F"]
        grafico = go.Figure(data=[go.Pie(labels=t1["Branch"], values=t1["price"],title="TIPO",titlefont=dict(size=24, color="white"),marker=dict(colors=cores_personalizadas,line=dict(color="#09fd83", width=3)),textfont=dict(size=16), hole=.5)])
        fig = self.estilos.estilo_2(grafico)
        return fig
    
    def grafico_3(self,t1):
        cores_personalizadas = ["#0000FF", "#00BFFF", "#191970", "#6959CD", "#2F4F4F"]
        grafico = px.bar(t1,x="Date",y="Unit price",color="Payment",text="Payment",color_discrete_map=dict(zip(t1["Payment"].unique(), cores_personalizadas)))
        fig = self.estilos.estilo_3(grafico)
        return fig
    
    def grafico_4(self,t1):
        cores_personalizadas = ["#0000FF", "#00BFFF", "#191970", "#6959CD", "#2F4F4F"]
        grafico_teste = px.area(
                t1,
                x="Date",
                y="Unit price",
                color="Product line",
                line_shape='linear',
                template=self.estilos.estilo_area(),
                color_discrete_sequence=cores_personalizadas
            )
        fig = self.estilos.estilo_4(grafico_teste)
        return fig

    def grafico_5(self,t1):
        cores_personalizadas = ["#0000FF", "#00BFFF", "#191970", "#6959CD", "#2F4F4F"]
        grafico_teste = px.area(
                t1,
                x="Date",
                y="Unit price",
                color="City",
                line_shape='linear',
                template=self.estilos.estilo_area(),
                color_discrete_sequence=cores_personalizadas
            )
        fig = self.estilos.estilo_5(grafico_teste)
        return fig
    