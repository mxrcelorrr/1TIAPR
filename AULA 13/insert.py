import sqlite3

conn = sqlite3.connect('FIAP.db')

cursor = conn.cursor()

cursor.execute('''
INSERT INTO alunos (nome, idade)
VALUES ('Augusto', 74) 
''')

conn.commit()