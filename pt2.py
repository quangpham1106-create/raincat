import pandas as pd
students = pd.read_csv("students.csv")
majors = pd.read_csv("majors.csv")
# Hiển thị 5 dòng đầu tiên của mỗi bảng
print("Students:")
print(students.head())
print("\nMajors:")
print(majors.head())

# Số dòng và số cột
print("\nSố dòng và số cột của bảng Students:")
print(students.shape)
print("\nSố dòng và số cột của bảng Majors:")
print(majors.shape)

# Tên các cột
print("\nTên các cột của bảng Students:")
print(students.columns.tolist())
print("\nTên các cột của bảng Majors:")
print(majors.columns.tolist())

# Kiểu dữ liệu của từng cột
print("\nKiểu dữ liệu của từng cột trong bảng Students:")
print(students.dtypes)
print("\nKiểu dữ liệu của từng cột trong bảng Majors:")
print(majors.dtypes)

# Kiểm tra các giá trị NULL
print("\nKiểm tra các giá trị NULL trong bảng Students:")
print(students.isnull().sum())
print("\nKiểm tra các giá trị NULL trong bảng Majors:")
print(majors.isnull().sum())

# Thay thế giá trị thiếu trong cột Mark bằng điểm trung bình của toàn bộ sinh viên.
mean_mark = students['Mark'].mean()
students['Mark'] = students['Mark'].fillna(mean_mark)
print("\nSau khi thay thế giá trị thiếu:")
print(students.isnull().sum())
# Lọc các sinh viên có điểm từ 8.0 trở lên.
high_mark_students = students[students['Mark'] >= 8.0]
print("\nDanh sách các sinh viên có điểm từ 8.0 trở lên:")
print(high_mark_students [['StudentID', 'Name', 'MajorID', 'Mark']])
# Loc cac sinh vien 22 tuoi va co diem .= 7.0
print("\nDanh sách các sinh viên 22 tuổi và có điểm từ 7.0 trở lên:")
result = students[(students["Age"] == 22) & (students["Mark"] >= 7.0)]
print(result)
# Lọc sinh viên theo thành phố
print("\nDanh sách các sinh viên theo thành phố:")
city_students = students[students["City"] == "Ha Noi"]
print(city_students)
city_students = students[students["City"] == "Da Nang"]
print(city_students)
city_students = students[students["City"] == "Hai Phong"]
print(city_students)
