import pandas as pd
from datetime import datetime, timedelta,date
from dash_mercado_graficos import Dahs_mercado_graficos_01
class Dash_mercado_contas_01():
    def __init__(self):
        self.frame = pd.DataFrame(pd.read_csv(r".\frames\supermarket_sales - Sheet1.csv"))
        self.frame["Date"] = pd.to_datetime(self.frame["Date"])
        self.graficos = Dahs_mercado_graficos_01()
        self.conta_1("2019-01-01","2019-01-10")
        
    def conta_1(self,data_ini,data_fin):
        data_i = datetime.strptime(data_ini,"%Y-%m-%d")
        data_f = datetime.strptime(data_fin,"%Y-%m-%d")
        filtro = self.frame[(self.frame["Date"] >= data_i) & (self.frame["Date"] <= data_f)]
        filtro_1 = filtro.groupby("Gender")["Unit price"].sum().reset_index(name="price").sort_values(by="price")
        fig = self.graficos.grafico_1(filtro_1)
        return fig
    
    def conta_2(self,data_ini,data_fin):
        data_i = datetime.strptime(data_ini,"%Y-%m-%d")
        data_f = datetime.strptime(data_fin,"%Y-%m-%d")
        filtro = self.frame[(self.frame["Date"] >= data_i) & (self.frame["Date"] <= data_f)]
        filtro_1 = filtro.groupby("Branch")["Unit price"].sum().reset_index(name="price").sort_values(by="price")
        fig = self.graficos.grafico_2(filtro_1)
        return fig

    def conta_3(self,data_ini,data_fin):
        data_i = datetime.strptime(data_ini,"%Y-%m-%d")
        data_f = datetime.strptime(data_fin,"%Y-%m-%d")
        filtro = self.frame[(self.frame["Date"] >= data_i) & (self.frame["Date"] <= data_f)]
        tabela_datas = filtro["Date"].unique()
        frame_n1 = pd.DataFrame(columns=["Payment","Unit price","Date"])
        for i , dataa in enumerate(tabela_datas):
            filtro_01 = filtro[filtro["Date"] == dataa]
            filtro_02 = pd.DataFrame(filtro_01.groupby("Payment")["Unit price"].sum().reset_index(name="Unit price").sort_values(by="Unit price"))
            filtro_02["Date"] = dataa
            frame_n1 = pd.concat([filtro_02,frame_n1])
        fig = self.graficos.grafico_3(frame_n1)
        return fig

    def conta_4(self,data_ini,data_fin):
        data_i = datetime.strptime(data_ini,"%Y-%m-%d")
        data_f = datetime.strptime(data_fin,"%Y-%m-%d")
        filtro = self.frame[(self.frame["Date"] >= data_i) & (self.frame["Date"] <= data_f)]
        tabela_datas = filtro["Date"].unique()
        frame_n1 = pd.DataFrame(columns=["Product line","Unit price","Date"])
        for i , dataa in enumerate(tabela_datas):
            filtro_01 = filtro[filtro["Date"] == dataa]
            filtro_02 = pd.DataFrame(filtro_01.groupby("Product line")["Unit price"].sum().reset_index(name="Unit price").sort_values(by="Unit price"))
            filtro_02["Date"] = dataa
            frame_n1 = pd.concat([filtro_02,frame_n1])
        fig = self.graficos.grafico_4(frame_n1)
        return fig
    
    def conta_5(self,data_ini,data_fin):
        data_i = datetime.strptime(data_ini,"%Y-%m-%d")
        data_f = datetime.strptime(data_fin,"%Y-%m-%d")
        filtro = self.frame[(self.frame["Date"] >= data_i) & (self.frame["Date"] <= data_f)]
        tabela_datas = filtro["Date"].unique()
        frame_n1 = pd.DataFrame(columns=["City","Unit price","Date"])
        for i , dataa in enumerate(tabela_datas):
            filtro_01 = filtro[filtro["Date"] == dataa]
            filtro_02 = pd.DataFrame(filtro_01.groupby("City")["Unit price"].sum().reset_index(name="Unit price").sort_values(by="Unit price"))
            filtro_02["Date"] = dataa
            frame_n1 = pd.concat([filtro_02,frame_n1])
        fig = self.graficos.grafico_5(frame_n1)
        return fig
    
    def conta_6(self,data_ini,data_fin):
        data_i = datetime.strptime(data_ini,"%Y-%m-%d")
        data_f = datetime.strptime(data_fin,"%Y-%m-%d")
        filtro = self.frame[(self.frame["Date"] >= data_i) & (self.frame["Date"] <= data_f)]
        filtro = filtro.sort_values(by="Date",ascending=False)
        return filtro



