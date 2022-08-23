import random


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
        for i in range(len(df)):
            infos=random.choice(tab)
            df['Country'][i]=infos["name"]
            df['Flag'][i]=infos["flags"]

    @classmethod
    def x(cls, x):
        x = x.split(' ')
        last_name = x[-1].upper()
        first_name = x[0].capitalize()
        x = ' '.join([first_name, last_name])
        return x

    @classmethod
    def concatData(cls, x,y,z):
        add=x+y+z
        return add

    @classmethod
    def convertDevise(cls, df1, df2):
        for i in range(len(df2)):
            for j in range(len(df1)):
                if df1['Devise'][j]== df2['Devise'][i]:
                    df1["XOF Value"][j]=int(df1['salary'][j])*int(df2['Achat'][i])
        return df1