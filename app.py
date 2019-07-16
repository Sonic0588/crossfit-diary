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

db.input_wods(conn, wod_timecap, wod_type)

[skill_id], = db.get_id(conn, "skills")
[wod_id], = db.get_id(conn, "wods")

# cursor.execute('''
# 	INSERT INTO days ('date', 'skill_id', 'wod_id')
# 	VALUES (?, ?, ?)
# ''', (date, skill_id, wod_id))

# cursor.execute('''
# 	INSERT INTO rounds ('skill_id')
# 	VALUES (?)
# 	''', (skill_id,))

# cursor.execute('''
# 	INSERT INTO rounds ('wod_id')
# 	VALUES (?)
# 	''', (wod_id,))

# conn.commit()

# skill_round_time = input("Время подхода навыка")
# skill_exercise = input("Название упражнения")
# skill_rounds = []
# for count in range(5):
# 	skill_rounds_masse = int(input("Масса подхода навыка"))
# 	skill_rounds.append((date, skill_type,))