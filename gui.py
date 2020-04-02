import tkinter as tk
import tkinter.messagebox
import _thread
from view import View
from database import DB


class GUI:
    """
    用户接口类，将视图与逻辑对接
    @author weingxing
    @since 2020/04/02
    """

    def __init__(self):
        self.db = DB()
        self.view = View()
        self.view.set_ui()

        self.sno = tk.StringVar()
        self.name = tk.StringVar()
        self.sex = tk.StringVar()
        self.college = tk.StringVar()
        self.clazz = tk.StringVar()

        self.connect()

    # 添加信息
    def add(self, event):
        sno = self.view._entry_sno.get()
        name = self.view._entry_name.get()
        sex = self.view._entry_sex.get()
        college = self.view._entry_college.get()
        clazz = self.view._entry_clazz.get()
        # 判断是否输入数据
        if sno != '' and name != '' and sex != '' and college != '' and clazz != '':
            if self.db.insert(sno=sno, name=name, sex=sex, college=college, clazz=clazz):
                values = (sno, name, sex, college, clazz)
                self.view.data_list.insert('', 'end', values=values)
                # 新建线程进行弹窗，否则按钮按点击后无法弹起来
                _thread.start_new_thread(lambda: tk.messagebox.showinfo(message='添加成功'), ())
            else:
                _thread.start_new_thread(lambda: tk.messagebox.showinfo(message='添加失败'), ())
            # 清空输入框
            self.view._entry_sno.delete(0, len(sno))
            self.view._entry_name.delete(0, len(name))
            self.view._entry_sex.delete(0, len(sex))
            self.view._entry_college.delete(0, len(college))
            self.view._entry_clazz.delete(0, len(clazz))
        else:
            _thread.start_new_thread(lambda: tk.messagebox.showinfo(message='请输入信息'), ())

    def update(self, event):
        sno = self.view.entry_sno.get()
        name = self.view.entry_name.get()
        sex = self.view.entry_sex.get()
        college = self.view.entry_college.get()
        clazz = self.view.entry_clazz.get()
        if sno != '' and name != '' and sex != '' and college != '' and clazz != '':
            if self.db.update(sno=sno, name=name, sex=sex, college=college, clazz=clazz):
                # 从数据库成功更新后更新界面，要传入event，这里使用 '' 代替
                self.refresh('')
                _thread.start_new_thread(lambda: tk.messagebox.showinfo(message='更新成功'), ())
            else:
                _thread.start_new_thread(lambda: tk.messagebox.showinfo(message='更新失败'), ())
        else:
            _thread.start_new_thread(lambda: tk.messagebox.showinfo(message='请补全信息'), ())

    def delete(self, event):
        sno = self.view.entry_sno.get()
        if sno != '':
            if self.db.delete(sno):
                # 从数据库成功删除后更新界面
                self.refresh('')
                # 清空信息
                self.sno.set('')
                self.view.entry_sno.configure(textvariable=self.sno)
                self.view.entry_name.delete(0, len(self.name.get()))
                self.view.entry_sex.delete(0, len(self.sex.get()))
                self.view.entry_college.delete(0, len(self.college.get()))
                self.view.entry_clazz.delete(0, len(self.clazz.get()))
                _thread.start_new_thread(lambda: tk.messagebox.showinfo(message='删除成功'), ())
            else:
                _thread.start_new_thread(lambda: tk.messagebox.showinfo(message='删除失败'), ())
        else:
            _thread.start_new_thread(lambda: tk.messagebox.showinfo(message='未选中数据'), ())

    def search(self, event):
        key = self.view.entry_search.get()
        try:
            assert not key == ''
            # 清空现有数据
            x = self.view.data_list.get_children()
            for item in x:
                self.view.data_list.delete(item)

            result = self.db.search(key)
            assert not result is None
            i = 0
            for d in result:
                self.view.data_list.insert('', i, value=d)
                i += 1
        except AssertionError:
            _thread.start_new_thread(lambda: tk.messagebox.showinfo(message='搜索失败'), ())

    def refresh(self, event):
        try:
            # 清空现有数据
            x = self.view.data_list.get_children()
            for item in x:
                self.view.data_list.delete(item)

            result = self.db.select()
            assert not result is None
            i = 0
            for d in result:
                self.view.data_list.insert('', i, value=d)
                i += 1
        except AssertionError:
            _thread.start_new_thread(lambda: tk.messagebox.showinfo(message='刷新失败'), ())

    def detail(self, event):
        if len(self.view.data_list.selection()) != 0:
            item = self.view.data_list.selection()[0]
            values = self.view.data_list.item(item, "values")
            self.sno.set(values[0])
            self.name.set(values[1])
            self.sex.set(values[2])
            self.college.set(values[3])
            self.clazz.set(values[4])

            self.view.entry_sno.configure(textvariable=self.sno)
            self.view.entry_name.configure(textvariable=self.name)
            self.view.entry_sex.configure(textvariable=self.sex)
            self.view.entry_college.configure(textvariable=self.college)
            self.view.entry_clazz.configure(textvariable=self.clazz)

    def connect(self):
        self.view.btn_add.bind('<Button-1>', self.add)
        self.view.btn_update.bind('<Button-1>', self.update)
        self.view.btn_delete.bind('<Button-1>', self.delete)
        self.view.btn_search.bind('<Button-1>', self.search)
        self.view.btn_refresh.bind('<Button-1>', self.refresh)
        self.view.data_list.bind('<ButtonRelease-1>', self.detail)

    def start(self):
        data = self.db.select()
        i = 0
        for d in data:
            self.view.data_list.insert('', i, value=d)
            i += 1
        self.view.window.mainloop()


if __name__ == '__main__':
    gui = GUI()
    gui.start()
