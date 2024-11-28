
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
from plotly import tools
from plotly.graph_objs import Figure, Bar
from plotly.subplots import make_subplots

class Dash_mercado_estilos_01():
    def __init__(self):
        pass

    def estilo_1(self,fig):
        cor_fundo = 'rgba(1, 49, 61, 0)'  
        fig.update_layout(
        plot_bgcolor="#214d56",  # Cor de fundo do gráfico
        paper_bgcolor=cor_fundo,   # Cor de fundo do gráfico
            xaxis=dict(title=""),  # Título do eixo x
            yaxis=dict(title=""),  # Título do eixo y
            font=dict(color='white'),
            width=350,
            height=265, # Cor dos rótulos dos eixos e título
            showlegend=False,
                     # Exibir legenda
        )
        fig.update_layout(
            margin=dict(l=0, r=0, t=0, b=0),
        )
        fig .update_traces(hoverinfo='label', textinfo='percent')
        return fig

    def estilo_2(self,fig):
        cor_fundo = 'rgba(1, 49, 61, 0)'  
        fig.update_layout(
        plot_bgcolor="#214d56",  # Cor de fundo do gráfico
        paper_bgcolor=cor_fundo,   # Cor de fundo do gráfico
            xaxis=dict(title=""),  # Título do eixo x
            yaxis=dict(title=""),  # Título do eixo y
            font=dict(color='white'),
            width=350,
            height=265, # Cor dos rótulos dos eixos e título
            showlegend=False,
                     # Exibir legenda
        )
        fig.update_layout(
            margin=dict(l=0, r=0, t=0, b=0),
        )
        fig .update_traces(hoverinfo='label', textinfo='percent')
        return fig
    
    def estilo_3(self,fig):
        cor_fundo = 'rgba(1, 49, 61, 0)'  
        fig.update_layout(
        plot_bgcolor=cor_fundo,  # Cor de fundo do gráfico
        paper_bgcolor=cor_fundo,  # Cor de fundo da área do gráfic 
        barnorm=None,
        bargap=0.08,
        bargroupgap=0.08  # Normalização das barras (pode ser 'percent', 'fraction', ou None)
        )
        fig.update_traces(  marker_line_color='#09fd83',  # Cor da borda das barras
                            marker_line_width=3  # Largura da borda das barras
        )
        fig.update_layout(
                xaxis_title=None,  # Título do eixo x
                yaxis_title=None, # Cor da grade e eixo x
                height=263,
                width=890,
                margin=dict(l=0, r=0, t=0, b=0),
                xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False)  # Cor dos rótulos no eixo y
        )
        fig.update_yaxes(showticklabels=False)
        fig.update_xaxes(showticklabels=False)
        fig.update_layout(showlegend=False)
        return fig

    def estilo_4(self,fig):
        g1 = fig
        g1.update_layout(
                xaxis_title=None,  # Título do eixo x
                yaxis_title=None,  # Título do eixo y
                xaxis_tickfont=dict(color='#09fd83', family='Arial, sans-serif',size=10),
                yaxis_tickfont=dict(color='#09fd83', family='Arial, sans-serif',size=10),
                height=263,
                width=982,
                xaxis=dict(showgrid=True, gridcolor='#09fd83'),
                yaxis=dict(showgrid=True, gridcolor='#09fd83'),
                margin=dict(l=0, r=0, t=0, b=0)
                # Cor dos rótulos no eixo y
            )
        g1.update_traces(line=dict(width=5,dash='solid'),
                              mode='lines+markers',
                              marker=dict(size=10, symbol='circle', color='#FFD700'))
        g1.update_layout(showlegend=False)
        return g1

    def estilo_5(self,fig):
        g1 = fig
        g1.update_layout(
                xaxis_title=None,  # Título do eixo x
                yaxis_title=None,  # Título do eixo y
                xaxis_tickfont=dict(color='#09fd83', family='Arial, sans-serif',size=10),
                yaxis_tickfont=dict(color='#09fd83', family='Arial, sans-serif',size=10),
                height=263,
                width=982,
                xaxis=dict(showgrid=True, gridcolor='#09fd83'),
                yaxis=dict(showgrid=True, gridcolor='#09fd83'),
                margin=dict(l=0, r=0, t=0, b=0)
                # Cor dos rótulos no eixo y
            )
        g1.update_traces(line=dict(width=5,dash='solid'),
                              mode='lines+markers',
                              marker=dict(size=10, symbol='circle', color='#FFD700'))
        g1.update_layout(showlegend=False)
        return g1
    
    def estilo_area(self):
            cor_fundo = 'rgba(1, 49, 61, 0)'  
            custom_template = {
            "layout": {
                "paper_bgcolor": cor_fundo,  # Cor de fundo do layout
                "plot_bgcolor": cor_fundo,  # Cor de fundo do gráfico
                "legend": {
                    "title": {
                        "font": {"color": "white"}  # Cor do título da legenda
                    },
                    "font": {"color": "white"}  # Cor do texto da legenda
                },
                "yaxis": {
                    "gridcolor": "white",  # Cor da grade do eixo y
                }
            }
            }
            return custom_template