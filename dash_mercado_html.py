from dash import Dash,Input,Output,dcc,html,dash,callback_context
import dash_bootstrap_components as dbc 
from datetime import datetime
from dash.dependencies import Input, Output,State  # Importar Input e Output corretamente
from datetime import datetime
from datetime import date
from dash_mercado_contas import Dash_mercado_contas_01

class Dash_html_01():
    def __init__(self):
        self.margin_1 = "3px"
        self.padding_1 = "2px"
        self.cor_1 = "black"
        self.cor_2 = "#000038"
        self.margin_e = "0px"
        self.padding_e = "0px"
        self.cor_3 = "white"
        self.contas = Dash_mercado_contas_01()
        self.grap_01 = self.contas.conta_1("2019-01-01","2019-01-10")
        self.grap_02 = self.contas.conta_2("2019-01-01","2019-01-10")
        self.grap_03 = self.contas.conta_3("2019-01-01","2019-01-10")
        self.grap_04 = self.contas.conta_4("2019-01-01","2019-01-10")
        self.grap_05 = self.contas.conta_5("2019-01-01","2019-01-10")
        self.tabela = self.contas.conta_6("2019-01-01","2019-01-10")
        self.etapa_criacao()
        self.estapa_layout()
        self.define_calback()
        self.etapa_final()
        
        

    def etapa_criacao(self):
        self.app = Dash()
    
    def estapa_layout(self):
        self.app.layout = html.Div([
            html.Div(children=[
            dbc.Card(children=[
                html.Div(children=[
                    html.A(
                    html.Img(src="https://github.com/Bruno011012/Dashs/blob/main/wired-lineal-438-lab-bottle-round%20(1).gif?raw=true", alt="GIF"),
                    href="https://fgr.com.br/?utm_term=fgr&utm_source=adwords&utm_campaign=&utm_medium=ppc&hsa_mt=b&hsa_grp=165179675491&hsa_src=g&hsa_kw=fgr&hsa_net=adwords&hsa_ver=3&hsa_tgt=kwd-14725552&hsa_ad=692396145054&hsa_acc=4326463385&hsa_cam=21071166859&gad_source=1&gclid=Cj0KCQjwsPCyBhD4ARIsAPaaRf3LSRSKj6TzSBX8cOsSSybumcd8BjzbHVeauRAVl3cby-mJq_e1qeoaAmexEALw_wcB",  # Pode ser qualquer URL ou "#" para manter no mesmo local
                    id="meu-botao-tipo-0",
                    style={"width":"78px","height":"78px","margin":"2px","padding":"2px"}
                    ),
                html.H3(children="DASHBOARD FGR",style={"color":self.cor_3,"textAlign":"right","margin":"8px","padding":"8px","textShadow": "2px 2px 4px #000000", "fontStyle": "italic", "fontWeight": "bold"}),
                html.H2(children="🏠",style={"color":"#FFD700","font-size":"42px","textAlign":"right","margin":self.padding_e,"padding":self.padding_e,"textShadow": "2px 2px 4px #000000", "fontStyle": "italic", "fontWeight": "bold"})
            ],style={"display":"flex","flexDirection":"row","margin":"2px","padding":"2px"}),
            dcc.DatePickerRange(
                    id='date-picker-range',
                    start_date=date(2019, 1, 1),
                    end_date=date(2019, 1, 1),
                    end_date_placeholder_text='Select a date!',
                    style={
                        'background-color': '#FF0000',
                        'color': 'darkblue',
                        'border': '3px solid #FF0000',
                        'border-radius': '5px',
                        "width": "290px", 
                        "height": "50px"

                    }
                ),html.Button(id="button-ok",children="✔️",n_clicks=0,style={"background-color":"red"}),
                html.Div(children=[
                         html.A(
                    html.Img(src="https://github.com/Bruno011012/Dashs/blob/main/wired-lineal-290-coin%20(1).gif?raw=true", alt="GIF"),
                    id="meu-botao-tipo-0",
                    style={"width":"44px","height":"44px","margin":"2px","padding":"2px"}
                    ),
                    html.H3(children="TOTAL NO PERIODO",style={"color":"white","textAlign":"center","margin":"7px","padding":"7px","textShadow": "2px 2px 4px #000000", "fontStyle": "italic", "fontWeight": "bold"}),
                ],style={"display":"flex","flexDirection":"row"}),
                html.Div(children=[
                         html.A(
                    html.Img(src="https://github.com/Bruno011012/Dashs/blob/main/wired-lineal-45-clock-time.gif?raw=true", alt="GIF"),
                    id="meu-botao-tipo-0",
                    style={"width":"44px","height":"44px","margin":"2px","padding":"2px"}
                    ),
                    html.H3(children="DE 01/01/2019 A 30/01/20219",id="data-ref",style={"color":"white","textAlign":"center","margin":"7px","padding":"7px","textShadow": "2px 2px 4px #000000", "fontStyle": "italic", "fontWeight": "bold"}),
                ],style={"display":"flex","flexDirection":"row"}),
                ]
            ,style={"width":"350px","height":"300px","backgorund-color":"blue","border":f"3px solid {self.cor_1}","margin":self.margin_1,"padding":self.padding_1}),
            dbc.Card(children=[
                html.Div(children=[
                     html.A(
                    html.Img(src="https://github.com/Bruno011012/Dashs/blob/main/wired-lineal-1221-test-tubes.gif?raw=true", alt="GIF"),
                    id="meu-botao-tipo-0",
                    style={"width":"32px","height":"32px","margin":"2px","padding":"2px"}
                    ),
                html.H2(children="GRAFICO SEXO(t)",style={"color":self.cor_3,"textAlign":"center","margin":"2px","padding":"2px","textShadow": "2px 2px 4px #000000", "fontStyle": "italic", "fontWeight": "bold"}),
                html.H2(children="➽",style={"font-size":"28px","margin":self.margin_e,"padding":self.padding_e,"textShadow": "2px 2px 4px #000000", "fontStyle": "italic", "fontWeight": "bold","color":"green"}),
                ],style={"display":"flex","flexDirection":"row"}),
                dcc.Graph(id="grap-1",figure=self.grap_01)
            ],style={"width":"350px","height":"300px","backgorund-color":"blue","border":f"3px solid {self.cor_1}","margin":self.margin_1,"padding":self.padding_1}),
            dbc.Card(children=[
                html.Div(children=[
                     html.A(
                    html.Img(src="https://github.com/Bruno011012/Dashs/blob/main/wired-lineal-18-location-pin.gif?raw=true", alt="GIF"),
                    id="meu-botao-tipo-0",
                    style={"width":"32px","height":"32px","margin":"2px","padding":"2px"}
                    ),
                html.H2(children="GRAFICO PRODUTO(t)",style={"color":self.cor_3,"textAlign":"center","margin":"2px","padding":"2px","textShadow": "2px 2px 4px #000000", "fontStyle": "italic", "fontWeight": "bold"}),
                html.H2(children="➤",style={"font-size":"28px","margin":self.margin_e,"padding":self.padding_e,"textShadow": "2px 2px 4px #000000", "fontStyle": "italic", "fontWeight": "bold","color":"green"}),
                ],style={"display":"flex","flexDirection":"row"}),
                dcc.Graph(id="grap-2",figure=self.grap_02)
            ],style={"width":"350px","height":"300px","backgorund-color":"blue","border":f"3px solid {self.cor_1}","margin":self.margin_1,"padding":self.padding_1}),
            dbc.Card(children=[
                html.Div(children=[
                     html.A(
                    html.Img(src="https://github.com/Bruno011012/Dashs/blob/main/wired-lineal-63-home.gif?raw=true", alt="GIF"),
                    id="meu-botao-tipo-0",
                    style={"width":"32px","height":"32px","margin":"2px","padding":"2px"}
                    ),
                html.H2(children="GRAFICO SOBRE O TIPO DE PAGAMENTO(t)",style={"color":self.cor_3,"textAlign":"center","margin":"2px","padding":"2px","textShadow": "2px 2px 4px #000000", "fontStyle": "italic", "fontWeight": "bold"}),
                html.H2(children="🢆",style={"font-size":"28px","margin":self.margin_e,"padding":self.padding_e,"textShadow": "2px 2px 4px #000000", "fontStyle": "italic", "fontWeight": "bold","color":"green"}),
                ],style={"display":"flex","flexDirection":"row"}),
                dcc.Graph(id="grap-3",figure=self.grap_03)
            ],style={"width":"890px","height":"300px","backgorund-color":"blue","border":f"3px solid {self.cor_1}","margin":self.margin_1,"padding":self.padding_1}),
            
        ],style={"display":"flex","flexDirection":"row","margin":self.margin_1,"padding":self.padding_1,"margin":self.margin_1,"padding":self.padding_1}),
        html.Div(children=[
            html.Div(children=[
                    dbc.Card(children=[
                        html.Div(children=[
                     html.A(
                    html.Img(src="https://github.com/Bruno011012/Dashs/blob/main/wired-lineal-12-layers.gif?raw=true", alt="GIF"),
                    id="meu-botao-tipo-0",
                    style={"width":"32px","height":"32px","margin":"2px","padding":"2px"}
                    ),
                html.H2(children="GRAFICO SOBRE O TIPO DE PRODUTO(t)",style={"color":self.cor_3,"textAlign":"center","margin":"2px","padding":"2px","textShadow": "2px 2px 4px #000000", "fontStyle": "italic", "fontWeight": "bold"}),
                html.H2(children="☛",style={"font-size":"28px","margin":self.margin_e,"padding":self.padding_e,"textShadow": "2px 2px 4px #000000", "fontStyle": "italic", "fontWeight": "bold","color":"green"}),
                ],style={"display":"flex","flexDirection":"row"}),
                dcc.Graph(id="grap-4",figure=self.grap_04)
                    ],style={"width":"982px","height":"300px","border":f"3px solid {self.cor_1}","margin":self.margin_1,"padding":self.padding_1}),
                    dbc.Card(children=[
                        html.Div(children=[
                     html.A(
                    html.Img(src="https://github.com/Bruno011012/Dashs/blob/main/wired-lineal-680-it-developer%20(1).gif?raw=true", alt="GIF"),
                    id="meu-botao-tipo-0",
                    style={"width":"32px","height":"32px","margin":"2px","padding":"2px"}
                    ),
                html.H2(children="GRAFICO SOBRE O TIPO A CIDADE(t)",style={"color":self.cor_3,"textAlign":"center","margin":"2px","padding":"2px","textShadow": "2px 2px 4px #000000", "fontStyle": "italic", "fontWeight": "bold"}),
                html.H2(children="▦",style={"font-size":"28px","margin":self.margin_e,"padding":self.padding_e,"textShadow": "2px 2px 4px #000000", "fontStyle": "italic", "fontWeight": "bold","color":"green"}),
                ],style={"display":"flex","flexDirection":"row"}),
                dcc.Graph(id="grap-5",figure=self.grap_05)
                    ],style={"width":"982px","height":"300px","border":f"3px solid {self.cor_1}","margin":self.margin_1,"padding":self.padding_1}),
                    
            ],style={"display":"flex","flexDirection":"row"})
        ],style={"margin":self.margin_1,"padding":self.padding_1}),
        html.Div(children=[html.Div(children=[
                    dbc.Card(children=[
                html.Div(
                style={'width': '1980px', 'height': '244px', 'margin': 'auto'},  # Definindo a largura, altura da div e centralizando
                children=[
                    html.Div(
                        style={'overflowY': 'scroll', 'height': '242px'},  # Adicionando barra de rolagem vertical e definindo altura da tabela
                        children=[
                            html.Table(id="table-1",
                                style={'width': '100%', 'borderCollapse': 'collapse', 'border': '1px solid black'},  # Estilos da tabela
                                children=[
                                    # Cabeçalho da tabela
                                    html.Tr([html.Th(col) for col in self.tabela.columns], style={'background-color': '#8B0000',"color":"white","font-size":"20px"})] +
                                    # Linhas da tabela
                                     [html.Tr([html.Td(self.tabela.iloc[i][col]) for col in self.tabela.columns], style={"color":"white","font-size":"16px",'background-color': '#191970' if i % 2 == 0 else '#A52A2A'}) for i in range(len(self.tabela))])])])
                    ],style={"width":"1980px","height":"240px","border":f"3px solid {self.cor_1}","margin":self.margin_1,"padding":self.padding_1})
        ],style={"display":"flex","flexDirection":"row","margin":self.margin_1,"padding":self.padding_1})

        ])
        ],style={"background-image":"url('https://github.com/Bruno011012/Dashs/blob/main/3598155-red-abstract-backgroud-vetor%20(2).jpg?raw=true')"})

    def etapa_final(self):
        self.app.run_server(debug=True)

    def define_calback(self):
        @self.app.callback(
        [Output('data-ref', 'children'),
         Output('grap-1', 'figure'),
         Output('grap-2', 'figure'),
         Output('grap-3', 'figure'),
         Output('grap-4', 'figure'),
         Output('grap-5', 'figure'),
         Output('table-1', 'children')],
        [Input('button-ok','n_clicks'),
        Input('date-picker-range', 'start_date'),
        Input('date-picker-range', 'end_date')]
        )
        def update_output(n_clicks,start_date,end_date):
            ctx = callback_context
            botao_clicado = ctx.triggered_id if ctx.triggered_id else 'meu-botao'
            if n_clicks == 0 and botao_clicado != "button-ok" :
                print(end_date)
                nt_1 = self.contas.conta_1("2019-01-01","2019-01-10")
                nt_2 = self.contas.conta_2("2019-01-01","2019-01-10")
                nt_3 = self.contas.conta_3("2019-01-01","2019-01-10")
                nt_4 = self.contas.conta_4("2019-01-01","2019-01-10")
                nt_5 = self.contas.conta_5("2019-01-01","2019-01-10")
                print(n_clicks,"2019-01-01","2019-01-10")
                lista_1 = [f"DATA DE 01/01/2019  A 10/01/2019"]
                updated_df = self.contas.conta_6("2019-01-01","2019-01-10")
                updated_children = html.Table(id="table-1",
                                style={'width': '100%', 'borderCollapse': 'collapse', 'border': '1px solid black'},  # Estilos da tabela
                                children=[
                                    # Cabeçalho da tabela
                                    html.Tr([html.Th(col) for col in updated_df.columns], style={'background-color': '#8B0000',"color":"white","font-size":"20px"})] +
                                    # Linhas da tabela
                                     [html.Tr([html.Td(updated_df.iloc[i][col]) for col in updated_df.columns], style={"color":"white","font-size":"16px",'background-color': '#191970' if i % 2 == 0 else '#A52A2A'}) for i in range(len(updated_df))])
                return lista_1,nt_1,nt_2,nt_3,nt_4,nt_5,updated_children
            elif n_clicks != 0 and botao_clicado == "button-ok":
                nt_1 = self.contas.conta_1(start_date,end_date)
                nt_2 = self.contas.conta_2(start_date,end_date)
                nt_3 = self.contas.conta_3(start_date,end_date)
                nt_4 = self.contas.conta_4(start_date,end_date)
                nt_5 = self.contas.conta_5(start_date,end_date)
                print(n_clicks,start_date,end_date)
                lista_1 = [f"DATA DE {start_date}  A {end_date}"]
                updated_df = self.contas.conta_6(start_date,end_date)
                updated_children = html.Table(id="table-1",
                                style={'width': '100%', 'borderCollapse': 'collapse', 'border': '1px solid black'},  # Estilos da tabela
                                children=[
                                    # Cabeçalho da tabela
                                    html.Tr([html.Th(col) for col in updated_df.columns], style={'background-color': '#8B0000',"color":"white","font-size":"20px"})] +
                                    # Linhas da tabela
                                     [html.Tr([html.Td(updated_df.iloc[i][col]) for col in updated_df.columns], style={"color":"white","font-size":"16px",'background-color': '#191970' if i % 2 == 0 else '#A52A2A'}) for i in range(len(updated_df))])
                return lista_1,nt_1,nt_2,nt_3,nt_4,nt_5,updated_children
            else:
                nt_1 = self.contas.conta_1(start_date,end_date)
                nt_2 = self.contas.conta_2(start_date,end_date)
                nt_3 = self.contas.conta_3(start_date,end_date)
                nt_4 = self.contas.conta_4(start_date,end_date)
                nt_5 = self.contas.conta_5(start_date,end_date)
                print(n_clicks,start_date,end_date)
                lista_1 = [f"DATA DE {start_date}  A {end_date}"]
                updated_df = self.contas.conta_6(start_date,end_date)
                updated_children = html.Table(id="table-1",
                                style={'width': '100%', 'borderCollapse': 'collapse', 'border': '1px solid black'},  # Estilos da tabela
                                children=[
                                    # Cabeçalho da tabela
                                    html.Tr([html.Th(col) for col in updated_df.columns], style={'background-color': '#8B0000',"color":"white","font-size":"20px"})] +
                                    # Linhas da tabela
                                     [html.Tr([html.Td(updated_df.iloc[i][col]) for col in updated_df.columns], style={"color":"white","font-size":"16px",'background-color': '#191970' if i % 2 == 0 else '#A52A2A'}) for i in range(len(updated_df))])
                return lista_1,nt_1,nt_2,nt_3,nt_4,nt_5,updated_children

    
        
    
Dash_html_01()