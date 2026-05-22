import sqlite3

class conndb:
    def __init__(self):
        cnx = sqlite3.connect('mahasiswa.db')
        conn = cnx.cursor()
        conn.execute('''
            CREATE TABLE IF NOT EXISTS tbl_mahasiswa (
                nama TEXT,
                npm TEXT,
                kelas TEXT,
                jurusan TEXT
            )
        ''')
        cnx.commit()
        cnx.close()

    def queryResult(self,strsql):
        cnx = sqlite3.connect('mahasiswa.db')
        conn = cnx.cursor()
        conn.execute(strsql)
        result = conn.fetchall()
        cnx.close()
        return result

    def queryExecute(self, strsql):
        cnx = sqlite3.connect('mahasiswa.db') 
        conn = cnx.cursor()
        conn.execute(strsql)
        cnx.commit()
        cnx.close()