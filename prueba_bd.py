import psycopg2
#conexion a bd
conexion = psycopg2.connect(
    user='postgres',
    password ='ADMIN',
    host='127.0.0.1',
    port='5432',
    database='test_db')
try:
    with conexion:
        #crear cursor se sentencias sql
        with conexion.cursor() as cursor:
            #alojar consultas y ejecutarlas
            sentencias = 'SELECT *FROM persona'
            cursor.execute(sentencias)
            #alojar resultados de las consultas
            registros = cursor.fetchall()
            print(registros)
except Exception as e:
    print(f'ha ocurrido un error {e}')
finally:
    conexion.close()
    #actalizacion
    #actualixacion 2
    #acutalizacion 3
