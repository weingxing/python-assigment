from view import View


# 是否点击 等于 按钮
flag = False


class Main:
    def __init__(self):
        self.view = View()
        self.view.set_ui()
        self.connect()

    # 绑定函数
    def connect(self):
        self.view.btn_zero.bind('<Button-1>', lambda e: self.input('0'))
        self.view.btn_one.bind('<Button-1>', lambda e: self.input('1'))
        self.view.btn_two.bind('<Button-1>', lambda e: self.input('2'))
        self.view.btn_three.bind('<Button-1>', lambda e: self.input('3'))
        self.view.btn_four.bind('<Button-1>', lambda e: self.input('4'))
        self.view.btn_five.bind('<Button-1>', lambda e: self.input('5'))
        self.view.btn_six.bind('<Button-1>', lambda e: self.input('6'))
        self.view.btn_seven.bind('<Button-1>', lambda e: self.input('7'))
        self.view.btn_eight.bind('<Button-1>', lambda e: self.input('8'))
        self.view.btn_nine.bind('<Button-1>', lambda e: self.input('9'))
        self.view.btn_add.bind('<Button-1>', lambda e: self.input('+'))
        self.view.btn_subtract.bind('<Button-1>', lambda e: self.input('-'))
        self.view.btn_multiply.bind('<Button-1>', lambda e: self.input('*'))
        self.view.btn_divide.bind('<Button-1>', lambda e: self.input('/'))
        self.view.btn_left.bind('<Button-1>', lambda e: self.input('('))
        self.view.btn_right.bind('<Button-1>', lambda e: self.input(')'))
        self.view.btn_dot.bind('<Button-1>', lambda e: self.input('.'))
        self.view.btn_negate.bind('<Button-1>', lambda e: self.input('--'))
        self.view.btn_clear.bind('<Button-1>', self.clear)
        self.view.btn_equal.bind('<Button-1>', lambda e: self.view.show.configure(
            text=self.calculate(self.view.show_exp.cget('text'))
        ))

    # 计算表达式
    def calculate(self, expression):
        self.view.show_exp.configure(text=expression+'=')
        try:
            result = eval(expression)
            global flag
            flag = True
            return str(result)
        except (SyntaxError, NameError):
            flag = True
            return '错误'

    # 显示、处理输入（按钮点击）
    def input(self, value):
        # 刚刚计算完，清空原有数据
        global flag
        if flag:
            self.clear('')
            flag = False

        operate = ['+', '-', '*', '/']
        text = self.view.show_exp.cget('text')
        # 正/负数转换
        if value == '--':
            value = ''
            # 反转原来的数据
            text = text[::-1]
            idx = []
            # 取得反转后的运算符索引
            for op in operate:
                i = text.find(op)
                if i != -1:
                    idx.append(i)
            # 取得最前面的运算符
            index = min(idx)

            if text[index] == '-' and text[index + 1] in operate:
                # 当前数是负数，变为正数，删除负号即可
                text = text[:index] + text[index + 1:]
            else:
                # 当前数不是负数，变为负数，插入负号即可
                text = text[:index] + '-' + text[index:]
            # 将数据恢复原来的顺序
            text = text[::-1]

        # 防止一个数输入多个小数点、运算符后跟小数点
        try:
            if value == '.':
                # 末尾已经是小数点
                if text[-1] == '.':
                    value = ''
                # 反转方便取得最后一个操作数
                text = text[::-1]
                idx = []
                # 取得反转后的运算符索引
                for op in operate:
                    i = text.find(op)
                    if i != -1:
                        idx.append(i)
                # 取得最前面的运算符
                try:
                    index = min(idx)
                except ValueError:
                    # 第一个操作数已经包含小数点
                    index = 0
                    if '.' in text:
                        value = ''
                # 最后输入的操作数已经包含小数点
                if '.' in text[:index]:
                    value = ''
                # 转回原顺序
                text = text[::-1]
        except IndexError:
            pass

        # 运算符更改  最后一个是运算符且输入的也是运算符，则更改运算符
        try:
            if text[-1] in operate and value in operate:
                text = text[:-1]
        except IndexError:
            pass

        # 更新数据显示
        val = text + value
        self.view.show_exp.configure(text=val)

    def clear(self, event):
        self.view.show_exp.configure(text='')
        self.view.show.configure(text='')

    def start(self):
        self.view.window.mainloop()


if __name__ == '__main__':
    main = Main()
    main.start()
