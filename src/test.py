from src.app import db, app
from src.models import Students, Classes
import psycopg2

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# class_id = "cbide03".upper()
# # class_id.upper()
# compare = db.session.query(Classes).filter(Classes.classid == class_id)
# print(compare)

# x = Classes.query.filter_by(classname='Fresher_DE_01').first()
# print(x)
# result = db.session.execute("SELECT classname FROM add_classes")
# print(result)
# lst = []
# for r in result:
#     # print(r[0])
#     lst.append(r[0])
# print(lst)
name = "'Phạm Bảo Long'"
querry = f"SELECT * FROM add_students WHERE studentname={name}"
result = db.session.execute(querry)
# print(result)
lst = []
for r in result:
    # print(r)
    # lst.append(r[1])
    lst.append(r)
    # StudentID = r[0]
    # FullName = r[1]
    # Gender = r[2]
    # Class_ = r[3]
# print(lst)
# print(lst[0][0])
# print(StudentID, FullName, Gender, Class_)
x = tuple(lst)
print(x[0][0])