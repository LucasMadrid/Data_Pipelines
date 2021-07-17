import requests
import psycopg2

with requests.get('http://127.0.0.1:5000/large_data_request/10000', stream=True) as read:
    print(read.text)

    conn = psycopg2.connect(dbname="stream_db",user="postgres", password="")

    cur = conn.cursor()
    sql = "INSERT INTO stream_transactions (transaction_id, user_id, amount) VALUES (%s,%s,%s)"

    buffer=""
    for chunk in read.iter_content(chunk_size=1):

        if chunk.endswith(b'\n'):
            tpl = eval(buffer)
            cur.execute(sql, (tpl[0], tpl[1], tpl[2]))
            conn.commit()
            print(tpl)
            buffer=""
        else:
            buffer += chunk.decode()