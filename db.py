
def create_db(conn):
	with conn:
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
			skill_id INT,
			wod_id INT,
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

def input_skills(conn, skill_timecap, skill_type):
	with conn:
		cursor = conn.cursor()
		cursor.execute('''
			INSERT INTO skills ('timecap', 'type')
			SELECT ? as timecap, ROWID FROM type_complex 
			WHERE name = ?
		''', (skill_timecap, skill_type))

def input_wods(conn, wod_timecap, wod_type):
	with conn:
		cursor = conn.cursor()
		cursor.execute('''
			INSERT INTO wods ('timecap', 'type')
			SELECT ? as timecap, ROWID FROM type_complex 
			WHERE name = ?
		''', (wod_timecap, wod_type))

def get_id(conn, table):
	with conn:
		cursor = conn.cursor()
		return cursor.execute(f"SELECT ROWID FROM {table} ORDER BY ROWID DESC LIMIT 1")