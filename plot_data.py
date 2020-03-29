import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import read_data
import os.path

class plot_data:

    def __init__(self):
        self.images_path   = "./grafici"
        if not os.path.isdir(self.images_path):
            os.mkdir(self.images_path)


    def grafici_nazionali(self):
        plt.close('all')
        data = read_data.covid19_data()

        ax = plt.gca()
        data.df_nazionali.plot(kind='line', use_index=True, y='totale_ospedalizzati', ax=ax, title="Italia")
        data.df_nazionali.plot(kind='line', use_index=True, y='isolamento_domiciliare', ax=ax, title="Italia")
        #plt.show()
        plt.savefig(self.images_path+'/nazionali_vari.png')
        plt.close('all')
        
        ax = plt.gca()
        data.df_nazionali.plot(kind='line', use_index=True, y='deceduti', color='red', ax=ax, title="Italia")
        data.df_nazionali.plot(kind='line', use_index=True, y='terapia_intensiva', ax=ax, title="Italia")
        #plt.show()
        plt.savefig(self.images_path+'/nazionali_terapInt_deceduti.png')
        plt.close('all')

        ax = plt.gca()
        data.df_nazionali.plot(kind='line', use_index=True, y='nuovi_attualmente_positivi', ax=ax, title="Italia")
        #plt.show()
        plt.savefig(self.images_path+'/nazionali_nuovi_positivi.png')
        plt.close('all')

        ax = plt.gca()
        data.df_nazionali.plot(kind='line', use_index=True, y='totale_casi', ax=ax, title="Italia")
        #plt.show()
        plt.savefig(self.images_path+'/nazionali_casi_totali.png')
        plt.close('all')

    def grafici_regione(self, cod):
        cod_reg = str(cod)
        plt.close('all')
        data = read_data.covid19_data()
        df_regionali_new = data.df_regionali.loc[data.df_regionali['codice_regione'] == cod]
        nome_reg = df_regionali_new.iloc[0]["denominazione_regione"]
        #print(data.df_regionali.head())

        ax = plt.gca()
        df_regionali_new.plot(kind='line', use_index=True, y='totale_ospedalizzati', ax=ax, title=nome_reg)
        df_regionali_new.plot(kind='line', use_index=True, y='isolamento_domiciliare', ax=ax, title=nome_reg)
        #plt.show()
        plt.savefig(self.images_path+'/regione_'+cod_reg+'_vari.png')
        plt.close('all')

        ax = plt.gca()
        df_regionali_new.plot(kind='line', use_index=True, y='deceduti', color='red', ax=ax, title=nome_reg)
        df_regionali_new.plot(kind='line', use_index=True, y='terapia_intensiva', ax=ax, title=nome_reg)
        #plt.show()
        plt.savefig(self.images_path+'/regione_'+cod_reg+'_terapInt_deceduti.png')
        plt.close('all')

        ax = plt.gca()
        df_regionali_new.plot(kind='line', use_index=True, y='nuovi_attualmente_positivi', ax=ax, title=nome_reg)
        #plt.show()
        plt.savefig(self.images_path+'/regione_'+cod_reg+'_nuovi_positivi.png')
        plt.close('all')

        ax = plt.gca()
        df_regionali_new.plot(kind='line', use_index=True, y='totale_casi', ax=ax, title=nome_reg)
        #plt.show()
        plt.savefig(self.images_path+'/regione_'+cod_reg+'_casi_totali.png')
        plt.close('all')

    def grafici_provincia(self, cod):
        cod_prov = str(cod)
        plt.close('all')
        data = read_data.covid19_data()
        df_provinciali_new = data.df_provinciali.loc[data.df_provinciali['codice_provincia'] == cod]
        nome_prov = df_provinciali_new.iloc[0]["denominazione_provincia"]
        #print(data.df_regionali.head())

        ax = plt.gca()
        df_provinciali_new.plot(kind='line', use_index=True, y='totale_casi', ax=ax, title=nome_prov)
        #plt.show()
        plt.savefig(self.images_path+'/provincia_'+cod_prov+'_casi_totali.png')
        plt.close('all')


    def grafici_regioni(self):
        data = read_data.covid19_data()
        for row in data.mat_regioni:
            self.grafici_regione(row[0])


    def grafici_province(self):
        data = read_data.covid19_data()
        for row in data.mat_province:
           self.grafici_provincia(row[0])

#grafici_regioni()
#grafici_province()