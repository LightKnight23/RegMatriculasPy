from datetime import date
from typing import List
from sqlalchemy.orm import Session
from ..models.models import Student, Course, Enrollment

def check_student_age(birth_date: date, min_age: int = 16) -> bool:
    """
    Check if student meets minimum age requirement
    """
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age >= min_age

def get_student_courses(db: Session, student_id: int) -> List[Course]:
    """
    Get all courses a student is enrolled in
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        return []
    return [enrollment.course for enrollment in student.enrollments]

def get_course_students(db: Session, course_id: int) -> List[Student]:
    """
    Get all students enrolled in a course
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        return []
    return [enrollment.student for enrollment in course.enrollments]

def get_course_availability(db: Session, course_id: int) -> int:
    """
    Get number of available slots in a course
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        return 0
    
    current_enrollments = db.query(Enrollment).filter(
        Enrollment.course_id == course_id
    ).count()
    
    return max(0, course.capacity - current_enrollments)
