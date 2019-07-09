import sqlite3

conn = sqlite3.connect("crossfit-diary.db")
cursor = conn.cursor()

cursor.execute('''
	CREATE TABLE IF NOT EXISTS days (
	ROWID INTEGER NOT NULL,
	date TEXT NOT NULL,
	skill_id INT NOT NULL,
	wod_id INT NOT NULL,
	PRIMARY KEY(ROWID),
	FOREIGN KEY (skill_id) REFERENCES skills(ROWID),
	FOREIGN KEY (wod_id) REFERENCES wods(ROWID)
	);'''
)

cursor.execute('''CREATE TABLE IF NOT EXISTS skills (
	ROWID INTEGER NOT NULL,
	type TEXT NOT NULL,
	timecap TEXT NOT NULL,
	PRIMARY KEY(ROWID),
	FOREIGN KEY (type) REFERENCES type_complex(ROWID)
	);'''
)

cursor.execute('''
	CREATE TABLE IF NOT EXISTS wods (
	ROWID INTEGER NOT NULL,
	type TEXT NOT NULL,
	timecap TEXT NOT NULL,
	PRIMARY KEY(ROWID),
	FOREIGN KEY (type) REFERENCES type_complex(ROWID)
	);'''
)

cursor.execute('''
	CREATE TABLE IF NOT EXISTS type_complex (
	ROWID INTEGER NOT NULL,
	name TEXT NOT NULL,
	PRIMARY KEY(ROWID)
	);'''
)

cursor.execute('''
	CREATE TABLE IF NOT EXISTS rounds (
	ROWID INTEGER NOT NULL,
	skill_id INT NOT NULL,
	wod_id INT NOT NULL,
	PRIMARY KEY(ROWID),
	FOREIGN KEY (skill_id) REFERENCES skills(ROWID),
	FOREIGN KEY (wod_id) REFERENCES wods(ROWID)
	);'''
)

cursor.execute('''
	CREATE TABLE IF NOT EXISTS exercise (
	ROWID INTEGER NOT NULL,
	round_id INT NOT NULL,
	repeats INT NOT NULL,
	weight INT NOT NULL,
	name TEXT NOT NULL,
	PRIMARY KEY(ROWID),
	FOREIGN KEY (round_id) REFERENCES rounds(ROWID)
	);'''
)

# date = input("Дата: ")
skill_type = input("Тип навыка ")
skill_timecap = input("Время навыка ")

cursor.execute('''
	INSERT INTO skills ('timecap', type)
	SELECT ? as timecap, ROWID FROM type_complex 
	WHERE name = ?
''', (skill_timecap, skill_type))

conn.commit()

# skill_round_time = input("Время подхода навыка")
# skill_exercise = input("Название упражнения")
# skill_rounds = []
# for count in range(5):
# 	skill_rounds_masse = int(input("Масса подхода навыка"))
# 	skill_rounds.append((date, skill_type,))