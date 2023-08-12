import sqlite3
from faker import Faker
from random import randint


COUNT_STUDENTS = 50
COUNT_GROUPS = 3
COUNT_TEACHERS = 5
COUNT_GRADES = 20
LIST_GROUPS = ['УІБ-11', 'УІБ-21', 'УІБ-31']
LIST_DISCIPLINES = ['Управління ризиками',
                    'СПЗ',
                    'КСЗІ',
                    'СРМ',
                    'Комп\'ютерна графіка',
                    'УІБ',
                    'Філософія',
                    'Мережі'
                    ]


def seed_students():
    sql = 'INSERT INTO students (first_name, last_name, email, phone_number, group_id) VALUES (?, ?, ?, ?, ?)'

    for _ in range(COUNT_STUDENTS):
        cur.execute(sql, (fake.first_name(), fake.last_name(), fake.email(), fake.phone_number(), randint(1, COUNT_GROUPS)))
    con.commit()


def seed_groups():
    sql = 'INSERT INTO groups (name) VALUES (?)'
    
    for group_name in LIST_GROUPS:
        cur.execute(sql, (group_name,))
        con.commit()


def seed_teachers():
    sql = 'INSERT INTO teachers (first_name, last_name, email, phone) VALUES (?, ?, ?, ?)'

    for _ in range(1, COUNT_TEACHERS+1):
        cur.execute(sql, (fake.first_name(), fake.last_name(), fake.email(), fake.phone_number()))
    con.commit()


def seed_disciplines():
    sql = 'INSERT INTO disciplines (name, teacher_id) VALUES (?, ?)'
    
    for discipline_name in LIST_DISCIPLINES:
        cur.execute(sql, (discipline_name, randint(1, COUNT_TEACHERS)))
    con.commit()


def seed_grades():
    sql = 'INSERT INTO grades (discipline_id, student_id, grade, date_of) VALUES(?, ?, ?, ?)'
    
    for _ in range(COUNT_GRADES):
        for student_id in range(1, COUNT_GRADES+1):
            date = fake.date_between(start_date='-1y', end_date='today')
            cur.execute(sql, (randint(1, len(LIST_DISCIPLINES)), student_id, randint(1, 100), date))
    con.commit()



def create_db():
    with open('create_tables.sql', 'r') as sql_file:
        sql = sql_file.read()

    with sqlite3.connect('crow.db') as con:
        cur = con.cursor()
        cur.executescript(sql)


if __name__ == "__main__":
    fake = Faker('uk-UA')
    con = sqlite3.connect('crow.db')
    cur = con.cursor() 
    create_db()
    seed_students()
    seed_groups()
    seed_teachers()
    seed_disciplines()
    seed_grades()
