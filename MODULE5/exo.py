from libraries.utils import Utils
from libraries.csv import CsvFactory
from libraries.json import JsonFactory
from libraries.html import HtmlFactory
from libraries.BCEAO import CurrencyScrapper
import pandas as pd
from libraries.countries import ApiGetter
from libraries.db import DataBase
from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return Utils.organizeData()
if __name__ == '__main__':
    data=Utils.concatData(HtmlFactory.main(),CsvFactory.main(),JsonFactory.main())
    df=pd.DataFrame(data)
    devisesDF=pd.DataFrame(CurrencyScrapper.makeCurrencyList())
    devisesTab=["Euro", "Dollar us", "Yen japonais"]
    df['Devise'] = ""
    df["XOF Value"]=0
    df['Devise'] = df['Devise'] \
        .apply(lambda x: Utils.randomise(devisesTab))
    df=Utils.convertDevise(df, devisesDF)
    countriesInformations=ApiGetter.getNameAndFlag()
    countriesDf=pd.DataFrame(countriesInformations)
    df['Country'] = ""
    df['Flag'] = ""
    Utils.randomiseCountryInfo(countriesInformations,df)
    print(Utils.divider())
    #DataBase.create('DATACOLLECTIONEXERCISE')
    #DataBase.CreateCountryTable("DATACOLLECTIONEXERCISE")
    #DataBase.CreateDevisesTable("DATACOLLECTIONEXERCISE")
    #DataBase.CreateCustomerTable("DATACOLLECTIONEXERCISE")
    #DataBase.insertCountry(countriesDf,"DATACOLLECTIONEXERCISE")
    #DataBase.insertDevises(devisesDF,"DATACOLLECTIONEXERCISE")
    #DataBase.insertCustommers(df,"DATACOLLECTIONEXERCISE")
    
    