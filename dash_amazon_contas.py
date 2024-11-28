import pandas as pd
from datetime import datetime,timedelta
from dash_amazon_graficos import Dahs_ama_graf_01

class Dash_ama_contas_01():
    def __init__(self):
        self.frame = pd.DataFrame(pd.read_csv(r".\frames\Amazon Sale Report.csv"))
        self.frame['Date'] = pd.to_datetime(self.frame['Date'])
        print(self.frame)
        self.graficos = Dahs_ama_graf_01()

    
    def conta_01(self,data_i,data_f):
        filtro_01 = self.frame[(self.frame["Date"] >= data_i) & (self.frame["Date"] <= data_f)]
        filtro_02 = filtro_01.groupby("Category")["Amount"].sum().reset_index(name="Amount").sort_values(by="Amount",ascending=False)
        filtro_03 = filtro_02.head(4)
        fig = self.graficos.grafico_01(filtro_03)
        return fig

    def conta_02(self,data_i,data_f):
        filtro_01 = self.frame[(self.frame["Date"] >= data_i) & (self.frame["Date"] <= data_f)]
        filtro_02 = filtro_01.groupby("Courier Status")["Amount"].sum().reset_index(name="Amount").sort_values(by="Amount",ascending=False)
        print(filtro_02)
        filtro_03 = filtro_02.head(2)
        fig = self.graficos.grafico_02(filtro_03)
        return fig

    def conta_03(self,data_i,data_f):
        filtro_01 = self.frame[(self.frame["Date"] >= data_i) & (self.frame["Date"] <= data_f)]
        lista_datas = filtro_01["Date"].unique()
        frame_01 = pd.DataFrame(columns=["ship-service-level","Amount","Date"])
        for i in lista_datas:
            filtro_02 = filtro_01[filtro_01["Date"] == i]
            filtro_03 = filtro_02.groupby("ship-service-level")["Amount"].sum().reset_index(name="Amount").sort_values(by="Amount",ascending=False)
            filtro_03["Date"] = i
            frame_01 = pd.concat([frame_01,filtro_03])
        fig = self.graficos.grafico_03(frame_01)
        return fig

    def conta_04(self,data_i,data_f):
        filtro_01 = self.frame[(self.frame["Date"] >= data_i) & (self.frame["Date"] <= data_f)]
        lista_datas = filtro_01["Date"].unique()
        frame_01 = pd.DataFrame(columns=["Fulfilment","Amount","Date"])
        for i in lista_datas:
            filtro_02 = filtro_01[filtro_01["Date"] == i]
            filtro_03 = filtro_02.groupby("Fulfilment")["Amount"].sum().reset_index(name="Amount").sort_values(by="Amount",ascending=False)
            filtro_03["Date"] = i
            frame_01 = pd.concat([frame_01,filtro_03])
        fig = self.graficos.grafico_04(frame_01)
        return fig

    def conta_05(self,data_i,data_f):
        filtro_01 = self.frame[(self.frame["Date"] >= data_i) & (self.frame["Date"] <= data_f)]
        lista_datas = filtro_01["Date"].unique()
        frame_01 = pd.DataFrame(columns=["Status","Amount","Date"])
        for i in lista_datas:
            filtro_02 = filtro_01[filtro_01["Date"] == i]
            filtro_03 = filtro_02.groupby("Status")["Amount"].sum().reset_index(name="Amount").sort_values(by="Amount",ascending=False)
            filtro_03["Date"] = i
            frame_01 = pd.concat([frame_01,filtro_03])
        fig = self.graficos.grafico_05(frame_01)
        return fig

    def conta_06(self,data_i,data_f):
        filtro_01 = self.frame[(self.frame["Date"] >= data_i) & (self.frame["Date"] <= data_f)]
        lista_datas = filtro_01["Date"].unique()
        frame_01 = pd.DataFrame(columns=["ship-state","Amount","Date"])
        for i in lista_datas:
            filtro_02 = filtro_01[filtro_01["Date"] == i]
            filtro_03 = filtro_02.groupby("ship-state")["Amount"].sum().reset_index(name="Amount").sort_values(by="Amount",ascending=False)
            filtro_03 = filtro_03.head(10)
            filtro_03["Date"] = i
            frame_01 = pd.concat([frame_01,filtro_03])
        fig = self.graficos.grafico_06(frame_01)
        return fig

    def conta_07(self,data_i,data_f):
        filtro_01 = self.frame[(self.frame["Date"] >= data_i) & (self.frame["Date"] <= data_f)]
        lista_datas = filtro_01["Date"].unique()
        frame_01 = pd.DataFrame(columns=["Size","Amount","Date"])
        for i in lista_datas:
            filtro_02 = filtro_01[filtro_01["Date"] == i]
            filtro_03 = filtro_02.groupby("Size")["Amount"].sum().reset_index(name="Amount").sort_values(by="Amount",ascending=False)
            filtro_03 = filtro_03.head(10)
            filtro_03["Date"] = i
            frame_01 = pd.concat([frame_01,filtro_03])
        fig = self.graficos.grafico_07(frame_01)
        return fig
    def conta_08(self,data_i,data_f):
        filtro_01 = self.frame[(self.frame["Date"] >= data_i) & (self.frame["Date"] <= data_f)]
        filtro_01 = filtro_01.sort_values(by="Date",ascending=False)
        filtro_01["promotion-ids"] =  filtro_01["promotion-ids"].apply(lambda x: str(x)[0:11])
        filtro_01 = filtro_01.head(500)
        return filtro_01
