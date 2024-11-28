import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
from plotly import tools
from plotly.graph_objs import Figure, Bar
from plotly.subplots import make_subplots

class dash_ama_esti_01():
    def __init__(self):
        pass
    
    def estilo_01(self,fig):
        cor_fundo = 'rgba(1, 49, 61, 0)'  
        fig.update_layout(
        plot_bgcolor="#214d56",  # Cor de fundo do gráfico
        paper_bgcolor=cor_fundo,   # Cor de fundo do gráfico
            xaxis=dict(title=""),  # Título do eixo x
            yaxis=dict(title=""),  # Título do eixo y
            font=dict(color='white'),
            width=320,
            height=220, # Cor dos rótulos dos eixos e título
            showlegend=False,
                     # Exibir legenda
        )
        fig.update_layout(
            margin=dict(l=0, r=0, t=0, b=0),
        )
        fig .update_traces(hoverinfo='label', textinfo='percent')
        return fig

    def estilo_02(self,fig):
        cor_fundo = 'rgba(1, 49, 61, 0)'  
        fig.update_layout(
        plot_bgcolor="#214d56",  # Cor de fundo do gráfico
        paper_bgcolor=cor_fundo,   # Cor de fundo do gráfico
            xaxis=dict(title=""),  # Título do eixo x
            yaxis=dict(title=""),  # Título do eixo y
            font=dict(color='white'),
            width=320,
            height=220, # Cor dos rótulos dos eixos e título
            showlegend=False,
                     # Exibir legenda
        )
        fig.update_layout(
            margin=dict(l=0, r=0, t=0, b=0),
        )
        fig .update_traces(hoverinfo='label', textinfo='percent')
        return fig

    def estilo_03(self,fig):
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
                height=220,
                width=635,
                margin=dict(l=0, r=0, t=0, b=0),
                xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False)  # Cor dos rótulos no eixo y
        )
        fig.update_yaxes(showticklabels=False)
        fig.update_xaxes(showticklabels=False)
        fig.update_layout(showlegend=False)
        return fig
    
    def estilo_04(self,fig):
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
                height=220,
                width=635,
                margin=dict(l=0, r=0, t=0, b=0),
                xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False)  # Cor dos rótulos no eixo y
        )
        fig.update_yaxes(showticklabels=False)
        fig.update_xaxes(showticklabels=False)
        fig.update_layout(showlegend=False)
        return fig
    
    def estilo_05(self,fig):
        cor_fundo = 'rgba(1, 49, 61, 0)'  
        fig.update_layout(
        xaxis=dict(showgrid=True, gridcolor='#09fd83'),
        yaxis=dict(showgrid=True, gridcolor='#09fd83'),
        plot_bgcolor=cor_fundo,  # Cor de fundo do gráfico
        paper_bgcolor=cor_fundo,  # Cor de fundo da área do gráfico
        bargap=0.2,  # Espaçamento entre as barras
        barnorm=None,  # Normalização das barras (pode ser 'percent', 'fraction', ou None)
        )
        fig.update_layout(
                    xaxis_title=None,  # Título do eixo x
                    yaxis_title=None,
                    xaxis_tickfont=dict(color='#fbc90b', family='Arial, sans-serif',size=10),
                    yaxis_tickfont=dict(color='#fbc90b', family='Arial, sans-serif',size=14),  # Cor da grade e eixo 
                    height=198,
                    width=978,
                    margin=dict(l=30, r=0, t=0, b=30) # Cor dos rótulos no eixo y
        )
        fig.update_traces(line=dict( width=5,dash='solid'),
                                mode='lines+markers',
                                marker=dict(size=13, symbol='circle', color="#008000",line=dict(color='#09fd83', width=3)))
        fig.update_layout(showlegend=False)
        return fig

    def estilo_06(self,fig):
        cor_fundo = 'rgba(1, 49, 61, 0)'  
        fig.update_layout(
        xaxis=dict(showgrid=True, gridcolor='#09fd83'),
        yaxis=dict(showgrid=True, gridcolor='#09fd83'),
        plot_bgcolor=cor_fundo,  # Cor de fundo do gráfico
        paper_bgcolor=cor_fundo,  # Cor de fundo da área do gráfico
        bargap=0.2,  # Espaçamento entre as barras
        barnorm=None,  # Normalização das barras (pode ser 'percent', 'fraction', ou None)
        )
        fig.update_layout(
                    xaxis_title=None,  # Título do eixo x
                    yaxis_title=None,
                    xaxis_tickfont=dict(color='#fbc90b', family='Arial, sans-serif',size=10),
                    yaxis_tickfont=dict(color='#fbc90b', family='Arial, sans-serif',size=14),  # Cor da grade e eixo 
                    height=198,
                    width=978,
                    margin=dict(l=30, r=0, t=0, b=30) # Cor dos rótulos no eixo y
        )
        fig.update_traces(line=dict( width=5,dash='solid'),
                                mode='lines+markers',
                                marker=dict(size=13, symbol='circle', color="#008000",line=dict(color='#09fd83', width=3)))
        fig.update_layout(showlegend=False)
        return fig
    
    def estilo_07(self,fig):
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
                height=250,
                width=1880,
                margin=dict(l=0, r=0, t=0, b=0),
                xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False)  # Cor dos rótulos no eixo y
        )
        fig.update_yaxes(showticklabels=False)
        fig.update_xaxes(showticklabels=False)
        fig.update_layout(showlegend=False)
        return fig