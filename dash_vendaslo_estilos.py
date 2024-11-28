import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

class Classe_dash_vendaloja_estil01():
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
            width=400,
            height=300, # Cor dos rótulos dos eixos e título
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
        # Estilizando o layout
        fig.update_layout(
            plot_bgcolor="#003198",  # Cor de fundo do gráfico
            paper_bgcolor=cor_fundo,  # Cor de fundo da área externa
            font=dict(color='white',size=14),  # Cor do texto
            width=400,  # Largura do gráfico
            height=300,  # Altura do gráfico
            showlegend=False,  # Oculta a legenda
            margin=dict(l=0, r=0, t=18, b=18),  # Reduz as margens
            polar=dict(
            radialaxis=dict(
                tickfont=dict(color='black')  # Cor dos rótulos do eixo radial
            )
        )
        )

        return fig
    
    def estilo_03(self,fig):
        cor_fundo = 'rgba(1, 49, 61, 0)'
        # Estilizando o layout
        fig.update_layout(
            plot_bgcolor="#003198",  # Cor de fundo do gráfico
            paper_bgcolor=cor_fundo,  # Cor de fundo da área externa do gráfico
            font=dict(color='white',size=14),  # Cor do texto
            width=400,  # Largura do gráfico
            height=300,  # Altura do gráfico
            showlegend=False,  # Oculta a legenda
            margin=dict(l=0, r=0, t=18, b=18),  # Reduz as margens
            polar=dict(
            radialaxis=dict(
                tickfont=dict(color='black')  # Cor dos rótulos do eixo radial
            )
        )
        )

        return fig
    
    def estilo_04(self,fig):
        cor_fundo = 'rgba(1, 49, 61, 0)'  
        fig.update_layout(
        plot_bgcolor="#214d56",  # Cor de fundo do gráfico
        paper_bgcolor=cor_fundo,   # Cor de fundo do gráfico
            xaxis=dict(title=""),  # Título do eixo x
            yaxis=dict(title=""),  # Título do eixo y
            font=dict(color='white'),
            width=400,
            height=300, # Cor dos rótulos dos eixos e título
            showlegend=False,
                     # Exibir legenda
        )
        fig.update_layout(
            margin=dict(l=0, r=0, t=0, b=0),
        )
        fig .update_traces(hoverinfo='label', textinfo='percent')
        return fig
    
    def estilo_05(self,fig):
        cor_fundo = 'rgba(1, 49, 61, 0)' 
        fig.update_geos(
                landcolor="#FF8C00",  # Cor da área de terra
                oceancolor="LightBlue",  # Cor da área oceânica
                showocean=True,  # Mostrar a área oceânica
                lakecolor="Blue",  # Cor da área de lagos
                showland=True,  # Mostrar a área de terra,
                showcoastlines = True,
                coastlinecolor = "red",
                showlakes = True ,
                showrivers = True ,
                rivercolor = "Blue",
                projection_type="equirectangular",
            )
            # Ajustar o layout do gráfico, incluindo a cor de fundo azul
        fig.update_layout(
                plot_bgcolor="#01313d",  # Substitua pelo código da cor desejada
                paper_bgcolor=cor_fundo,  # Substitua pelo código da cor desejada # Substitua pelo código da cor desejada
                width=1070,
                height=580,
                title="Receita Estados EUA",
                font=dict(
                    color="black",  # Cor do texto
                    family="Arial, sans-serif",  # Estilo da fonte
                    size=14,  # Tamanho da fonte
                ),
                
            )
        fig.update_layout(
                margin=dict(l=0, r=0, t=0, b=0), 
                title=dict(y=0.86), # Ajuste os valores conforme necessário
            )
        fig.update_layout(coloraxis_colorbar=dict(title="", tickvals=[], ticktext=[]), coloraxis_colorbar_thickness=0)
        return fig
    
    def estilo_06(self,fig):
        cor_fundo = 'rgba(1, 49, 61, 0)'  
        fig.update_layout(
        plot_bgcolor=cor_fundo,  # Cor de fundo do gráfico
        paper_bgcolor=cor_fundo,  # Cor de fundo da área do gráfic 
        barnorm=None,
        bargap=0.08,
        bargroupgap=0.08  # Normalização das barras (pode ser 'percent', 'fraction', ou None)
        )
        fig.update_traces(  marker_line_color='white',  # Cor da borda das barras
                            marker_line_width=2  # Largura da borda das barras
        )
        fig.update_layout(
                xaxis_title=None,  # Título do eixo x
                yaxis_title=None, # Cor da grade e eixo x
                height=250,
                width=900,
                margin=dict(l=0, r=0, t=0, b=0),
                xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False)  # Cor dos rótulos no eixo y
        )
        fig.update_yaxes(showticklabels=False)
        fig.update_xaxes(showticklabels=False)
        fig.update_layout(showlegend=False)
        return fig
    
    def estilo_07(self,fig):
        g1 = fig
        g1.update_layout(
                xaxis_title=None,  # Título do eixo x
                yaxis_title=None,  # Título do eixo y
                xaxis_tickfont=dict(color='#09fd83', family='Arial, sans-serif',size=10),
                yaxis_tickfont=dict(color='#09fd83', family='Arial, sans-serif',size=10),
                height=250,
                width=900,
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