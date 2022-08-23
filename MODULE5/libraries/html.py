import json
from .utils import Utils
from bs4 import BeautifulSoup


BASE_URL = 'DATABASES/data-zIybdmYZoV4QSwgZkFtaB.html'


class HtmlFactory(object):
    @classmethod
    def openFile(cls):
        with open(BASE_URL) as file:
            data = file.read()
            data = BeautifulSoup(
                data,
                'html.parser')
            file.close()
        return data
    
    @classmethod
    def listObject(cls):
        data=cls.openFile()
        tab=[]
        tr=data.find_all('tr')
        for i in tr[1:]:
            td=i.find_all('td')
            naming=td[0].text.split(' ')
            tab.append(
                {
                    'name': f'{naming[0]} {naming[-1].upper()}', 
                    'phone': td[1].text, 
                    'email': td[2].text, 
                    'address': '', 
                    'latlng': td[3].text, 
                    'salary': td[4].text, 
                    'age': td[5].text
                }
            )
        return tab

    @classmethod
    def main(cls):
        data=cls.listObject()
        return data
        
        
            