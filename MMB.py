import requests
import xml.etree.ElementTree as ET

##берем xml с сайта ММВБ
url = 'https://iss.moex.com/iss/engines/futures/markets/forts/boards/RFUD/securities/SiZ2.xml'
root = ET.fromstring(requests.get(url).content)

##так через файл
##tree=ET.parse('SiZ2.xml')
##root=tree.getroot ()

Price=root.find("data[2]/rows[1]/row[1]").attrib.get("LAST")
print ("Последняя цена фьючерса SiZ2 = "+Price)
