# testing 45

import requests
import json
import datetime
import psycopg2
import time
import sys

dtoday = datetime.datetime.now()
dtd = dtoday.strftime('%Y-%m-%d')
param = sys.argv[1]

from datetime import datetime, timedelta
specdate = datetime(2015, 5, 1)
spd = specdate.strftime('%Y-%m-%d')
endspecdate = datetime(2015, 7, 30)
spend = endspecdate.strftime('%Y-%m-%d')

con = psycopg2.connect(
  database="[your_database_name]",
  user="[your_database_username]",
  password="[your_database_password]",
  host="127.0.0.1",
  port="5432"
)
print('Соединение открыто успешно')


while specdate < dtoday:

    responsed = 'http://api.spending.gov.ua/api/v2/api/transactions/?payers_edrpous=' + str(param) + '&startdate=' + str(spd) + '&enddate=' + str(spend)
    print('...... формирую ссылку для парсинга')
    print(responsed)
    print(param)

    response = requests.get(responsed)
    data = response.text
    parsed = json.loads(data)

    for transact in parsed:

        ntr = transact['id']
        doc_vob = transact['doc_vob']
        doc_vob_name = transact['doc_vob_name']
        doc_number = transact['doc_number']
        doc_date = transact['doc_date']
        doc_v_date = transact['doc_v_date']
        trans_date = transact['trans_date']
        amount = transact['amount']
        amount_cop = transact['amount_cop']
        currency = transact['currency']
        payer_edrpou = transact['payer_edrpou']
        payer_name = transact['payer_name']
        payer_account = transact['payer_account']
        payer_mfo = transact['payer_mfo']
        payer_bank = transact['payer_bank']
        recipt_edrpou = transact['recipt_edrpou']
        recipt_name = transact['recipt_name']
        recipt_account = transact['recipt_account']
        recipt_bank = transact['recipt_bank']
        recipt_mfo = transact['recipt_mfo']
        payment_details = transact['payment_details']
        doc_add_attr = transact['doc_add_attr']
        region_id = transact['region_id']
        payment_type = transact['payment_type']
        payment_data = transact['payment_data']
        source_id = transact['source_id']
        source_name = transact['source_name']

        print(ntr)
        print('Платник:', payer_name)
        print('Сума:', amount, currency)
        print('Одержувач:', recipt_name)
        print(payment_details)

        cur = con.cursor()
        sql = "INSERT INTO transaction (id, doc_vob, doc_vob_name, doc_number, doc_date, doc_v_date, trans_date, amount, amount_cop,currency, payer_edrpou, payer_name, payer_account, payer_mfo, payer_bank, recipt_edrpou, recipt_name, recipt_account, recipt_bank, recipt_mfo, payment_details, doc_add_attr, region_id, payment_type, payment_data, source_id, source_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s) ON CONFLICT (id) DO NOTHING;"
        data = (ntr, doc_vob, doc_vob_name, doc_number, doc_date, doc_v_date, trans_date, amount, amount_cop, currency, payer_edrpou, payer_name, payer_account, payer_mfo, payer_bank, recipt_edrpou, recipt_name, recipt_account, recipt_bank, recipt_mfo, payment_details, doc_add_attr, region_id, payment_type, payment_data, source_id, source_name)
        cur.execute(sql, data)

        print('Запрос выполнен успешно!')
        print('______________________________________________')
    con.commit()# это обязательно, иначе запрос не пойдет в таблицу
    print('Засыпаю на 2 секунды')
    time.sleep(2)# дабы избежать блокировки по количеству запросов, длительность можно уменьшить


    specdate = specdate + timedelta(days=90)
    spd = specdate.strftime('%Y-%m-%d')
    spende = endspecdate + timedelta(days=90)
    endspecdate = spende
    spend = endspecdate.strftime('%Y-%m-%d')
con.close()
print('========================================================================')
print('========================================================================')
print('Соединение закрыто')
print('Импорт завершен успешно')
