from dash import Dash,html,dcc,callback_context
import dash_bootstrap_components as dbc 
import pandas as pd
import os
import numpy as np
from datetime import datetime,date,timedelta
from dash_vendaslo_contas import Classe_dash_vendaloja_conta01
from dash.dependencies import Input,Output,State
import webbrowser

class Classe_vendaloja_html01():
    def __init__(self):
        self.contador_chome = 0
        self.cor_card = "rgba(0,90,255,0.5)"
        self.linha_card = "5px"
        self.cor_linha_c = "white"
        self.margin = "4px"
        self.padding = "3px"
        self.raio_borda = "20px"
        self.cor_sombra = "#21a9af"
        self.contas = Classe_dash_vendaloja_conta01()
        self.graph_01 = self.contas.conta_01("02/01/2020","01/06/2022")
        self.graph_02 = self.contas.conta_02("02/01/2020","01/06/2022")
        self.graph_03 = self.contas.conta_03("02/01/2020","01/06/2022")
        self.graph_04 = self.contas.conta_04("02/01/2020","01/06/2022")
        self.graph_05 = self.contas.conta_05()
        self.graph_06 = self.contas.conta_06("02/01/2020","15/02/2020")
        self.graph_07 = self.contas.conta_07("02/01/2020","15/02/2020")
        self.inicio_01()
        self.layout_01()
        self.define_calback()
        self.navegador()
        self.final_01()
    
    def inicio_01(self):
        self.app = Dash(__name__)
    
    def layout_01(self):
        self.app.layout = html.Div(children=[
            html.Div(children=[
                dbc.Card(children=[
                    html.Div(children=[
                        html.A(
                    html.Img(src="https://github.com/Bruno011012/graficos/blob/main/garrafinha.gif?raw=true", alt="GIF"),
                    style={"width":"42px","height":"42px","margin":"4px","padding":"3px"}
                    ),
                    html.H2(children="DASHBOARD LOJA E-COMMERCE",style={"font-size":"24px","color":"white","textShadow":"2px 2px 2px black","margin":"2px","padding":"2px"})
                    ],style={"display":"flex","flexDirection":"row"}),
                      dcc.DatePickerRange(
                    id='date-picker-range',
                    start_date=date(2020, 1, 2),
                    end_date=date(2023, 12, 30),
                    end_date_placeholder_text='Select a date!',
                    style={
                        'background-color': 'blue',
                        'color': 'darkblue',
                        'border': '3px solid white',
                        'border-radius': '5px',
                        "width": "290px", 
                        "height": "50px"

                    }
                ),
                 html.H2(id="datatx-1",children="SELEÇÃO DE DATAS",style={"font-size":"24px","color":"white","textShadow":"2px 2px 2px black","margin":"2px","padding":"2px"}),
                 html.Div(children=[
                     html.A(
                    html.Img(src="https://github.com/Bruno011012/graficos/blob/main/rashtag.gif?raw=true", alt="GIF"),
                    style={"width":"72px","height":"72px","margin":"4px","padding":"3px"}
                    ),
                    html.A(
                    html.Img(src="https://github.com/Bruno011012/graficos/blob/main/rashtag.gif?raw=true", alt="GIF"),
                    style={"width":"72px","height":"72px","margin":"4px","padding":"3px"}
                    ),
                    html.A(
                    html.Img(src="https://github.com/Bruno011012/graficos/blob/main/rashtag.gif?raw=true", alt="GIF"),
                    style={"width":"72px","height":"72px","margin":"4px","padding":"3px"}
                    ),
                 ],style={"display":"flex","flexDirection":"row"})
                ],style={"width":"360px","height":"300px","margin":self.margin,"padding":self.padding,"background-color":self.cor_card,"border":f"{self.linha_card} solid {self.cor_linha_c}","border-radius":self.raio_borda,"box-shadow":f"10px 10px 8px 2px {self.cor_sombra}"}),
                dbc.Card(children=[
                    html.Div(children=[
                    dcc.Graph(id="graph-1",figure=self.graph_01)
                    ],style={"display":"flex","flexDirection":"row"})
                ],style={"width":"400px","height":"300px","margin":self.margin,"padding":self.padding,"background-color":self.cor_card,"border":f"{self.linha_card} solid {self.cor_linha_c}","border-radius":self.raio_borda,"box-shadow":f"10px 10px 8px 2px {self.cor_sombra}"}),
                dbc.Card(children=[
                    dcc.Graph(id="graph-2",figure=self.graph_02)
                ],style={"width":"400px","height":"300px","margin":self.margin,"padding":self.padding,"background-color":self.cor_card,"border":f"{self.linha_card} solid {self.cor_linha_c}","border-radius":self.raio_borda,"box-shadow":f"10px 10px 8px 2px {self.cor_sombra}"}),
                dbc.Card(children=[
                    dcc.Graph(id="graph-3",figure=self.graph_03)
                ],style={"width":"400px","height":"300px","margin":self.margin,"padding":self.padding,"background-color":self.cor_card,"border":f"{self.linha_card} solid {self.cor_linha_c}","border-radius":self.raio_borda,"box-shadow":f"10px 10px 8px 2px {self.cor_sombra}"}),
                dbc.Card(children=[
                    dcc.Graph(id="graph-4",figure=self.graph_04)
                ],style={"width":"400px","height":"300px","margin":self.margin,"padding":self.padding,"background-color":self.cor_card,"border":f"{self.linha_card} solid {self.cor_linha_c}","border-radius":self.raio_borda,"box-shadow":f"10px 10px 8px 2px {self.cor_sombra}"})
            ],style={"display":"flex","flexDirection":"row"}),
            html.Div(children=[
                dbc.Card(children=[
                    dcc.Graph(id="graph-5",figure=self.graph_05)
                ],style={"width":"1100px","height":"582px","margin":self.margin,"padding":self.padding,"background-color":self.cor_card,"border":f"{self.linha_card} solid {self.cor_linha_c}","border-radius":self.raio_borda,"box-shadow":f"10px 10px 8px 2px {self.cor_sombra}"}),
                html.Div(children=[
                    dbc.Card(children=[
                        html.Div(children=[
                        html.A(
                    html.Img(src="https://github.com/Bruno011012/graficos/blob/main/laser.gif?raw=true", alt="GIF"),
                    style={"width":"32px","height":"32px","margin":"0px","padding":"0px"}
                    ),
                    html.H2(children="GRAFICOS DE TIPOLOGIA PRODUTOS EM FUNÇÃO DO TEMPO (t)",style={"font-size":"20px","color":"white","textShadow":"2px 2px 2px black","margin":"2px","padding":"2px"})
                    ],style={"display":"flex","flexDirection":"row"}),
                    dcc.Graph(id="graph-6",figure=self.graph_06)
                ],style={"width":"900px","height":"282px","margin":self.margin,"padding":self.padding,"background-color":self.cor_card,"border":f"{self.linha_card} solid {self.cor_linha_c}","border-radius":self.raio_borda,"box-shadow":f"10px 10px 8px 2px {self.cor_sombra}"}),
                dbc.Card(children=[
                    html.Div(children=[
                        html.A(
                    html.Img(src="https://github.com/Bruno011012/graficos/blob/main/laser.gif?raw=true", alt="GIF"),
                    style={"width":"32px","height":"32px","margin":"0px","padding":"0px"}
                    ),
                    html.H2(children="GRAFICOS DE MERCADO EM FUNÇÃO DO TEMPO (t)",style={"font-size":"20px","color":"white","textShadow":"2px 2px 2px black","margin":"2px","padding":"2px"})
                    ],style={"display":"flex","flexDirection":"row"}),
                    dcc.Graph(id="graph-7",figure=self.graph_07)
                ],style={"width":"900px","height":"282px","margin":self.margin,"padding":self.padding,"background-color":self.cor_card,"border":f"{self.linha_card} solid {self.cor_linha_c}","border-radius":self.raio_borda,"box-shadow":f"10px 10px 8px 2px {self.cor_sombra}"})
                ])
            ],style={"display":"flex","flexDirection":"row"})
        ],style={"width":"2030px","height":"930px","background-image":"url('https://github.com/Bruno011012/graficos/blob/main/Design%20sem%20nome.png?raw=true')"})
    
    def define_calback(self):
        @self.app.callback(
            [Output('graph-1','figure'),
             Output('graph-2','figure'),
             Output('graph-3','figure'),
             Output('graph-4','figure'),
             Output('graph-5','figure'),
             Output('graph-6','figure'),
             Output('graph-7','figure'),
             Output('datatx-1','children'),],
             [Input('date-picker-range','start_date'),
              Input('date-picker-range','end_date')]
        )
        def update_output(start_date,end_date):
            retorno = callback_context.triggered_id
            print(retorno)
            if retorno == "date-picker-range":
                data_01 = start_date
                data_02 = end_date
                graph_01 = self.contas.conta_01(data_01,data_02)
                graph_02 = self.contas.conta_02(data_01,data_02)
                graph_03 = self.contas.conta_03(data_01,data_02)
                graph_04 = self.contas.conta_04(data_01,data_02)
                graph_05 = self.contas.conta_05()
                graph_06 = self.contas.conta_06(data_01,data_02)
                graph_07 = self.contas.conta_07(data_01,data_02)
                data_ref = f"DATA SELECIONADA {data_01} A {data_02}"
                return graph_01,graph_02,graph_03,graph_04,graph_05,graph_06,graph_07,data_ref
            else:
                graph_01 = self.contas.conta_01("02/01/2020","01/06/2022")
                graph_02 = self.contas.conta_02("02/01/2020","01/06/2022")
                graph_03 = self.contas.conta_03("02/01/2020","01/06/2022")
                graph_04 = self.contas.conta_04("02/01/2020","01/06/2022")
                graph_05 = self.contas.conta_05()
                graph_06 = self.contas.conta_06("02/01/2020","15/02/2020")
                graph_07 = self.contas.conta_07("02/01/2020","15/02/2020")
                data_ref = f"DATA SELECIONADA 02/01/2020 A 01/06/2022"
                return graph_01,graph_02,graph_03,graph_04,graph_05,graph_06,graph_07,data_ref

    def navegador(self):
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Substitua pelo caminho correto
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        # Crie o objeto navegador
        navegador = webbrowser.get('chrome')
        # Abra o endereço no navegador
        navegador.open_new("http://127.0.0.1:8050/")

    def final_01(self):
        self.app.run_server(debug=True)
        

Classe_vendaloja_html01()