import json
import requests

URL = 'https://restcountries.com/v3.1/all'


class ApiGetter(object):
    @classmethod
    def apiFetcher(cls):
        result = requests.get(URL)
        return result.text

    @classmethod
    def getNameAndFlag(cls):
        countries=[]
        result = json.loads(cls.apiFetcher())
        for i in result:
            countries.append({
                "name":i['name']['official'],
                "flags":i["flags"]["png"]
            })
        return countries