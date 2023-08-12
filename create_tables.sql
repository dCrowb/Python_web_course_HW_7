-- Create students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(30),
	last_name VARCHAR(30),
    email VARCHAR(50) UNIQUE NOT NULL,
    phone_number VARCHAR(20) UNIQUE NOT NULL,
	group_id REFERENCES [groups] (id)

);
-- Create groups
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name STRING UNIQUE NOT NULL
);
-- Create teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(20),
	last_name VARCHAR(30),
    email VARCHAR(30) UNIQUE NOT NULL,
    phone VARCHAR(30) UNIQUE NOT NULL
);
-- Create disciplines
DROP TABLE IF EXISTS disciplines;
CREATE TABLE disciplines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(30),
	teacher_id REFERENCES teachers (id)
);
-- Create grades
DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id REFERENCES students (id),
    discipline_id REFERENCES disciplines (id),
	grade INTEGER,
	date_of DATE
);