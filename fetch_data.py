'''
Arg1 -> starting biblionumber
Arg2 -> ending biblionumber
Arg3 -> instance number 

Outputs : 
    - data-<instance>.csv
    - checked_out-<instance>.csv
    - unavailable_pgnos-<instance>.csv
    - duplicates-<instance>.csv

Returns -> None
'''

import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from helpers.make_data_row import *

def fetch_lib_data(from_bib_no : int, to_bib_no : int, instance : int) -> None : 
    data_dir = f'./data_files/{instance}_data'
    if not os.path.exists(data_dir) : os.mkdir(data_dir)
    

    with open(f'{data_dir}/data.csv', 'a') as f: 
        f.write('biblionumber,idnumber,page number,call sign,availability')

        for id in range(from_bib_no, to_bib_no+1) : 
            url = f'https://library.plaksha.edu.in/cgi-bin/koha/opac-detail.pl?biblionumber={id}'     
            try : 
                response = requests.get(url)
            except Exception as e : 
                print(f'An Error Occured : \n{e}')
                break 

            df = pd.DataFrame

            # Checking for the status code fo the request response.
            if response.status_code == 200 :  # Status 200 -> Success
                html_content = response.content
                soup = BeautifulSoup(html_content, 'html.parser')

                # Finding Elements 
                # id_nos = soup.find_all('td', property='serialNumber')
                pg_nos = soup.find('span', property='description')
                t_rows = soup.find_all('tr', {'typeof':'Offer'})

                for row in t_rows :
                    # Find all cells in the row
                    cells = row.find_all('td')
                    cells = [cell.text.replace('(Browse shelf)', ' ').strip() for cell in cells]
                    # Print the cell data
                    print(cells)
                    print(','.join([cells[3], cells[4], cells[6]]))



                #  call_s = soup.find_all('td', property='sku')
                # avails = soup.find_all('span', class_='item-status available')

                # print(id_nos, pg_nos, call_s, avails)

                # if len(id_nos) >= 1 : 
                #     for count in range(len(id_nos)) :
                #         create_data_row(id, id_nos, pg_nos, call_s, avails, count)



            

fetch_lib_data(6463, 6465, 1)