# encoding:utf-8

"""
author:Crazyfang
data:2017-5-23
function:将文件夹下的文件按照顺序命名
"""

# TODO 改进命名规则，支持命名重复文件的替换。
# TODO 增加多种顺序命名规则
# TODO 界面美化

from Tkinter import *
import tkFileDialog
import tkMessageBox
import os


class FileRenameSystem(object):
    """
    文件顺序命名类
    """

    def __init__(self):
        self.window = Tk()
        self.window.title('文件批量改名系统')

        self.frame = Frame(self.window)
        self.frame.pack()

        self.label_filepath = Label(self.frame, text='选择文件夹路径')
        self.file_path = StringVar()
        self.entry_file_path = Entry(self.frame, textvariable=self.file_path)
        self.button_file_path = Button(self.frame, text='浏览...', command=self.open_file_path)

        self.label_filepath.grid(row=1, column=1)
        self.entry_file_path.grid(row=1, column=2)
        self.button_file_path.grid(row=1, column=3)

        self.label_variable_begin = Label(self.frame, text='设定命名开始值')
        self.variable_begin = StringVar()
        self.entry_variable_begin = Entry(self.frame, textvariable=self.variable_begin)

        self.label_variable_begin.grid(row=2, column=1)
        self.entry_variable_begin.grid(row=2, column=2)

        self.label_variable_end = Label(self.frame, text='设定命名结束值')
        self.variable_end = StringVar()
        self.entry_variable_end = Entry(self.frame, textvariable=self.variable_end)

        self.label_variable_end.grid(row=3, column=1)
        self.entry_variable_end.grid(row=3, column=2)

        self.deal_button = Button(self.frame, text='开始处理', command=self.process)
        self.deal_button.grid(row=4, column=2)

        self.window.mainloop()

    def open_file_path(self):
        self.file_path.set(tkFileDialog.askdirectory())

    def process(self):
        if not self.variable_begin.get() and not self.variable_end.get() and not self.file_path.get():
            tkMessageBox.showinfo('提示', '当前信息未填写完全，请重新填写确认！！！')
        else:
            if os.path.isdir(self.file_path.get()):
                file_list = os.listdir(self.file_path.get())
                for subscript, files in enumerate(file_list):
                    old_file_name = self.file_path.get() + '/{}'.format(files)
                    extension = os.path.splitext(files)[1]
                    new_file_name = self.file_path.get() + '/{}{}'.format(subscript + int(self.variable_begin.get()),
                                                                          extension)

                    os.rename(old_file_name, new_file_name)
                tkMessageBox.showinfo('成功', '转换完成！！！')
            else:
                tkMessageBox.showinfo('错误', '当前路径错误，请重新选取！！！')

if __name__ == '__main__':
    FileRenameSystem()
