from faker import Faker
from random import randint, choice
from sqlalchemy import select

from source.db_connect import session
from source.models import Teacher, Student, Discipline, Grade, Group

COUNT_STUDENTS = 50
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

def seed_groups():
    for group in LIST_GROUPS:
            session.add(Group(name=group))
    session.commit()

    
def seed_students():
    group_ids = session.scalars(select(Group.id)).all()
    for _ in range(COUNT_STUDENTS):
        student = Student(
            fullname=fake.name(),
            email=fake.ascii_free_email(),
            phone_number=fake.phone_number(),
            group_id=choice(group_ids)
        )
        session.add(student)
    session.commit()


def seed_teachers():
    for _ in range(COUNT_TEACHERS):
        teacher = Teacher(
            fullname=fake.name(),
            email=fake.ascii_free_email(),
            phone_number=fake.phone_number(),
        )
        session.add(teacher)
    session.commit()


def seed_disciplines():
    teacher_ids = session.scalars(
            select(Teacher.id)
        ).all()  
    for discipline in LIST_DISCIPLINES:
        session.add(Discipline(name=discipline, teacher_id=choice(teacher_ids)))
    session.commit()



def seed_grades():
    discipline_ids = session.scalars(select(Discipline.id)).all()
    student_ids = session.scalars(select(Student.id)).all()
    for _ in range(COUNT_GRADES):
        for student_id in range(1, COUNT_GRADES+1):
            date = fake.date_between(start_date='-1y', end_date='today')
            grade = Grade(
                grade=randint(37, 100),
                date_of=date,
                student_id=choice(student_ids),
                discipline_id=choice(discipline_ids)
            )
            session.add(grade)
    session.commit()


if __name__ == "__main__":
    fake = Faker('uk-UA')
    seed_groups()
    seed_students()
    seed_teachers()
    seed_disciplines()
    seed_grades()