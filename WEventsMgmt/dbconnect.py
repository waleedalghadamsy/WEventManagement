import psycopg2

def postgresConnect():
    conn = psycopg2.connect(database="djeventsmgmtdb", 
                            host="localhost", 
                            port="5432", 
                            user="waleed", 
                            password="AbcXyz123")
    return conn.cursor()
