import tkinter as tk
from tkinter import Label, Entry, Button
from datetime import datetime
# Tạo cửa sổ chính
root = tk.Tk()
root.title("Thông tin nhân viên")
root.geometry("685x350")

# Tiêu đề
o1 = tk.Label(root, text="Thông tin nhân viên", font=("Arial", 14), anchor="center")
o1.place(x=-160, y=5, width=500, height=30)

# Biến để lưu trạng thái của checkbox
checkbox_var = tk.BooleanVar()

# Tạo ô đánh dấu tích
checkbox1 = tk.Checkbutton(root, text="Là khách hàng", variable=checkbox_var, onvalue=1, offvalue=0)
checkbox1.place(x=180, y=10)
checkbox2 = tk.Checkbutton(root, text="Là nhà cung cấp", variable=checkbox_var, onvalue=2, offvalue=0)
checkbox2.place(x=300, y=10)
def show():
    if checkbox_var.get() ==1:
        print()
    elif checkbox_var.get() ==2:
        print()
    else:
        print()
tapT1=tk.Label(root, text="Mã*", width=60)
tapT1.place(x=-20, y=35, width=80, height=60)
txtT1=tk.Entry()
txtT1.place(x=10, y=75)
tapT2=tk.Label(root, text="Tên*", width=60)
tapT2.place(x=130, y=35, width=80, height=60)
txtT2=tk.Entry()
txtT2.place(x=160, y=75)
tapT3=tk.Label(root, text="Ngày sinh", width=60)
tapT3.place(x=300, y=35, width=80, height=60)
txtT3=Entry()
txtT3.place(x=315, y=75)
tapT4=tk.Label(root, text="Giới tính", width=60)
tapT4.place(x=450, y=35, width=80, height=60)
gioitinh=tk.StringVar(value="")
nam=tk.Radiobutton(root, text="Nam", variable=gioitinh, value="Nam")
nam.place(x=470, y=73)
nu=tk.Radiobutton(root, text="Nữ", variable=gioitinh, value="Nữ")
nu.place(x=530, y=73)
tapT5=tk.Label(root, text="Đơn vị*", width=60)
tapT5.place(x=-20, y=100, width=90, height=60)
txtT5=tk.Entry(width=45)
txtT5.place(x=10, y=138)
tapT6=tk.Label(root, text="Số CMND", width=70)
tapT6.place(x=300, y=100, width=90, height=60)
txtT6=tk.Entry(width=35)
txtT6.place(x=315, y=138)
tapT7=tk.Label(root, text="Ngày cấp", width=60)
tapT7.place(x=530, y=100, width=80, height=60)
txtT7=tk.Entry()
txtT7.place(x=545, y=138)
tapT8=tk.Label(root, text="Chức danh", width=60)
tapT8.place(x=-10, y=160, width=90, height=60)
txtT8=tk.Entry(width=45)
txtT8.place(x=10, y=200)
tapT9=tk.Label(root, text="Nơi cấp", width=60)
tapT9.place(x=300, y=160, width=90, height=60)
txtT9=tk.Entry(width=58)
txtT9.place(x=315, y=200)
nhanvien = [
    {"name": "Nguyễn Văn A", "dob": "11/04"},
    {"name": "Trần Thị B", "dob": "28/06"},

]



def check_birthday():
    today = datetime.now().strftime("%d/%m")
    birthday_employees = [emp["name"] for emp in nhanvien if emp["dob"] == today]

    if birthday_employees:
        result_text = "Sinh nhật hôm nay:\n" + "\n".join(birthday_employees)
    else:
        result_text = "Không có nhân viên nào sinh nhật hôm nay."

    # Hiển thị kết quả trong cửa sổ
    tapT10.config(text=result_text)



sinhnhat = Button(root, text="Sinh nhật hôm nay", command=check_birthday)
sinhnhat.place(x=10, y=240)
tapT10 = Label(root, text="", font=("Arial", 10), anchor="w")
tapT10.place(x=130, y=240, width=500, height=40)
danhsach=Button(root, text="danh sách nhân viên", )
danhsach.place(x=300, y=300)
# Chạy vòng lặp chính
root.mainloop()
