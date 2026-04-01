import sqlite3

conn = sqlite3.connect('FIAP.db')

cursor = conn.cursor()

cursor.execute('SELECT * FROM alunos')

alunos = cursor.fetchall()

for alunos in alunos:
    print(alunos)

conn.close