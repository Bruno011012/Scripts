import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os 
import numpy as np
from dash_vendaslo_estilos import Classe_dash_vendaloja_estil01
import pprint

class Classe_dash_vendaloja_graphs01():
    def __init__(self):
        self.estilos = Classe_dash_vendaloja_estil01()
        self.cores_personalizadas = ["#FFD700","#FF4500","#00FF00", "#00CED1", "#FF1493"]
        pass

    def grafico_01(self,frame):
        cores_personalizadas = self.cores_personalizadas
        grafico = go.Figure(data=[go.Pie(labels=frame["Ship Mode"], values=frame["Total"],title="CLASSE",titlefont=dict(size=24, color="white"),marker=dict(colors=cores_personalizadas,line=dict(color="white", width=3)),textfont=dict(size=14), hole=.5)])
        fig = self.estilos.estilo_01(grafico)
        return fig

    def grafico_02(self,frame):
        grafico = px.bar_polar(frame,r="Total",theta="Sub-Category",color="Sub-Category",color_discrete_sequence = px.colors.sequential.Plasma_r)
        grafico_01 = self.estilos.estilo_02(grafico)
        return grafico_01
    
    def grafico_03(self,frame):
        grafico = px.line_polar(frame,r="Total",theta="State",line_close=True)
        grafico.update_traces(fill="toself")
        grafico_01 = self.estilos.estilo_03(grafico)
        return grafico_01
    
    def grafico_04(self,frame):
        cores_personalizadas = self.cores_personalizadas
        grafico = go.Figure(data=[go.Pie(labels=frame["Region"], values=frame["Total"],title="CATEGORIA",titlefont=dict(size=24, color="white"),marker=dict(colors=cores_personalizadas,line=dict(color="white", width=3)),textfont=dict(size=14), hole=.5)])
        fig = self.estilos.estilo_04(grafico)
        return fig
    
    def grafico_05(self,dicionario):
        geojson_url = "https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json"
        fig = px.choropleth(
            locations=list(dicionario.keys()),  # Siglas dos estados
            geojson=geojson_url,  # GeoJSON dos estados dos EUA
            color=list(dicionario.values()),  # Valores associados
            color_continuous_scale=px.colors.sequential.Reds_r,  # Escala de cores
            title="Mapa dos Estados dos EUA (Gradiente Bluered)",
            locationmode="USA-states"  # Modo de localização para estados dos EUA
        )
        grafico = self.estilos.estilo_05(fig)
        return grafico
    
    def grafico_06(self,frame):
        cores_personalizadas = self.cores_personalizadas
        grafico = px.bar(frame,x="Order Date",y="Valores",color="Segment",color_discrete_map=dict(zip(frame["Segment"].unique(), cores_personalizadas)))
        fig = self.estilos.estilo_06(grafico)
        return fig
    
    def grafico_07(self,frame):
        cores_personalizadas = self.cores_personalizadas
        grafico_teste = px.area(
                frame,
                x="Order Date",
                y="Valores",
                color="Category",
                line_shape='linear',
                template=self.estilos.estilo_area(),
                color_discrete_sequence=cores_personalizadas
            )
        fig = self.estilos.estilo_07(grafico_teste)
        return fig