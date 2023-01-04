def create_data_row(id, id_nos, pg_nos, call_s, avails, count) : 
    data = [f'00{id}']

    # if len(avails) 


    id_no = id_nos[count].get_text().strip()
    
    pages = pg_nos.get_text().strip() 
    pg_no = pages if pages != "" else " "

    call_sign = call_s[count].contents[0][:-1].strip()
    
    availability = 'Checked_Out' if avails[count].get_text().strip() != 'Available' else 'Available'
    data.extend([id_no, pg_no, call_sign, availability])
    print(','.join(data))
    return ','.join(data)