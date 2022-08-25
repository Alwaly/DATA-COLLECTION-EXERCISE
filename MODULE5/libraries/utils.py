import random
from .db import DataBase

class Utils(object):
    @classmethod
    def divider(cls, n=54):
        return '-' * n

    @classmethod
    def randomize(cls,
                  start,
                  final):
        return random \
            .randint(start, final)

    @classmethod
    def randomise(cls,tab):
        return random \
            .choice(tab)

    @classmethod
    def randomiseCountryInfo(cls,tab,df):
        assert len(df) > 0, f"df expected a non-empty dataFrame, got {df}"
        assert len(tab) > 0, f"df expected a non-empty dataFrame, got {tab}"
        for i in range(len(df)):
            infos=random.choice(tab)
            df['Country'][i]=infos["name"]
            df['Flag'][i]=infos["flags"]

    @classmethod
    def x(cls, x):
        assert len(x) > 0, f"x expected a non-empty string, got {x}"
        x = x.split(' ')
        last_name = x[-1].upper()
        first_name = x[0].capitalize()
        x = ' '.join([first_name, last_name])
        return x

    @classmethod
    def concatData(cls, x,y,z):
        assert len(x) > 0, f"x expected a non-empty list, got {x}"
        assert len(y) > 0, f"y expected a non-empty list, got {y}"
        assert len(z) > 0, f"z expected a non-empty list, got {z}"
        add=x+y+z
        return add

    @classmethod
    def convertDevise(cls, df1, df2):
        assert len(df1) > 0, f"df expected a non-empty dataFrame, got {df1}"
        assert len(df2) > 0, f"df expected a non-empty dataFrame, got {df2}"
        for i in range(len(df2)):
            for j in range(len(df1)):
                if df1['Devise'][j]== df2['Devise'][i]:
                    df1["XOF Value"][j]=int(df1['salary'][j])*int(df2['Achat'][i])
        return df1
    @classmethod
    def organizeData(cls):
        apiData=DataBase.selectApiData("DATACOLLECTIONEXERCISE")
        tab=[]
        for i in apiData:
            datas=list(i)
            tab.append(
                {
                    "Person":{
                        "name":datas[0],
                        "phone":datas[1],
                        "email":datas[2],
                        "age":datas[6],
                        "Adress":datas[3],
                        "latlng":datas[4]
                    },
                    'income':{
                        "salary":datas[5],
                        "XOF Value":datas[7],
                        "devise":datas[10],
                    },
                    'country':{
                        "name":datas[8],
                        "flag":datas[9],
                    }
                    
                }
            )
        return tab
