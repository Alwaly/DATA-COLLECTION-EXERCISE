from libraries.utils import Utils
from libraries.csv import CsvFactory
from libraries.json import JsonFactory
from libraries.html import HtmlFactory
from libraries.BCEAO import CurrencyScrapper
import pandas as pd
from libraries.countries import ApiGetter

if __name__ == '__main__':
    print(Utils.divider())
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
    df['Country'] = ""
    df['Flag'] = ""
    Utils.randomiseCountryInfo(countriesInformations,df)
    print(df[['Flag','Country']])
    print(Utils.divider())