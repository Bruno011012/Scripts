from dash import Dash , html , dcc ,Input,Output,callback_context
import dash_bootstrap_components as dbc 
from dash_amazon_contas import Dash_ama_contas_01
from datetime import datetime,timedelta

class Dash_amazon_html_01():
    def __init__(self):
        self.cor_borda = "white"
        self.letra = "white"
        self.margin_01 = "6px"
        self.padding_01 = "2px"
        self.raio_borda = "20px"
        self.cor_f_car = "rgba(0, 0, 255, 0.5)"
        data_i = datetime(2022,3,31)
        data_f = datetime(2022,4,5)
        self.des_01 = 0
        self.contas = Dash_ama_contas_01()
        self.fig_01 = self.contas.conta_01(data_i,data_f)
        self.fig_02 = self.contas.conta_02(data_i,data_f)
        self.fig_03 = self.contas.conta_03(data_i,data_f)
        self.fig_04 = self.contas.conta_04(data_i,data_f)
        self.fig_05 = self.contas.conta_05(data_i,data_f)
        self.fig_06 = self.contas.conta_06(data_i,data_f)
        self.fig_07 = self.contas.conta_07(data_i,data_f)
        self.tabela = self.contas.conta_08(data_i,data_f)
        self.datas()
        self.inicio()
        self.layout()
        self.define_calback()
        self.final()
    
    def datas(self):
        start_date = datetime(2022, 3, 31)
        end_date = datetime(2022, 6, 29)
        self.dates_01 = []
        date = start_date
        while date <= end_date:
            self.dates_01.append(date.strftime('%Y-%m-%d'))
            date += timedelta(days=6)
            
    def inicio(self):
        self.app = Dash(__name__)
    
    def layout(self):
        self.app.layout = html.Div(children=[
            html.Div(children=[
                dbc.Card(children=[
                    html.Div(children=[
                    html.A(
                    html.Img(src="https://github.com/Bruno011012/Dash_1/blob/main/wired-lineal-1445-greek-helmet%20(1).gif?raw=true", alt="GIF"),
                    id="meu-botao-tipo-0",
                    style={"width":"44px","height":"44px","margin":"2px","padding":"2px"}
                    ),
                    html.H1(id="botton-data",children="CLIQUE >>",style={"color":f"{self.letra}","margin":"2px","padding":"2px","font-size":"26px"}),
                    html.Button(id="button-1",children="OK",style={"margin":"2px","padding":"2px","color":f"{self.letra}","background-color":f"red"}),
                    ],style={"display":"flex","flexDirection":"row"}),
                    html.Div(children=[
                        dcc.Graph(id="fig-01",figure=self.fig_01,style={"display":"none"})
                    ],style={"width":"230","height":"217px","margin":"0px","padding":"0px"}),
                    
                ],style={"background-color":f"{self.cor_f_car}","margin":f"{self.margin_01}","padding":f"{self.padding_01}","width":"320px","height":"270px","border":f"3px solid {self.cor_borda}","border-radius": f"{self.raio_borda}","box-shadow": f"10px 10px 8px 2px {self.cor_f_car}"}),
                dbc.Card(children=[
                    html.Div(children=[
                    html.A(
                    html.Img(src="https://github.com/Bruno011012/Dash_1/blob/main/wired-lineal-1445-greek-helmet%20(1).gif?raw=true", alt="GIF"),
                    id="meu-botao-tipo-0",
                    style={"width":"44px","height":"44px","margin":"2px","padding":"2px"}
                    ),
                    html.H1(children="STATUS",style={"color":f"{self.letra}","margin":"2px","padding":"2px","font-size":"26px"}),
                    html.H1(children=">>",style={"margin":"2px","padding":"2px","color":f"{self.letra}","font-size":"26px"})
                    ],style={"display":"flex","flexDirection":"row"}),
                    html.Div(children=[
                        dcc.Graph(id="fig-02",figure=self.fig_02,style={"display":"none"})
                    ],style={"width":"230","height":"217px","margin":"0px","padding":"0px"}),

                ],style={"background-color":f"{self.cor_f_car}","margin":f"{self.margin_01}","padding":f"{self.padding_01}","width":"320px","height":"270x","border":f"3px solid {self.cor_borda}","border-radius": f"{self.raio_borda}","box-shadow": f"10px 10px 8px 2px {self.cor_f_car}"}),
                dbc.Card(children=[
                    html.Div(children=[
                    html.A(
                    html.Img(src="https://github.com/Bruno011012/Dash_1/blob/main/wired-lineal-1445-greek-helmet%20(1).gif?raw=true", alt="GIF"),
                    id="meu-botao-tipo-0",
                    style={"width":"44px","height":"44px","margin":"2px","padding":"2px"}
                    ),
                    html.H1(children="NIVEL DO PACOTE",style={"color":f"{self.letra}","margin":"2px","padding":"2px","font-size":"26px"}),
                    html.H1(children=">>",style={"margin":"2px","padding":"2px","color":f"{self.letra}","font-size":"26px"})
                    ],style={"display":"flex","flexDirection":"row"}),
                    html.Div(children=[
                        dcc.Graph(id="fig-03",figure=self.fig_03,style={"display":"none"})
                    ],style={"width":"660","height":"217px","margin":"0px","padding":"0px"}),
                ],style={"background-color":f"{self.cor_f_car}","margin":f"{self.margin_01}","padding":f"{self.padding_01}","width":"660px","height":"270px","border":f"3px solid {self.cor_borda}","border-radius": f"{self.raio_borda}","box-shadow": f"10px 10px 8px 2px {self.cor_f_car}"}),
                dbc.Card(children=[
                    html.Div(children=[
                    html.A(
                    html.Img(src="https://github.com/Bruno011012/Dash_1/blob/main/wired-lineal-1445-greek-helmet%20(1).gif?raw=true", alt="GIF"),
                    id="meu-botao-tipo-0",
                    style={"width":"44px","height":"44px","margin":"2px","padding":"2px"}
                    ),
                    html.H1(children="TIPO DE SERVIÇO PRIME OU NAO",style={"color":f"{self.letra}","margin":"2px","padding":"2px","font-size":"26px"}),
                    html.H1(children=">>",style={"margin":"2px","padding":"2px","color":f"{self.letra}","font-size":"26px"})
                    ],style={"display":"flex","flexDirection":"row"}),
                     html.Div(children=[
                        dcc.Graph(id="fig-04",figure=self.fig_04,style={"display":"none"})
                    ],style={"width":"660","height":"217px","margin":"0px","padding":"0px"}),
                    
                ],style={"background-color":f"{self.cor_f_car}","margin":f"{self.margin_01}","padding":f"{self.padding_01}","width":"660px","height":"270px","border":f"3px solid {self.cor_borda}","border-radius": f"{self.raio_borda}","box-shadow": f"10px 10px 8px 2px {self.cor_f_car}"})
            ],style={"display":"flex","flexDirection":"row"}),
            html.Div(children=[
                    dbc.Card(children=[
                    html.Div(
                children=[
            dcc.Slider(
                id='mes-slider',
                min=0,
                max=len(self.dates_01) - 1,
                marks={i: {'label': self.dates_01[i], 'style': {'color': 'white', 'fontSize': '18px'}} for i in range(len(self.dates_01))},
                value=len(self.dates_01) - 1
        )],style={"width":"1960px","height":"40px","margin": "0px", "padding": "0px"}),    
                    
                ],style={"background-color":f"{self.cor_f_car}","margin":f"{self.margin_01}","padding":f"{self.padding_01}","width":"2000px","height":"40px","border":f"3px solid {self.cor_borda}","border-radius": f"{self.raio_borda}","box-shadow": f"10px 10px 8px 2px {self.cor_f_car}"})
            ],style={"display":"flex","flexDirection":"row"}),
            html.Div(children=[
                    dbc.Card(children=[
                    html.Div(children=[
                    html.A(
                    html.Img(src="https://github.com/Bruno011012/Dash_1/blob/main/wired-lineal-1445-greek-helmet%20(1).gif?raw=true", alt="GIF"),
                    id="meu-botao-tipo-0",
                    style={"width":"44px","height":"44px","margin":"2px","padding":"2px"}
                    ),
                    html.H1(children="CARACTERISTICAS DO SERVIÇO (t)",style={"color":f"{self.letra}","margin":"2px","padding":"2px","font-size":"26px"}),
                    html.H1(children=">>",style={"margin":"2px","padding":"2px","color":f"{self.letra}","font-size":"26px"})
                    ],style={"display":"flex","flexDirection":"row"}),
                    html.Div(children=[
                        dcc.Graph(id="fig-05",figure=self.fig_05,style={"display":"none"})
                    ],style={"width":"978px","height":"198px","margin":"0px","padding":"0px"}),
                    
                ],style={"background-color":f"{self.cor_f_car}","margin":f"{self.margin_01}","padding":f"{self.padding_01}","width":"978px","height":"250px","border":f"3px solid {self.cor_borda}","border-radius": f"{self.raio_borda}","box-shadow": f"10px 10px 8px 2px {self.cor_f_car}"}),
                dbc.Card(children=[
                    html.Div(children=[
                    html.A(
                    html.Img(src="https://github.com/Bruno011012/Dash_1/blob/main/wired-lineal-1445-greek-helmet%20(1).gif?raw=true", alt="GIF"),
                    id="meu-botao-tipo-0",
                    style={"width":"44px","height":"44px","margin":"2px","padding":"2px"}
                    ),
                    html.H1(children="CIDADES DE ENTREGA (t)",style={"color":f"{self.letra}","margin":"2px","padding":"2px","font-size":"26px"}),
                    html.H1(children=">>",style={"margin":"2px","padding":"2px","color":f"{self.letra}","font-size":"26px"})
                    ],style={"display":"flex","flexDirection":"row"}),
                    html.Div(children=[
                        dcc.Graph(id="fig-06",figure=self.fig_06,style={"display":"none"})
                    ],style={"width":"978px","height":"198px","margin":"0px","padding":"0px"}),
                    
                ],style={"background-color":f"{self.cor_f_car}","margin":f"{self.margin_01}","padding":f"{self.padding_01}","width":"978px","height":"250px","border":f"3px solid {self.cor_borda}","border-radius": f"{self.raio_borda}","box-shadow": f"10px 10px 8px 2px {self.cor_f_car}"})
            ],style={"display":"flex","flexDirection":"row"}),
            html.Div(children=[
            dbc.Card(children=[
                html.Div(
                        style={'overflowY': 'scroll', 'height': '242px'},  # Adicionando barra de rolagem vertical e definindo altura da tabela
                        children=[
                            html.Table(id="table-1",
                                style={'width': '100%', 'borderCollapse': 'collapse', 'border': '1px solid black'},  # Estilos da tabela
                                children=[
                                    # Cabeçalho da tabela
                                    html.Tr([html.Th(col) for col in self.tabela.columns], style={'background-color': '#8B0000',"color":"white","font-size":"18px"})] +
                                    # Linhas da tabela
                                     [html.Tr([html.Td(self.tabela.iloc[i][col]) for col in self.tabela.columns], style={"color":"white","font-size":"16px",'background-color': '#0000FF' if i % 2 == 0 else '#2F4F4F'}) for i in range(len(self.tabela))])]),
                ],style={"background-color":f"{self.cor_f_car}","margin":f"{self.margin_01}","padding":f"{self.padding_01}","width":"1995px","height":"250px","border":f"3px solid {self.cor_borda}","border-radius": f"{self.raio_borda}","box-shadow": f"10px 10px 8px 2px {self.cor_f_car}"}),
            ],style={"display":"flex","flexDirection":"row"}),
        ],style={"width":"2000px","height":"900px","background-image":"url('https://github.com/Bruno011012/Dash_1/blob/main/3%20(2).png?raw=true')"})

    def final(self):
        self.app.run_server(debug=True)

    def define_calback(self):
        @self.app.callback(
        [Output('fig-01', 'style'),
         Output('fig-02', 'style'),
         Output('fig-03', 'style'),
         Output('fig-04', 'style'),
         Output('fig-05', 'style'),
         Output('fig-06', 'style'),
         Output('fig-01', 'figure'),
         Output('fig-02', 'figure'),
         Output('fig-03', 'figure'),
         Output('fig-04', 'figure'),
         Output('fig-05', 'figure'),
         Output('fig-06', 'figure'),
         Output('table-1', 'children')],
        [Input('button-1','n_clicks'),
         Input('mes-slider', 'value')]
        )
        def update_output(n_clicks,selected_value):
            ctx = callback_context.triggered_id
            print(ctx)
            if ctx == "button-1":
                self.des_01 = 1
                print(ctx)
                lis_01 = {'display': 'block'}
                lis_02 = {'display': 'none'}
                data_i = datetime(2022,3,31)
                data_f = datetime(2022,4,5)
                fig_01 = self.contas.conta_01(data_i,data_f)
                fig_02 = self.contas.conta_02(data_i,data_f)
                fig_03 = self.contas.conta_03(data_i,data_f)
                fig_04 = self.contas.conta_04(data_i,data_f)
                fig_05 = self.contas.conta_05(data_i,data_f)
                fig_06 = self.contas.conta_06(data_i,data_f)
                fig_07 = self.contas.conta_07(data_i,data_f)
                tabela = self.contas.conta_08(data_i,data_f)
                updated_children = html.Table(id="table-1",
                style={'width': '100%', 'borderCollapse': 'collapse', 'border': '1px solid black'},  # Estilos da tabela
                children=[html.Tr([html.Th(col) for col in tabela.columns], style={'background-color': '#8B0000',"color":"white","font-size":"18px"})] +
                [html.Tr([html.Td(tabela.iloc[i][col]) for col in tabela.columns], style={"color":"white","font-size":"16px",'background-color': '#0000FF' if i % 2 == 0 else '#2F4F4F'}) for i in range(len(tabela))])
                return lis_01,lis_01,lis_01,lis_01,lis_01,lis_01,fig_01,fig_02,fig_03,fig_04,fig_05,fig_06,updated_children
            elif self.des_01 == 1 :
                print(ctx)
                print(selected_value)
                print(self.dates_01[int(selected_value)])
                data_i = datetime(2022,3,31)
                data_f = self.dates_01[int(selected_value)]
                fig_01 = self.contas.conta_01(data_i,data_f)
                fig_02 = self.contas.conta_02(data_i,data_f)
                fig_03 = self.contas.conta_03(data_i,data_f)
                fig_04 = self.contas.conta_04(data_i,data_f)
                fig_05 = self.contas.conta_05(data_i,data_f)
                fig_06 = self.contas.conta_06(data_i,data_f)
                fig_07 = self.contas.conta_07(data_i,data_f)
                lis_01 = {'display': 'block'}
                lis_02 = {'display': 'none'}
                tabela = self.contas.conta_08(data_i,data_f)
                updated_children = html.Table(id="table-1",
                style={'width': '100%', 'borderCollapse': 'collapse', 'border': '1px solid black'},  # Estilos da tabela
                children=[html.Tr([html.Th(col) for col in tabela.columns], style={'background-color': '#8B0000',"color":"white","font-size":"18px"})] +
                [html.Tr([html.Td(tabela.iloc[i][col]) for col in tabela.columns], style={"color":"white","font-size":"16px",'background-color': '#0000FF' if i % 2 == 0 else '#2F4F4F'}) for i in range(len(tabela))])
                return lis_01,lis_01,lis_01,lis_01,lis_01,lis_01,fig_01,fig_02,fig_03,fig_04,fig_05,fig_06,updated_children
            else:
                print(ctx)
                lis_01 = {'display': 'none'}
                data_i = datetime(2022,3,31)
                data_f = datetime(2022,4,5)
                fig_01 = self.contas.conta_01(data_i,data_f)
                fig_02 = self.contas.conta_02(data_i,data_f)
                fig_03 = self.contas.conta_03(data_i,data_f)
                fig_04 = self.contas.conta_04(data_i,data_f)
                fig_05 = self.contas.conta_05(data_i,data_f)
                fig_06 = self.contas.conta_06(data_i,data_f)
                fig_07 = self.contas.conta_07(data_i,data_f)
                tabela = self.contas.conta_08(data_i,data_f)
                updated_children = html.Table(id="table-1",
                style={'width': '100%', 'borderCollapse': 'collapse', 'border': '1px solid black'},  # Estilos da tabela
                children=[html.Tr([html.Th(col) for col in tabela.columns], style={'background-color': '#8B0000',"color":"white","font-size":"18px"})] +
                [html.Tr([html.Td(tabela.iloc[i][col]) for col in tabela.columns], style={"color":"white","font-size":"16px",'background-color': '#0000FF' if i % 2 == 0 else '#2F4F4F'}) for i in range(len(tabela))])
                return lis_01,lis_01,lis_01,lis_01,lis_01,lis_01,fig_01,fig_02,fig_03,fig_04,fig_05,fig_06,updated_children
  
            
Dash_amazon_html_01()