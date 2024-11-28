import pandas as pd 
import numpy as np
import os
from dash_vendaslo_graficos import Classe_dash_vendaloja_graphs01
import pprint 

class Classe_dash_vendaloja_conta01():
    def __init__(self):
        self.graficos = Classe_dash_vendaloja_graphs01()
        self.criacao_frames()

    def criacao_frames(self):
        caminho = r".\frames\vendas"
        arquivo_01 = os.path.join(caminho,"Orders.csv")
        arquivo_02 = os.path.join(caminho,"Products.csv")
        arquivo_03 = os.path.join(caminho,"Customers.csv")
        arquivo_04 = os.path.join(caminho,"Location.csv")
        arquivo_vendas = pd.DataFrame(pd.read_csv(arquivo_01,sep=";",encoding="latin1"))
        arquivo_produtos = pd.DataFrame(pd.read_csv(arquivo_02,sep=";",encoding="latin1"))
        arquivo_clientes = pd.DataFrame(pd.read_csv(arquivo_03,sep=";",encoding="latin1"))
        arquivo_loc = pd.DataFrame(pd.read_csv(arquivo_04,sep=";",encoding="latin1"))
        frame_relac_01 = pd.merge(arquivo_vendas,arquivo_produtos,left_on="Product ID",right_on="Product ID",how="inner")
        frame_relac_02 = pd.merge(frame_relac_01,arquivo_clientes,left_on="Customer ID",right_on="Customer ID",how="inner")
        self.frame_relac_03 = pd.merge(frame_relac_02,arquivo_loc,left_on="Postal Code",right_on="Postal Code",how="inner")
        self.frame_relac_03["Total"] = self.frame_relac_03["Sales"] *  self.frame_relac_03["Quantity"]  
        self.frame_relac_03["Sigla"] = "-"
        self.frame_relac_03["Order Date"] = pd.to_datetime(self.frame_relac_03["Order Date"],format="mixed")
        self.frame_relac_03["Ship Date"] = pd.to_datetime(self.frame_relac_03["Ship Date"],format="mixed")
 

    def conta_01(self,data_01,data_02):
        filtro_00 = self.frame_relac_03[(self.frame_relac_03["Order Date"] >= data_01) & (self.frame_relac_03["Order Date"] <= data_02)]
        filtro_01 = filtro_00.groupby("Ship Mode")["Total"].sum().reset_index(name="Total").sort_values(by="Total")
        grafico = self.graficos.grafico_01(filtro_01)
        return grafico

    def conta_02(self,data_01,data_02):
        filtro_00 = self.frame_relac_03[(self.frame_relac_03["Order Date"] >= data_01) & (self.frame_relac_03["Order Date"] <= data_02)]
        filtro_01 = filtro_00.groupby("Sub-Category")["Total"].sum().reset_index(name="Total").sort_values(by="Total")
        grafico = self.graficos.grafico_02(filtro_01)
        return grafico

    def conta_03(self,data_01,data_02):
        filtro_00 = self.frame_relac_03[(self.frame_relac_03["Order Date"] >= data_01) & (self.frame_relac_03["Order Date"] <= data_02)]
        filtro_01 = filtro_00.groupby("State")["Total"].sum().reset_index(name="Total").sort_values(by="Total",ascending=False).head(17)
        grafico = self.graficos.grafico_03(filtro_01)
        return grafico

    def conta_04(self,data_01,data_02):
        filtro_00 = self.frame_relac_03[(self.frame_relac_03["Order Date"] >= data_01) & (self.frame_relac_03["Order Date"] <= data_02)]
        filtro_01 = filtro_00.groupby("Region")["Total"].sum().reset_index(name="Total").sort_values(by="Total")
        grafico = self.graficos.grafico_04(filtro_01)
        return grafico

    def conta_05(self):
        states_dict = {
        "Kentucky": "KY",
        "California": "CA",
        "Florida": "FL",
        "North Carolina": "NC",
        "Washington": "WA",
        "Texas": "TX",
        "Wisconsin": "WI",
        "Utah": "UT",
        "Nebraska": "NE",
        "Pennsylvania": "PA",
        "Illinois": "IL",
        "Minnesota": "MN",
        "Michigan": "MI",
        "Delaware": "DE",
        "Indiana": "IN",
        "New York": "NY",
        "Arizona": "AZ",
        "Virginia": "VA",
        "Tennessee": "TN",
        "Alabama": "AL",
        "South Carolina": "SC",
        "Oregon": "OR",
        "Colorado": "CO",
        "Iowa": "IA",
        "Ohio": "OH",
        "Missouri": "MO",
        "Oklahoma": "OK",
        "New Mexico": "NM",
        "Louisiana": "LA",
        "Connecticut": "CT",
        "New Jersey": "NJ",
        "Massachusetts": "MA",
        "Georgia": "GA",
        "Nevada": "NV",
        "Rhode Island": "RI",
        "Mississippi": "MS",
        "Arkansas": "AR",
        "Montana": "MT",
        "New Hampshire": "NH",
        "Maryland": "MD",
        "District of Columbia": "DC",
        "Kansas": "KS",
        "Maine": "ME",
        "South Dakota": "SD",
        "Idaho": "ID",
        "North Dakota": "ND",
        "Wyoming": "WY",
        "West Virginia": "WV",
        }
        states_with_zero_values = {}
        for i , nome_es  in enumerate(self.frame_relac_03["State"]):
            for u , dct_nome_es in  enumerate(states_dict.keys()):
                if nome_es == dct_nome_es:
                    self.frame_relac_03.loc[i,"Sigla"] = states_dict[dct_nome_es]

        filtro = self.frame_relac_03.groupby("Sigla")["Total"].sum().reset_index(name="Total").sort_values(by="Total")

        for i, valor_dictref in enumerate(filtro["Sigla"]):
            states_with_zero_values[valor_dictref] = filtro.loc[i,"Total"]

        print(filtro)
        pprint.pprint(states_with_zero_values)
        grafico = self.graficos.grafico_05(states_with_zero_values)
        return grafico

    def conta_06(self,data_01,data_02):
        filtro_00 = self.frame_relac_03[(self.frame_relac_03["Order Date"] >= data_01) & (self.frame_relac_03["Order Date"] <= data_02)]
        valores_00 = filtro_00.groupby("Segment")["Total"].sum().reset_index(name="Total").sort_values(by="Total",ascending=False).head(5)
        valores_01 = list(valores_00["Segment"].unique())
        filtro_01 = filtro_00[filtro_00["Segment"].isin(valores_01)]
        tabela_pivot = pd.pivot_table(filtro_01,index="Order Date",columns="Segment",values="Total",aggfunc="sum",fill_value=0)
        tabela_pivot = tabela_pivot.reset_index()
        colunas_0 = list(tabela_pivot.columns)
        colunas_1 = [x for x in colunas_0 if x not in ["Order Date","Total"]]
        tabela_melte = pd.melt(tabela_pivot,id_vars="Order Date",value_vars=colunas_1,value_name="Valores")
        tabela_melte = tabela_melte.sort_values(by="Order Date")
        grafico = self.graficos.grafico_06(tabela_melte)
        return grafico
    
    def conta_07(self,data_01,data_02):
        filtro_00 = self.frame_relac_03[(self.frame_relac_03["Order Date"] >= data_01) & (self.frame_relac_03["Order Date"] <= data_02)]
        valores_00 = filtro_00.groupby("Category")["Total"].sum().reset_index(name="Total").sort_values(by="Total",ascending=False).head(5)
        valores_01 = list(valores_00["Category"].unique())
        filtro_01 = filtro_00[filtro_00["Category"].isin(valores_01)]
        tabela_pivot = pd.pivot_table(filtro_01,index="Order Date",columns="Category",values="Total",aggfunc="sum",fill_value=0)
        tabela_pivot = tabela_pivot.reset_index()
        colunas_0 = list(tabela_pivot.columns)
        colunas_1 = [x for x in colunas_0 if x not in ["Order Date","Total"]]
        tabela_melte = pd.melt(tabela_pivot,id_vars="Order Date",value_vars=colunas_1,value_name="Valores")
        tabela_melte = tabela_melte.sort_values(by="Order Date")
        grafico = self.graficos.grafico_07(tabela_melte)
        return grafico

Classe_dash_vendaloja_conta01()