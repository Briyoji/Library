import requests
from bs4 import BeautifulSoup
from csv import writer

# def handle_mult()

with open('data.csv', 'a', newline='') as f: 
    writer_obj = writer(f)
    for id in range(6391, 6425) : 
        url = f"https://library.plaksha.edu.in/cgi-bin/koha/opac-detail.pl?biblionumber={id}"

        data = []

        content = requests.get(url)
        htmlContent = content.content

        
        soup = BeautifulSoup(htmlContent, 'html.parser')
        
        data.append(f"00{id}")

        pg_nos = soup.find_all('span', property='description')
        if len(pg_nos) > 0 : 
            for pg_no in pg_nos :
                pages = pg_no.get_text().strip() 
                data.append(pages if pages != "" else " ")
        else : 
            data.append(" ")

        id_nos = soup.find_all('td', property='serialNumber')
        for id_no in id_nos : 
            data.append(id_no.get_text().strip())

        call_signs = soup.find_all('td', property='sku')
        for call_sign in call_signs : 
            data.append(call_sign.contents[0][:-1].strip())

        statuses = soup.find_all('span', class_='item-status available')
        for status in statuses : 
            data.append(status.get_text().strip())
        if "Available" not in data : data.append("Checked Out")
    
        writer_obj.writerow(data)
        print(data, len(data))

