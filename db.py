import psycopg2


def connection():
    connect = None
    try:
        connect = psycopg2.connect(
            host="localhost",
            port="5432",
            database="postgres",
            user="postgres",
            password="GhbdtnDkfl")

        cursor = connect.cursor()
        cursor.close()

        return connect
    except (Exception, psycopg2.DatabaseError) as error:
        print(error, "Error")


connection()
