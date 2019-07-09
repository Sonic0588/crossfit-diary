import sqlite3

conn = sqlite3.connect("crossfit-diary.db")



# sql = '''
# 	CREATE TABLE IF NOT EXISTS days (
# 	date TEXT NOT NULL,
# 	skill_id INT NOT NULL,
# 	wod_id INT NOT NULL,
# 	FOREIGN KEY (skill_id) REFERENCES skills(ROWID),
# 	FOREIGN KEY (wod_id) REFERENCES wods(ROWID)
# 	);

# 	CREATE TABLE IF NOT EXISTS skills (
# 	type TEXT NOT NULL,
# 	timecap TEXT NOT NULL,
# 	FOREIGN KEY (type) REFERENCES type_complex(ROWID)
# 	);

# 	CREATE TABLE IF NOT EXISTS wods (
# 	type TEXT NOT NULL,
# 	timecap TEXT NOT NULL,
# 	FOREIGN KEY (type) REFERENCES type_complex(ROWID)
# 	);

# 	CREATE TABLE IF NOT EXISTS type_complex (
# 	name TEXT NOT NULL,
# 	);

# 	CREATE TABLE IF NOT EXISTS rounds (
# 	skill_id INT NOT NULL,
# 	wod_id INT NOT NULL,
# 	FOREIGN KEY (skill_id) REFERENCES skills(ROWID),
# 	FOREIGN KEY (wod_id) REFERENCES wods(ROWID)
# 	);

# 	CREATE TABLE IF NOT EXISTS exercise (
# 	round_id INT NOT NULL,
# 	repeats INT NOT NULL,
# 	weight INT NOT NULL,
# 	name TEXT NOT NULL,
# 	FOREIGN KEY (round_id) REFERENCES rounds(ROWID),
# 	);

# '''