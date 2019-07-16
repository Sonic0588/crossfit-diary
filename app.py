import sqlite3
import db

# Создание Базы данных
conn = sqlite3.connect("crossfit-diary.db")

db.create_db(conn)

#Заполняю БД
date = "2019-07-16"
skill_type = "emom"
skill_timecap = '12'

db.input_skills(conn, skill_timecap, skill_type)

wod_type = "for_time"
wod_timecap = '15'



cursor.execute('''
	INSERT INTO wods ('timecap', 'type')
	SELECT ? as timecap, ROWID FROM type_complex 
	WHERE name = ?
''', (wod_timecap, wod_type))


[skill_id], = cursor.execute("SELECT ROWID FROM skills ORDER BY ROWID DESC LIMIT 1")
[wod_id], = cursor.execute("SELECT ROWID FROM wods ORDER BY ROWID DESC LIMIT 1")

print(type(skill_id))
cursor.execute('''
	INSERT INTO days ('date', 'skill_id', 'wod_id')
	VALUES (?, ?, ?)
''', (date, skill_id, wod_id))

cursor.execute('''
	INSERT INTO rounds ('skill_id')
	VALUES (?)
	''', (skill_id,))

cursor.execute('''
	INSERT INTO rounds ('wod_id')
	VALUES (?)
	''', (wod_id,))

conn.commit()

# skill_round_time = input("Время подхода навыка")
# skill_exercise = input("Название упражнения")
# skill_rounds = []
# for count in range(5):
# 	skill_rounds_masse = int(input("Масса подхода навыка"))
# 	skill_rounds.append((date, skill_type,))