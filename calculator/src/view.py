import tkinter as tk
import tkinter.font as font


class View:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('计算器')
        # 大小 840x540，窗口移动到 距屏幕左侧350，上侧150 的位置
        self.window.geometry('599x295+350+150')
        # 按钮宽度，统一设置，便于修改
        self.btn_width = 10
        # 按钮字体大小
        self.btn_font = font.Font(size=20)
        # frame 便于布局
        self.frame = tk.Frame(self.window)
        self.display = tk.Frame(self.frame)
        self.buttons = tk.Frame(self.frame)
        # 显示区域
        self.show = tk.Label(self.display, font=self.btn_font,
                             background='#FCFCFC', width=42, height=2)
        # 按钮 0-9
        self.btn_zero = tk.Button(self.buttons, text='0',
                                  font=self.btn_font, width=self.btn_width)
        self.btn_one = tk.Button(self.buttons, text='1',
                                 font=self.btn_font, width=self.btn_width)
        self.btn_two = tk.Button(self.buttons, text='2',
                                 font=self.btn_font, width=self.btn_width)
        self.btn_three = tk.Button(self.buttons, text='3',
                                   font=self.btn_font, width=self.btn_width)
        self.btn_four = tk.Button(self.buttons, text='4',
                                  font=self.btn_font, width=self.btn_width)
        self.btn_five = tk.Button(self.buttons, text='5',
                                  font=self.btn_font, width=self.btn_width)
        self.btn_six = tk.Button(self.buttons, text='6',
                                 font=self.btn_font, width=self.btn_width)
        self.btn_seven = tk.Button(self.buttons, text='7',
                                   font=self.btn_font, width=self.btn_width)
        self.btn_eight = tk.Button(self.buttons, text='8',
                                   font=self.btn_font, width=self.btn_width)
        self.btn_nine = tk.Button(self.buttons, text='9',
                                  font=self.btn_font, width=self.btn_width)
        # 按钮 运算符号
        self.btn_dot = tk.Button(self.buttons, text='.',
                                 font=self.btn_font, width=self.btn_width)
        self.btn_add = tk.Button(self.buttons, text='+',
                                 font=self.btn_font, width=self.btn_width)
        self.btn_subtract = tk.Button(self.buttons, text='-',
                                      font=self.btn_font, width=self.btn_width)
        self.btn_multiply = tk.Button(self.buttons, text='*',
                                      font=self.btn_font, width=self.btn_width)
        self.btn_divide = tk.Button(self.buttons, text='/',
                                    font=self.btn_font, width=self.btn_width)
        self.btn_equal = tk.Button(self.buttons, text='=',
                                   font=self.btn_font, width=self.btn_width)
        self.btn_negate = tk.Button(self.buttons, text='+/-',
                                    font=self.btn_font, width=self.btn_width)
        self.btn_left = tk.Button(self.buttons, text='(',
                                  font=self.btn_font, width=self.btn_width)
        self.btn_right = tk.Button(self.buttons, text=')',
                                   font=self.btn_font, width=self.btn_width)
        self.btn_clear = tk.Button(self.buttons, text='C',
                                   font=self.btn_font, width=self.btn_width)

    def set_ui(self):
        # 放置 frame
        self.frame.grid(row=0, column=0)
        self.display.grid(row=0, column=0)
        self.buttons.grid(row=1, column=0)
        # 放置显示区域
        self.show.grid(row=0, column=0)
        # 放置 C、（、）、/
        self.btn_clear.grid(row=0, column=0)
        self.btn_left.grid(row=0, column=1)
        self.btn_right.grid(row=0, column=2)
        self.btn_divide.grid(row=0, column=3)
        # 放置 7、8、9、*
        self.btn_seven.grid(row=1, column=0)
        self.btn_eight.grid(row=1, column=1)
        self.btn_nine.grid(row=1, column=2)
        self.btn_multiply.grid(row=1, column=3)
        # 放置 4、5、6、-
        self.btn_four.grid(row=2, column=0)
        self.btn_five.grid(row=2, column=1)
        self.btn_six.grid(row=2, column=2)
        self.btn_subtract.grid(row=2, column=3)
        # 放置 1、2、3、+
        self.btn_one.grid(row=3, column=0)
        self.btn_two.grid(row=3, column=1)
        self.btn_three.grid(row=3, column=2)
        self.btn_add.grid(row=3, column=3)
        # 放置 +/- 、0、. 、=
        self.btn_negate.grid(row=4, column=0)
        self.btn_zero.grid(row=4, column=1)
        self.btn_dot.grid(row=4, column=2)
        self.btn_equal.grid(row=4, column=3)


if __name__ == '__main__':
    # 测试
    view = View()
    view.set_ui()
    view.window.mainloop()
