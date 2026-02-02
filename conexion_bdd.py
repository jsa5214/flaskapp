import mysql.connector

def conectar_bdd():
    conexion = mysql.connector.connect(
        host="localhost",
        user="joelsansi",
        password="1234",
        database="practica"
    )
    cursor = conexion.cursor()
    return conexion, cursor


def consulta_email(cursor, nombre):
    sql = "SELECT email FROM nom_email WHERE nombre = %s"
    cursor.execute(sql, (nombre,))
    return cursor.fetchone()


def insertar_email(conexion, cursor, nombre, email):
    sql = "INSERT INTO nom_email (nombre, email) VALUES (%s, %s)"
    cursor.execute(sql, (nombre, email))
    conexion.commit()
