import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, date, timedelta
import os.path
import numpy

class covid19_data:

    def __init__(self):
        self.url_dati_nazionali   = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv"
        self.url_dati_provinciali = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/dpc-covid19-ita-province.csv"
        self.url_dati_regionali   = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv"

        self.file_dati_nazionali   = "nazionali.csv"
        self.file_dati_provinciali = "provinciali.csv"
        self.file_dati_regionali   = "regionali .csv"

        self.df_nazionali   = 0
        self.df_provinciali = 0
        self.df_regionali   = 0

        self.mat_province = 0
        self.mat_regioni = 0

        self.process_files()

    def process_files(self):

        date_today = date.today()
        download = False

        if os.path.isfile(self.file_dati_nazionali):
            self.df_nazionali = pd.read_csv(self.file_dati_nazionali)
            self.df_nazionali = self.df_nazionali.set_index('data')
            #print(df_nationali.head())
            last_date = self.df_nazionali.index[-1]
            last_date = datetime.fromisoformat(last_date).date()
            if not date_today==last_date:
                download = True
        else:
            download = True

        if download:
            self.df_nazionali = pd.read_csv(self.url_dati_nazionali)
            self.df_nazionali = self.df_nazionali.set_index('data')
            self.df_nazionali.to_csv(self.file_dati_nazionali)
            self.df_provinciali = pd.read_csv(self.url_dati_provinciali)
            self.df_provinciali = self.df_provinciali.set_index('data')
            self.df_provinciali.to_csv(self.file_dati_provinciali)
            self.df_regionali = pd.read_csv(self.url_dati_regionali)
            self.df_regionali = self.df_regionali.set_index('data')
            self.df_regionali.to_csv(self.file_dati_regionali)

        self.df_nazionali = pd.read_csv(self.file_dati_nazionali)
        self.df_nazionali["data"] = pd.to_datetime(self.df_nazionali["data"]).apply(lambda x: datetime.strftime(x, "%d-%m"))
        self.df_nazionali = self.df_nazionali.set_index('data')

        self.df_provinciali = pd.read_csv(self.file_dati_provinciali)
        self.df_provinciali["data"] = pd.to_datetime(self.df_provinciali["data"]).apply(lambda x: datetime.strftime(x, "%d-%m"))
        self.df_provinciali = self.df_provinciali.set_index('data')
        df_temp = self.df_provinciali.loc[self.df_provinciali['denominazione_provincia'] != "In fase di definizione/aggiornamento"]
        codici_province = df_temp['codice_provincia'].unique()
        nomi_province= df_temp['denominazione_provincia'].unique()
        self.mat_province =[codici_province, nomi_province]
        self.mat_province = numpy.transpose(self.mat_province)

        self.df_regionali = pd.read_csv(self.file_dati_regionali)
        self.df_regionali["data"] = pd.to_datetime(self.df_regionali["data"]).apply(lambda x: datetime.strftime(x, "%d-%m"))
        self.df_regionali = self.df_regionali.set_index('data')
        self.df_regionali.loc[self.df_regionali['denominazione_regione'] == "P.A. Trento", 'codice_regione'] = '101'
        codici_regioni = self.df_regionali['codice_regione'].unique()
        nomi_regioni = self.df_regionali['denominazione_regione'].unique()
        self.mat_regioni = [codici_regioni, nomi_regioni]
        self.mat_regioni = numpy.transpose(self.mat_regioni)



#x = covid19_data()
#for row in x.mat_province:
#    print(row)


#for row in x.mat_regioni:
#    print(row)
#print(x.mat_regioni)
#print(x.mat_province)




