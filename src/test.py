from src.app import db
from src.models import Students, Classes
import psycopg2


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
name = r"'Phạm Bảo Long'"
querry = f"SELECT * FROM add_students WHERE studentname={name}"
result = db.session.execute(querry)
print(result)
lst = []
for r in result:
    # print(r)
    # lst.append(r[1])
    lst.append(r)
print(lst)