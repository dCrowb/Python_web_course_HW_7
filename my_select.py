from sqlalchemy import func, desc

from source.db_connect import session
from source.models import Teacher, Student, Discipline, Grade, Group

def select_1():
    result = (
        session.query(
            Student.fullname, func.round(func.avg(Grade.grade), 1).label("avg_grade")
        )
        .select_from(Grade)
        .join(Student)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(5)
        .all()
    )
    return result


def select_2(discipline_id: int):
    result = (
        session.query(
            Discipline.name,
            Student.fullname,
            func.round(func.avg(Grade.grade), 1).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Student)
        .join(Discipline)
        .filter(Discipline.id == discipline_id)
        .group_by(Student.id, Discipline.name)
        .order_by(desc("avg_grade"))
        .limit(1)
        .all()
    )
    return result


def select_3(discipline_id: int):
    result = (
        session.query(
            Group.name,
            Discipline.name,
            func.round(func.avg(Grade.grade), 1).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Student)
        .join(Group)
        .join(Discipline)
        .filter(Discipline.id == discipline_id)
        .group_by(Group.name, Discipline.name)
        .order_by("avg_grade")
        .all()
    )
    return result


def select_4():
    result = (
        session.query(func.round(func.avg(Grade.grade), 1)).select_from(Grade).all()
    )
    return result


def select_5(teacher_id: int):
    result = (
        session.query(Teacher.fullname, Discipline.name)
        .select_from(Teacher)
        .join(Discipline)
        .filter(Teacher.id == teacher_id)
        .group_by(Teacher.fullname, Discipline.name)
        .order_by(Discipline.name)
        .all()
    )
    return result


def select_6(group_id: int):
    result = (
        session.query(Group.name, Student.fullname)
        .select_from(Group)
        .join(Student)
        .filter(Group.id == group_id)
        .group_by(Group.name, Student.fullname)
        .order_by(Student.fullname)
        .all()
    )
    return result


def select_7(group_id: int, discipline_id: int):
    result = (
        session.query(Group.name, Discipline.name, Grade.grade)
        .select_from(Group)
        .join(Student)
        .join(Grade)
        .join(Discipline)
        .filter(Group.id == group_id)
        .filter(Discipline.id == discipline_id)
        .group_by(Group.name, Discipline.name, Grade.grade)
        .all()
    )
    return result


def select_8(teacher_id: int):
    result = (
        session.query(
            Teacher.fullname,
            Discipline.name,
            func.round(func.avg(Grade.grade), 1).label("avg_grade"),
        )
        .select_from(Discipline)
        .join(Teacher)
        .join(Grade)
        .filter(Teacher.id == teacher_id)
        .group_by(Teacher.fullname, Discipline.name)
        .order_by("avg_grade")
        .all()
    )
    return result


def select_9(student_id: int):
    result = (
        session.query(Student.fullname, Discipline.name)
        .select_from(Grade)
        .join(Student)
        .join(Discipline)
        .filter(Student.id == student_id)
        .group_by(Student.fullname, Discipline.name)
        .order_by(Student.fullname)
        .all()
    )
    return result


def select_10(student_id: int, teacher_id: int):
    result = (
        session.query(Student.fullname, Teacher.fullname, Discipline.name)
        .select_from(Grade)
        .join(Student)
        .join(Discipline)
        .join(Teacher)
        .filter(Teacher.id == teacher_id)
        .filter(Student.id == student_id)
        .group_by(Student.fullname, Teacher.fullname, Discipline.name)
        .order_by(Discipline.name)
        .all()
    )
    return result


if __name__ == "__main__":
    print(f'select_1 result:\n{select_1()}\n')
    print(f'select_2 result:\n{select_2(4)}\n')
    print(f'select_3 result:\n{select_3(6)}\n')
    print(f'select_4 result:\n{select_4()}\n')
    print(f'select_5 result:\n{select_5(4)}\n')
    print(f'select_6 result:\n{select_6(2)}\n')
    print(f'select_7 result:\n{select_7(1, 6)}\n')
    print(f'select_8 result:\n{select_8(2)}\n')
    print(f'select_9 result:\n{select_9(32)}\n')
    print(f'select_10 result:\n{select_10(41, 3)}\n')
