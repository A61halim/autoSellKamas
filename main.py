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
['Monocompte IX',15], 
['Monocompte VII',16], 
['Monocompte X ',17],
['Nidas',18],
['Ombre(Shadow)',19], 
['Oto Mustam',20],
['Pandore',21],
['Rubilax',22],
['Temporis I ',23],
['Temporis II',24] ,
['Thanatena',25 ],
['USH',26]]
print(tabulate(ser))
s = int(input('Enter the number for your Server: '))



loop.boucle(server_list[ser[s-1][0]])
