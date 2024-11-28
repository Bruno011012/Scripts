import plotly.express as px
import plotly.graph_objects as go
from dash_amazon_estilos import dash_ama_esti_01
class Dahs_ama_graf_01():
    def __init__(self):
        self.estilos = dash_ama_esti_01()
        self.cores_personalizadas = ["#FF1493","#00FFFF","#FF0000", "#7CFC00", "#0000FF"]
        pass
    
    def grafico_01(self,t1):
        cores_personalizadas = self.cores_personalizadas
        grafico = go.Figure(data=[go.Pie(labels=t1["Category"], values=t1["Amount"],title="CATEGORIA",titlefont=dict(size=24, color="#00FFFF"),marker=dict(colors=cores_personalizadas,line=dict(color="#09fd83", width=3)),textfont=dict(size=14), hole=.5)])
        fig = self.estilos.estilo_01(grafico)
        return fig

    def grafico_02(self,t1):
        cores_personalizadas = self.cores_personalizadas
        grafico = go.Figure(data=[go.Pie(labels=t1["Courier Status"], values=t1["Amount"],title="Status",titlefont=dict(size=24, color="#00FFFF"),marker=dict(colors=cores_personalizadas,line=dict(color="#09fd83", width=3)),textfont=dict(size=14), hole=.5)])
        fig = self.estilos.estilo_02(grafico)
        return fig
    
    def grafico_03(self,t1):
        cores_personalizadas = self.cores_personalizadas
        grafico = px.bar(t1,x="Date",y="Amount",color="ship-service-level",text="ship-service-level",color_discrete_map=dict(zip(t1["ship-service-level"].unique(), cores_personalizadas)))
        fig = self.estilos.estilo_03(grafico)
        return fig
    
    def grafico_04(self,t1):
        cores_personalizadas = self.cores_personalizadas
        grafico = px.bar(t1,x="Date",y="Amount",color="Fulfilment",text="Fulfilment",color_discrete_map=dict(zip(t1["Fulfilment"].unique(), cores_personalizadas)))
        fig = self.estilos.estilo_04(grafico)
        return fig

    def grafico_05(self,t1):
        cores_personalizadas = self.cores_personalizadas
        categorias_unicas = t1['Status'].unique()
        color_map = {categoria: cores_personalizadas[i % len(cores_personalizadas)] for i, categoria in enumerate(categorias_unicas)}
        grafico = px.line(t1,x="Date",y="Amount",color="Status",text="Status",color_discrete_map=color_map)
        fig = self.estilos.estilo_05(grafico)
        return fig
    
    def grafico_06(self,t1):
        cores_personalizadas = self.cores_personalizadas
        categorias_unicas = t1['ship-state'].unique()
        color_map = {categoria: cores_personalizadas[i % len(cores_personalizadas)] for i, categoria in enumerate(categorias_unicas)}
        grafico = px.line(t1,x="Date",y="Amount",color="ship-state",text="ship-state",color_discrete_map=color_map)
        fig = self.estilos.estilo_06(grafico)
        return fig

    def grafico_07(self,t1):
        cores_personalizadas = self.cores_personalizadas
        grafico = px.bar(t1,x="Date",y="Amount",color="Size",text="Size",color_discrete_map=dict(zip(t1["Size"].unique(), cores_personalizadas)))
        fig = self.estilos.estilo_07(grafico)
        return fig
