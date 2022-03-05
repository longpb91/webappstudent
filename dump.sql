CREATE TABLE IF NOT EXISTS add_teachers (
teacherid SERIAL PRIMARY KEY,
teachername VARCHAR(200),
teachsubject VARCHAR(200),
teachergender VARCHAR(200),
teacherclasses VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS add_subjects (
subjectid VARCHAR(10) PRIMARY KEY,
subjectname VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS add_classes (
classid VARCHAR(10) PRIMARY KEY,
classname VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS add_students (
studentid SERIAL PRIMARY KEY,
studentname VARCHAR(200),
studentgender VARCHAR(10),
class_ VARCHAR(200)
);

