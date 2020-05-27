from view import MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from PyQt5.QtCore import QDir
import core
from core import error_log
import time


class Main(QWidget, MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.slot_init()

    # 连接槽函数
    def slot_init(self):
        self.combo_model.currentTextChanged.connect(self.change_state)
        self.btn_src.clicked.connect(lambda: self.chose_file(flag='src'))
        self.btn_dist.clicked.connect(lambda: self.chose_file(flag='dist'))
        self.btn_encrypt.clicked.connect(self.do_encrypt)
        self.btn_decrypt.clicked.connect(self.do_decrypt)
        self.btn_close.clicked.connect(self.close)

    # 读取数据
    def read_data(self, file):
        try:
            with open(file, 'rb') as f:
                return f.read()
        except Exception as e:
            error_log(e)
            QMessageBox.critical(self, '错误', '读取文件时出错')

    # 写入数据
    def write_data(self, file, data):
        try:
            with open(file, 'wb') as f:
                f.write(data)
            return True
        except Exception as e:
            error_log(e)
            QMessageBox.critical(self, '错误', '写入文件时出错')

    # 更改 偏移量编辑框 的可用状态
    def change_state(self):
        model = self.combo_model.currentText()
        if model == 'ECB':
            self.edit_vi.setEnabled(False)
            self.edit_vi.setText('ECB模式无需偏移量')
        else:
            self.edit_vi.setEnabled(True)
            self.edit_vi.clear()

    # 进行加密
    def do_encrypt(self):
        method = self.combo_method.currentText()
        model = self.combo_model.currentText()
        key = self.edit_key.text()
        vi = self.edit_vi.text()
        src = self.edit_src.text()
        dist = self.edit_dist.text()
        result = self.encrypt(src, dist, method, model, key, vi)
        if not result:
            QMessageBox.information(self, '提示', '加密失败')
            return
        file = dist + '/' + src.split('/')[-1] + '.data'
        if self.write_data(file, result):
            QMessageBox.information(self, '提示', f'加密成功，文件路径：\n {file}')

    # 进行解密
    def do_decrypt(self):
        method = self.combo_method.currentText()
        model = self.combo_model.currentText()
        key = self.edit_key.text()
        vi = self.edit_vi.text()
        src = self.edit_src.text()
        dist = self.edit_dist.text()
        result = self.decrypt(src, dist, method, model, key, vi)
        if not result:
            QMessageBox.information(self, '提示', '解密失败')
            return
        try:
            # 文件后缀
            ext = src.split('/')[-1].split('.')[-2]
            file = dist + '/' + src.split('/')[-1] + '.' + ext
            if self.write_data(file, result):
                QMessageBox.information(self, '提示', f'解密成功，文件路径：\n {file}')
        except:
            file = dist + '/decrypt' + src.split('/')[-1]
            if self.write_data(file, result):
                QMessageBox.information(self, '提示', f'解密成功，文件路径：\n {file}\n'
                                                    f'请自行修改文件后缀')

    # 浏览选择文件/文件夹，flag用于判断是选择文件，还是选择文件夹
    def chose_file(self, flag='src'):
        dig = QFileDialog()
        path = None
        if flag == 'src':
            # 设置可以打开任何文件
            dig.setFileMode(QFileDialog.AnyFile)
            # 文件过滤
            dig.setFilter(QDir.Files)
            if dig.exec_():
                path = dig.selectedFiles()[0]
            self.edit_src.setText(path)
        else:
            path = dig.getExistingDirectory(self)
            self.edit_dist.setText(path)

    # 对选择的算法等进行校验，不通过则弹窗提示
    def check(self, src, dist, method, model, key, vi):
        if src == '':
            QMessageBox.information(self, '提示', '请输入输入路径')
            return False
        if dist == '':
            QMessageBox.information(self, '提示', '请输入输出路径')
            return False
        # 校验加密算法的选择
        if method == '请选择':
            QMessageBox.information(self, '提示', '请选择加密算法')
            return False
        # 校验加密模式的选择
        if model == '请选择':
            QMessageBox.information(self, '提示', '请选择加密模式')
            return False
        # 校验密钥
        if key == '':
            QMessageBox.information(self, '提示', '请输入加密密钥')
            return False
        elif method == 'DES' and len(key) != 8:
            QMessageBox.information(self, '提示', 'DES算法密钥长度位8位')
            return False
        elif method == 'AES' and len(key) not in [16, 24, 32]:
            QMessageBox.information(self, '提示', 'AES算法密钥长度位16/24/32位')
            return False
        # 校验偏移量
        if model == 'CBC':
            if vi == '':
                QMessageBox.information(self, '提示', '请输入偏移量')
                return False
            elif method == 'DES' and len(vi) != 8:
                QMessageBox.information(self, '提示', 'DES算法偏移量长度位8位')
                return False
            elif method == 'AES' and len(vi) != 16:
                QMessageBox.information(self, '提示', 'AES算法偏移量长度位16位')
                return False
        return True

    # 加密
    def encrypt(self, src, dist, method, model, key, vi):
        if not self.check(src, dist, method, model, key, vi):
            return
        data = self.read_data(src)
        if method == 'AES':
            if model == 'CBC':
                result = core.aes_encrypt_cbc(data, key, vi)
            else:
                result = core.aes_encrypt_ecb(data, key)
        else:
            if model == 'CBC':
                result = core.des_encrypt_cbc(data, key, vi)
            else:
                result = core.des_encrypt_ecb(data, key)
        return result

    # 解密
    def decrypt(self, src, dist, method, model, key, vi):
        if not self.check(src, dist, method, model, key, vi):
            return
        data = self.read_data(src)
        if method == 'AES':
            if model == 'CBC':
                result = core.aes_decrypt_cbc(data, key, vi)
            else:
                result = core.aes_decrypt_ecb(data, key)
        else:
            if model == 'CBC':
                result = core.des_decrypt_cbc(data, key, vi)
            else:
                result = core.des_decrypt_ecb(data, key)
        return result


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
