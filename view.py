import tkinter as tk
from tkinter import ttk


class View:
    """
    视图类，定义软件界面布局
    @author weingxing
    @since 2020/04/02
    """

    def __init__(self):
        self.window = tk.Tk()
        self.window.title('学生管理系统')
        # 大小 840x540，窗口移动到 距屏幕左侧350，上侧100 的位置
        self.window.geometry('880x600+350+100')
        # 定义 frame，便于布局
        self.frame = tk.Frame(self.window)

        self.frame_left = tk.Frame(self.frame)
        self.frame_right = tk.Frame(self.frame)
        self.frame_add = tk.Frame(self.frame)

        self.frame_search = tk.Frame(self.frame_left)
        self.frame_list = tk.Frame(self.frame_left)
        self.frame_detail = tk.Frame(self.frame_right)

        # 定义控件
        # 搜索按钮和输入框
        self.btn_search = tk.Button(self.frame_search, text='搜 索',
                                    width=10, height=1, relief=tk.GROOVE)
        self.entry_search = tk.Entry(self.frame_search, width=25)
        self.btn_refresh = tk.Button(self.frame_search, text='刷 新',
                                     width=10, height=1, relief=tk.GROOVE)
        # 信息列表显示控件
        self.lab_title = tk.Label(self.frame_list, text='学生信息')
        columns = ('sno', 'name', 'sex', 'college', 'clazz')
        self.data_list = ttk.Treeview(self.frame_list, height=18, show='headings', columns=columns)
        # 滚动条
        self.VScroll1 = tk.Scrollbar(self.frame_left, orient='vertical', command=self.data_list.yview)
        self.VScroll1.place(relx=0.964, rely=0.190, relwidth=0.034, relheight=0.766)
        # 给treeview添加配置
        self.data_list.configure(yscrollcommand=self.VScroll1.set)

        # 信息更改显示控件
        self.lab_sno = tk.Label(self.frame_detail, text='学号')
        self.entry_sno = tk.Entry(self.frame_detail, state=tk.DISABLED)
        self.lab_name = tk.Label(self.frame_detail, text='姓名')
        self.entry_name = tk.Entry(self.frame_detail)
        self.lab_sex = tk.Label(self.frame_detail, text='性别')
        self.entry_sex = tk.Entry(self.frame_detail)
        self.lab_college = tk.Label(self.frame_detail, text='学院')
        self.entry_college = tk.Entry(self.frame_detail)
        self.lab_clazz = tk.Label(self.frame_detail, text='班级')
        self.entry_clazz = tk.Entry(self.frame_detail)
        self.btn_update = tk.Button(self.frame_detail, text='更 新', relief=tk.GROOVE)
        self.btn_delete = tk.Button(self.frame_detail, text='删 除', relief=tk.GROOVE)
        # 添加信息控件
        self._lab_sno = tk.Label(self.frame_add, text='学号')
        self._entry_sno = tk.Entry(self.frame_add)
        self._lab_name = tk.Label(self.frame_add, text='姓名')
        self._entry_name = tk.Entry(self.frame_add)
        self._lab_sex = tk.Label(self.frame_add, text='性别')
        self._entry_sex = tk.Entry(self.frame_add)
        self._lab_college = tk.Label(self.frame_add, text='学院')
        self._entry_college = tk.Entry(self.frame_add)
        self._lab_clazz = tk.Label(self.frame_add, text='班级')
        self._entry_clazz = tk.Entry(self.frame_add)
        self.btn_add = tk.Button(self.frame_add, text='添 加', relief=tk.GROOVE)

    def set_ui(self):
        # 表示列, 不显示
        self.data_list.column('sno', width=100, anchor='center')
        self.data_list.column('name', width=100, anchor='center')
        self.data_list.column('sex', width=100, anchor='center')
        self.data_list.column('college', width=150, anchor='center')
        self.data_list.column('clazz', width=100, anchor='center')
        # 显示表头
        self.data_list.heading('sno', text='学号')
        self.data_list.heading('name', text='姓名')
        self.data_list.heading('sex', text='性别')
        self.data_list.heading('college', text='学院')
        self.data_list.heading('clazz', text='班级')
        # 放置 frame
        self.frame.grid(row=0, column=0)
        self.frame_left.grid(row=0, column=0, padx=20)
        self.frame_right.grid(row=0, column=1)
        self.frame_add.grid(row=1, column=0)
        self.frame_search.grid(row=0, column=0, pady=10)
        self.frame_list.grid(row=1, column=0, pady=20)
        self.frame_detail.grid(row=0, column=0)

        # 放置搜索、刷新
        self.entry_search.grid(row=0, column=0, padx=5)
        self.btn_search.grid(row=0, column=1, padx=5)
        self.btn_refresh.grid(row=0, column=2, padx=5)

        # 放置数据表格
        self.lab_title.grid(row=1, column=0)
        self.data_list.grid(row=2, column=0)

        # 放置详细内容控件
        self.lab_sno.grid(row=0, column=2, pady=5)
        self.entry_sno.grid(row=0, column=3, pady=5)
        self.lab_name.grid(row=1, column=2, pady=5)
        self.entry_name.grid(row=1, column=3, pady=5)
        self.lab_sex.grid(row=2, column=2, pady=5)
        self.entry_sex.grid(row=2, column=3, pady=5)
        self.lab_college.grid(row=3, column=2, pady=5)
        self.entry_college.grid(row=3, column=3, pady=5)
        self.lab_clazz.grid(row=4, column=2, pady=5)
        self.entry_clazz.grid(row=4, column=3, pady=5)
        self.btn_delete.grid(row=5, column=2, pady=15, ipadx=15)
        self.btn_update.grid(row=5, column=3, pady=15, ipadx=15)

        # 放置添加内容控件
        self._lab_sno.grid(row=0, column=0, padx=15)
        self._entry_sno.grid(row=0, column=1)
        self._lab_name.grid(row=0, column=2, padx=15)
        self._entry_name.grid(row=0, column=3)
        self._lab_sex.grid(row=0, column=4, padx=15)
        self._entry_sex.grid(row=0, column=5)
        self._lab_college.grid(row=1, column=0, pady=10)
        self._entry_college.grid(row=1, column=1)
        self._lab_clazz.grid(row=1, column=2)
        self._entry_clazz.grid(row=1, column=3)
        self.btn_add.grid(row=1, column=4, ipadx=20, columnspan=2)


if __name__ == '__main__':
    # 测试
    view = View()
    view.set_ui()
    view.window.mainloop()
