import tkinter as tk
import _tkinter
from tkinter import messagebox
from database import DB
from gui import GUI


class Login:
    """
    登录界面及逻辑，程序以此文件为入口
    @author weingxing
    @since 2020/04/02
    """

    def __init__(self):
        self.db = DB()

        self.window = tk.Tk()
        self.window.title('学生管理系统')
        self.window.geometry('450x300+500+200')

        # 加载图片
        try:
            self.canvas = tk.Canvas(self.window, height=200, width=500)
            self.image_file = tk.PhotoImage(file='welcome.gif')
            self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.image_file)
            self.canvas.pack(side='top')
        except _tkinter.TclError:
            tk.messagebox.showinfo(message='图片丢失')

        # 以下定义登录控件
        # 定义用户名和密码标签，并直接布局到界面
        tk.Label(self.window, text='用户名:').place(x=100, y=150)
        tk.Label(self.window, text='密   码:').place(x=100, y=190)
        # 定义用户名和密码输入框并布局到界面
        self.entry_user = tk.Entry(self.window)
        self.entry_user.place(x=160, y=150)
        self.entry_pwd = tk.Entry(self.window, show='*')
        self.entry_pwd.place(x=160, y=190)
        # 定义登录和注册按钮并布局到界面
        tk.Button(self.window, text='登 录', width=5,
                  command=self.login, relief=tk.GROOVE).place(x=170, y=230)
        tk.Button(self.window, text='注 册', width=5,
                  command=self.register, relief=tk.GROOVE).place(x=270, y=230)

        self.flag = False

    def login(self):
        _user = self.entry_user.get()
        _pwd = self.entry_pwd.get()
        users = self.db.login()
        # 校验用户名和密码
        if len(users) > 0:
            for user in users:
                if _user == user[1] and _pwd == user[2]:
                    # 销毁登录界面
                    self.window.destroy()
                    # 加载主界面
                    GUI().start()
                    self.flag = True
                    break

            if not self.flag:
                tk.messagebox.showinfo(message='用户名或密码错误')
        else:
            tk.messagebox.showinfo(message='无法登录')

    def register(self):
        # 向数据库添加用户
        def add_user():
            # 获取输入
            username = self._entry_username.get()
            password = self._entry_pwd.get()
            confirm_password = self._entry_pwd_confirm.get()
            # 判断输入
            if username != '' and password != '' and confirm_password != '':
                if password == confirm_password:
                    if self.db.register(username=username, password=password):
                        tk.messagebox.showinfo(message='注册成功')
                    else:
                        tk.messagebox.showinfo(message='注册失败')
                else:
                    tk.messagebox.showinfo(message='两次输入的密码不一致')
            else:
                tk.messagebox.showinfo(message='请补全信息')

        # 定义注册界面
        self.window_register = tk.Toplevel(self.window)
        self.window_register.geometry('350x200+560+260')
        self.window_register.title('账号注册')
        # 输入框定义
        self._entry_username = tk.Entry(self.window_register)
        self._entry_pwd = tk.Entry(self.window_register, show='*')
        self._entry_pwd_confirm = tk.Entry(self.window_register, show='*')
        # 布局
        tk.Label(self.window_register, text='用户名: ').place(x=80, y=10)
        self._entry_username.place(x=140, y=10)
        tk.Label(self.window_register, text='密 码: ').place(x=85, y=50)
        self._entry_pwd.place(x=140, y=50)
        tk.Label(self.window_register, text='确认密码: ').place(x=70, y=90)
        self._entry_pwd_confirm.place(x=140, y=90)
        # 按钮
        self.btn_register = tk.Button(self.window_register, text='注 册',
                                      width=15, command=add_user, relief=tk.GROOVE).place(x=140, y=130)

    def start(self):
        self.window.mainloop()


if __name__ == '__main__':
    login = Login()
    login.start()
