from asyncio.windows_events import NULL
import mysql.connector
import pandas as pd

class DataBase(object):

    @classmethod
    def createDB(cls, dbName):
        assert len(dbName) > 0, f"db expected a non-empty string, got {dbName}"
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )

        mycursor = mydb.cursor()
        mycursor.execute(f"CREATE DATABASE {dbName}")
    
    @classmethod
    def insertCountry(cls, df, db):
        assert len(db) > 0, f"db expected a non-empty string, got {db}"
        assert len(df) > 0, f"df expected a non-empty dataFrame, got {df}"
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database= db
        )

        mycursor = mydb.cursor()
        val=[]
        for i in range(len(df)):
            country=df["name"][i]
            flag=df["flags"][i]
            val.append((country, flag))
        sql = "INSERT INTO country (name, flag) VALUES (%s, %s)"
        mycursor.executemany(sql,val)
        mydb.commit()
    
    @classmethod
    def insertCustommers(cls, df, db):
        assert len(db) > 0, f"db expected a non-empty string, got {db}"
        assert len(df) > 0, f"df expected a non-empty dataFrame, got {df}"
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database= db
        )
        mycursor = mydb.cursor()
        countryColumn=["Key", "Country", "Flag"]
        deviseColumns=["Key", 'Devise', "Buy", 'Sale']
        deviseData=pd.DataFrame(cls.select('DATACOLLECTIONEXERCISE','devises'),columns=deviseColumns)
        countryData=pd.DataFrame(cls.select('DATACOLLECTIONEXERCISE','country'),columns=countryColumn)
        countryData=countryData.astype({'Key':'int'})
        deviseData=deviseData.astype({'Key':'int'})
        val=[]
        for i in range(len(df)):
            for j in range(len(deviseData)):
                if deviseData["Devise"][j]==df["Devise"][i]:
                    df["Devise"][i]=deviseData["Key"][j]
            for k in range(len(countryData)):
                if countryData["Country"][k]==df["Country"][i]:
                    df["Country"][i]=countryData["Key"][k]
            val.append((df["name"][i], df["phone"][i], df["email"][i], df["address"][i], df["latlng"][i], str(df["salary"][i]), str(df["age"][i]), str(df["XOF Value"][i]), str(df["Devise"][i]), str(df["Country"][i])))
        sql = "INSERT INTO customers( \
                    name, phone, email, address, latlng, salary, age, XOF, deviseId, countryId\
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        mycursor.executemany(sql,val)
        mydb.commit() 

    @classmethod
    def insertDevises(cls, df, db):
        assert len(db) > 0, f"db expected a non-empty string, got {db}"
        assert len(df) > 0, f"df expected a non-empty dataFrame, got {df}"
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database= db
        )

        mycursor = mydb.cursor()
        val=[]
        for i in range(len(df)):
            devise=df["Devise"][i]
            achat=df["Achat"][i]
            vente=df["Vente"][i]
            val.append((devise, achat, vente))
        sql = "INSERT INTO devises (name, buy, sale) VALUES (%s, %s, %s)"
        mycursor.executemany(sql,val)
        mydb.commit()  

    @classmethod
    def selectApiData(cls, db):
        assert len(db) > 0, f"db expected a non-empty string, got {db}"
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database= db
        )

        mycursor = mydb.cursor()
        mycursor.execute(\
            f"Select\
                customers.name, \
                customers.phone, \
                customers.email, \
                customers.address, \
                customers.latlng, \
                customers.salary, \
                customers.age, \
                customers.XOF, \
                country.name, \
                country.flag, \
                devises.name \
                from \
                customers \
                INNER JOIN devises ON customers.deviseId = devises.id \
                INNER JOIN country ON customers.countryId = country.id \
                ")
        return mycursor.fetchall()

    @classmethod
    def CreateCustomerTable(cls, db):
        assert len(db) > 0, f"db expected a non-empty string, got {db}"
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database= db
        )

        mycursor = mydb.cursor()
        mycursor.execute(
            "CREATE TABLE \
                customers ( \
                    id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, \
                        phone VARCHAR(55) NOT NULL, \
                        email VARCHAR(55) NOT NULL, \
                        address VARCHAR(255), \
                        latlng VARCHAR(255), \
                        salary FLOAT NOT NULL, \
                        age INT NOT NULL, \
                        XOF INT NOT NULL,\
                        deviseId INT NOT NULL,\
                        countryId INT NOT NULL,\
                        CONSTRAINT fk_devise FOREIGN KEY (deviseId) REFERENCES devises(id) ON UPDATE CASCADE ON DELETE CASCADE,\
                        CONSTRAINT fk_country FOREIGN KEY (countryId) REFERENCES country(id) ON UPDATE CASCADE ON DELETE CASCADE\
                )ENGINE=InnoDB"
        )
    
    @classmethod
    def CreateCountryTable(cls, db):
        assert len(db) > 0, f"db expected a non-empty string, got {db}"
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database= db
        )

        mycursor = mydb.cursor()
        mycursor.execute(
            "CREATE TABLE country ( \
                id INT AUTO_INCREMENT PRIMARY KEY, \
                name VARCHAR(255) NOT NULL, \
                flag VARCHAR(255) \
            )ENGINE=InnoDB"
        )
    
    @classmethod
    def CreateDevisesTable(cls, db):
        assert len(db) > 0, f"db expected a non-empty string, got {db}"
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database= db
        )

        mycursor = mydb.cursor()
        mycursor.execute(
            "CREATE TABLE devises ( \
                id INT AUTO_INCREMENT PRIMARY KEY, \
                name VARCHAR(255) NOT NULL, \
                buy FLOAT NOT NULL, \
                sale FLOAT NOT NULL\
            )ENGINE=InnoDB"
        )