class Employee:
    def __init__(self,ID, name, position,salary):
        self.ID = ID
        self.name = name
        self.position = position
        self.salary = float(salary)
    def get_bonus(self):
        return 0.0
    def display_info(self):
        print(f"ID: {self.ID}, Name: {self.name}, Position: {self.position}, Salary: {self.salary:.2f}")

class Director(Employee):
    def __init__(self, ID, name, salary, bonus_rate=5):
        super().__init__(ID, name, "Director", salary)
        self.bonus_rate = bonus_rate
    def get_bonus(self):
        return self.salary * self.bonus_rate

class Manager(Employee):
    def __init__(self, ID, name, salary, bonus_rate=3):
        super().__init__(ID, name, "Manager", salary)
        self.bonus_rate = bonus_rate
    def get_bonus(self):
        return self.salary * self.bonus_rate    

class Staff(Employee):
    def __init__(self, ID, name, salary, bonus_rate=2):
        super().__init__(ID, name, "Staff", salary)
        self.bonus_rate = bonus_rate
    def get_bonus(self):
        return self.salary * self.bonus_rate
employer = {}
while True:
    print("\n1. Tạo Director")
    print("2. Tạo Manager")
    print("3. Tạo Staff")
    print("4. Tìm nhân viên theo ID")
    print("5. Tìm nhân viên có lương cao nhất")
    print("6. Cập nhật thông tin Director, Manager, Staff")
    print("7. Tính tổng thưởng cuối năm, mỗi 1 loại nhân viên có cách tính thưởng khác nhau")
    print("8. Lưu dictionary xuống file")
    print("9. Đọc dữ liệu từ file và lưu vào dictionary")
    print("10. Thoát")
    choice = input("Nhập lựa chọn của bạn: ").strip()

    if choice == "1":
            ID = input("Nhập ID Director: ").strip()
            if ID in employer:
                print("ID đã tồn tại. Vui lòng nhập ID khác.")
            else:
                name = input("Nhập tên Director: ").strip()
                try:
                    salary = float(input("Nhập lương Director: ").strip())
                    director = Director(ID, name, salary)
                    employer[ID] = director
                    print("Đã tạo Director thành công.")
                except ValueError:
                    print("Lỗi: Lương phải là một số hợp lệ.")
    elif choice == "2":
            ID = input("Nhập ID Manager: ").strip()
            if ID in employer:
                print("ID đã tồn tại. Vui lòng nhập ID khác.")
            else:
                name = input("Nhập tên Manager: ").strip()
                try:
                    salary = float(input("Nhập lương Manager: ").strip())
                    manager = Manager(ID, name, salary)
                    employer[ID] = manager
                    print("Đã tạo Manager thành công.")
                except ValueError:
                    print("Lỗi: Lương phải là một số hợp lệ.")
    elif choice == "3":
            ID = input("Nhập ID Staff: ").strip()
            if ID in employer:
                print("ID đã tồn tại. Vui lòng nhập ID khác.")
            else:
                name = input("Nhập tên Staff: ").strip()
                try:
                    salary = float(input("Nhập lương Staff: ").strip())
                    staff = Staff(ID, name, salary)
                    employer[ID] = staff
                    print("Đã tạo Staff thành công.")
                except ValueError:
                    print("Lỗi: Lương phải là một số hợp lệ.")
    elif choice == "4":
            ID = input("Nhập ID nhân viên cần tìm: ").strip()
            if ID in employer:
                employer[ID].display_info()
            else:
                print("Không tìm thấy nhân viên với ID này.")
    elif choice == "5":
            if employer:
                highest_salary_employee = max(employer.values(), key=lambda emp: emp.salary)
                print("Nhân viên có lương cao nhất:")
                highest_salary_employee.display_info()
            else:
                print("Chưa có nhân viên nào trong hệ thống.")
    elif choice == "6":
            ID = input("Nhập ID nhân viên cần cập nhật: ").strip()
            if ID in employer:
                name = input("Nhập tên mới (để trống nếu không muốn thay đổi): ").strip()
                salary_input = input("Nhập lương mới (để trống nếu không muốn thay đổi): ").strip()
                if name:
                    employer[ID].name = name
                if salary_input:
                    try:
                        salary = float(salary_input)
                        employer[ID].salary = salary
                    except ValueError:
                        print("Lỗi: Lương phải là một số hợp lệ.")
                print("Cập nhật thông tin thành công.")
            else:
                print("Không tìm thấy nhân viên với ID này.")
    elif choice == "7":
            if not employer:
                print("Chưa có nhân viên nào trong hệ thống.")
            else:
                bonus_by_position = {Director: 0.0, Manager: 0.0, Staff: 0.0}
                count_by_position = {Director: 0.0, Manager: 0.0, Staff: 0.0}
                for emp in employer.values():
                    bonus_by_position[type(emp)] += emp.get_bonus()
                    count_by_position[type(emp)] += 1
                print("Tổng thưởng cuối năm theo vị trí:")
                for pos in [Director, Manager, Staff]:
                        pos_name = pos.__name__
                        total_bonus = bonus_by_position[pos]
                        count = count_by_position[pos]
                        print(f"{pos_name}: Tổng thưởng = {total_bonus:.2f}, Số lượng = {int(count)}")
    elif choice == "8":
            import pickle
            with open("employer_data_2.txt", "wb") as f:
                pickle.dump(employer, f)
            print("Đã lưu dữ liệu xuống file employer_data_2.txt.")
    elif choice == "9":
            import pickle
            try:
                with open("employer_data_2.txt", "rb") as f:
                    employer = pickle.load(f)
                print("Đã đọc dữ liệu từ file employer_data_2.txt.")
            except FileNotFoundError:
                print("Không tìm thấy file employer_data_2.txt.")
    elif choice == "10":
            print("Thoát chương trình.")
            break
    else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
        