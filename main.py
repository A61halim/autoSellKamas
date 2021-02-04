from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from notify import notification
from server import server
from tabulate import tabulate
from dictionnary import server_list
from loop import loop
import time

ser = [['Agride',1],
['Atcham',2],
['Boune',3],
['Brumen',3],
['Crail',4],
['Echo',5],
['Eratz',6],
['Furye',7],
['Galgarion',8],
['Henual',9],
['Ilyzaelle',10],
['Jahash',11],
['Julith',12],
['Meriana',13],
['Merkator',14],
['Nidas',15],
['Ombre(Shadow)',16], 
['Oto Mustam',17],
['Pandore',18],
['Rubilax',19],
['Temporis I ',20],
['Temporis II',21] ,
['Thanatena',22],
['USH',23]]
print(tabulate(ser))
s = int(input('Enter the number for your Server: '))



loop.boucle(server_list[ser[s-1][0]])
