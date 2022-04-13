

from email import message
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import webbrowser as web
import sys
import pymysql
import qtawesome
import index
from actions.collection import Collection

class MainUi(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()
    self.init_ui()
  def init_ui(self):
      self.pagehome()
  def pagehome(self):

    self.setFixedSize(960,700)
    self.main_widget = QtWidgets.QWidget() # 创建窗口主部件
    self.main_layout = QtWidgets.QGridLayout() # 创建主部件的网格布局
    self.main_widget.setLayout(self.main_layout) # 设置窗口主部件布局为网格布局

    self.left_widget = QtWidgets.QWidget() # 创建左侧部件
    self.left_widget.setObjectName('left_widget')
    self.left_layout = QtWidgets.QGridLayout() # 创建左侧部件的网格布局层
    self.left_widget.setLayout(self.left_layout) # 设置左侧部件布局为网格

    self.right_widget = QtWidgets.QWidget() # 创建右侧部件
    self.right_widget.setObjectName('right_widget')
    self.right_layout = QtWidgets.QGridLayout()
    self.right_widget.setLayout(self.right_layout) # 设置右侧部件布局为网格

    self.main_layout.addWidget(self.left_widget,0,0,12,2) # 左侧部件在第0行第0列，占8行3列
    self.main_layout.addWidget(self.right_widget,0,2,12,10) # 右侧部件在第0行第3列，占8行9列
    self.setCentralWidget(self.main_widget) # 设置窗口主部件
    self.left_close = QtWidgets.QPushButton("X") # 关闭按钮
    self.left_close.clicked.connect(self.closeClick)
    self.left_visit = QtWidgets.QPushButton("") # 空白按钮
    self.left_mini = QtWidgets.QPushButton("-") # 最小化按钮
    self.left_mini.clicked.connect(self.hiddeClick)
    self.left_label_1 = QtWidgets.QPushButton("信息收集")
    self.left_label_1.setObjectName('left_label')
    self.left_label_1.clicked.connect(self.page1)
    self.left_label_2 = QtWidgets.QPushButton("查寝签到")
    self.left_label_2.clicked.connect(self.page2)
    self.left_label_2.setObjectName('left_label')
    self.left_label_3 = QtWidgets.QPushButton("首页👉")
    self.left_label_3.clicked.connect(self.backpagehome)
    self.left_label_3.setObjectName('left_label')
    self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.comment',color='white'),"联系作者")
    self.left_button_7.clicked.connect(self.skipurl)
    self.left_button_7.setObjectName('left_button')
    self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.star',color='white'),"检查版本")
    self.left_button_8.clicked.connect(self.checkVersion)

    self.left_button_8.setObjectName('left_button')
    self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa.question',color='white'),"遇到问题")
    self.left_button_9.clicked.connect(self.skipurl)
    self.left_button_9.setObjectName('left_button')
    self.left_xxx = QtWidgets.QPushButton("作者:小新")
    self.left_xxx.setObjectName('left_button')
    self.left_layout.addWidget(self.left_xxx, 13, 0, 1, 3)
    self.left_layout.addWidget(self.left_mini, 0, 0,1,1)
    self.left_layout.addWidget(self.left_close, 0, 2,1,1)
    self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
    self.left_layout.addWidget(self.left_label_1,1,0,1,3)
    self.left_layout.addWidget(self.left_label_2, 5, 0,1,3)
    self.left_layout.addWidget(self.left_label_3, 9, 0,1,3)
    self.left_layout.addWidget(self.left_button_7, 10, 0,1,3)
    self.left_layout.addWidget(self.left_button_8, 11, 0,1,3)
    self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)

    self.right_recommend_label = QtWidgets.QLabel("欢迎使用今日校园信息收集和查寝签到软件（南京晓庄学院版），"+
                                                   "请仔细阅读用前须知：\n\t1.信息收集:选择你所在的校区后，"+
                                                   "填写用于登录信息门户的学号和\n\b\b\b\b密码，填写接收信息的邮箱，"+"点击start按钮等待约7秒，出现结果提示。"+"\n\t2.查寝签到:"+
                                                   "选择你所在校区后，填写用于登录信息门户的学号和密\n\b\b\b\b码，填写接收信息的邮箱，上传签到照片，"+
                                                   "点击start按钮等待约7s，出\n\b\b\b\b现结果提示。"+"\n\t3.本软件需联网使用，不得用于商业用途，仅供学习交流，如作他用\n\b\b\b\b所承受的法"+
                                                   "律责任一概与作者无关，使用时间：6：30-23：00，此版本为最终版！")
    self.right_recommend_label.setObjectName('right_lable') 
    self.right_layout.addWidget(self.right_recommend_label, 0,0,0,0)
   

    self.left_close.setFixedSize(15,15) # 设置关闭按钮的大小
    self.left_visit.setFixedSize(15, 15) # 设置按钮大小
    self.left_mini.setFixedSize(15, 15) # 设置最小化按钮大小
    self.left_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
    self.left_visit.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
    self.left_mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
    self.left_widget.setStyleSheet('''
     QPushButton{border:none;color:white;}
     QPushButton#left_label{
        border:none;
        border-bottom:1px solid white;
        font-size:18px;
        font-weight:700;
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                }
          QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
          QPushButton#left_label:hover{border-left:6px solid blue;font-weight:700;}
                ''')


    self.right_widget.setStyleSheet('''
        QWidget#right_widget{
        color:#232C51;
        background:white;
        border-top:1px solid darkGray;
        border-bottom:1px solid darkGray;
        border-right:1px solid darkGray;
        border-top-right-radius:10px;
        border-bottom-right-radius:10px;
                 }
          QLabel#right_lable{
            border:none;
            font-size:16px;
            font-weight:700;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
         ''')
    self.setWindowOpacity(0.9) # 设置窗口透明度
    self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
    self.setWindowFlag(QtCore.Qt.FramelessWindowHint) # 隐藏边框

    self.main_widget.setStyleSheet('''
            QWidget#left_widget{
            background:gray;
            border-top:1px solid white;
            border-bottom:1px solid white;
            border-left:1px solid white;
            border-top-left-radius:10px;
            border-bottom-left-radius:10px;
            }
        ''')
    self.main_layout.setSpacing(0)
  def backpagehome(self):
    self.main_widget.close()
    self.setFixedSize(960,700)
    self.main_widget = QtWidgets.QWidget() # 创建窗口主部件
    self.main_layout = QtWidgets.QGridLayout() # 创建主部件的网格布局
    self.main_widget.setLayout(self.main_layout) # 设置窗口主部件布局为网格布局

    self.left_widget = QtWidgets.QWidget() # 创建左侧部件
    self.left_widget.setObjectName('left_widget')
    self.left_layout = QtWidgets.QGridLayout() # 创建左侧部件的网格布局层
    self.left_widget.setLayout(self.left_layout) # 设置左侧部件布局为网格

    self.right_widget = QtWidgets.QWidget() # 创建右侧部件
    self.right_widget.setObjectName('right_widget')
    self.right_layout = QtWidgets.QGridLayout()
    self.right_widget.setLayout(self.right_layout) # 设置右侧部件布局为网格

    self.main_layout.addWidget(self.left_widget,0,0,12,2) # 左侧部件在第0行第0列，占8行3列
    self.main_layout.addWidget(self.right_widget,0,2,12,10) # 右侧部件在第0行第3列，占8行9列
    self.setCentralWidget(self.main_widget) # 设置窗口主部件
    self.left_close = QtWidgets.QPushButton("X") # 关闭按钮
    self.left_close.clicked.connect(self.closeClick)
    self.left_visit = QtWidgets.QPushButton("") # 空白按钮
    self.left_mini = QtWidgets.QPushButton("-") # 最小化按钮
    self.left_mini.clicked.connect(self.hiddeClick)
    self.left_label_1 = QtWidgets.QPushButton("信息收集")
    self.left_label_1.setObjectName('left_label')
    self.left_label_1.clicked.connect(self.page1)
    self.left_label_2 = QtWidgets.QPushButton("查寝签到")
    self.left_label_2.clicked.connect(self.page2)
    self.left_label_2.setObjectName('left_label')
    self.left_label_3 = QtWidgets.QPushButton("首页👉")
    self.left_label_3.clicked.connect(self.pagehome)
    self.left_label_3.setObjectName('left_label')
    self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.comment',color='white'),"联系作者")
    self.left_button_7.clicked.connect(self.skipurl)
    self.left_button_7.setObjectName('left_button')
    self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.star',color='white'),"检查版本")
    self.left_button_8.clicked.connect(self.checkVersion)

    self.left_button_8.setObjectName('left_button')
    self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa.question',color='white'),"遇到问题")
    self.left_button_9.clicked.connect(self.skipurl)
    self.left_button_9.setObjectName('left_button')
    self.left_xxx = QtWidgets.QPushButton("作者:小新")
    self.left_xxx.setObjectName('left_button')
    self.left_layout.addWidget(self.left_xxx, 13, 0, 1, 3)
    self.left_layout.addWidget(self.left_mini, 0, 0,1,1)
    self.left_layout.addWidget(self.left_close, 0, 2,1,1)
    self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
    self.left_layout.addWidget(self.left_label_1,1,0,1,3)
    self.left_layout.addWidget(self.left_label_2, 5, 0,1,3)
    self.left_layout.addWidget(self.left_label_3, 9, 0,1,3)
    self.left_layout.addWidget(self.left_button_7, 10, 0,1,3)
    self.left_layout.addWidget(self.left_button_8, 11, 0,1,3)
    self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)

    self.right_recommend_label = QtWidgets.QLabel("欢迎使用今日校园信息收集和查寝签到软件（南京晓庄学院版），"+
                                                   "请仔细阅读用前须知：\n\t1.信息收集:选择你所在的校区后，"+
                                                   "填写用于登录信息门户的学号和\n\b\b\b\b密码，填写接收信息的邮箱，"+"点击start按钮等待约7秒，出现结果提示。"+"\n\t2.查寝签到:"+
                                                   "选择你所在校区后，填写用于登录信息门户的学号和密\n\b\b\b\b码，填写接收信息的邮箱，上传签到照片，"+
                                                   "点击start按钮等待约7秒，出\n\b\b\b\b现结果提示。"+"\n\t3.本软件需联网使用，不得用于商业用途，仅供学习交流，如作他用\n\b\b\b\b所承受的法"+
                                                   "律责任一概与作者无关，使用时间：6：30-23：00，此版本为最终版本！")
    self.right_recommend_label.setObjectName('right_lable') 
    self.right_layout.addWidget(self.right_recommend_label, 0,0,0,0)
   

    self.left_close.setFixedSize(15,15) # 设置关闭按钮的大小
    self.left_visit.setFixedSize(15, 15) # 设置按钮大小
    self.left_mini.setFixedSize(15, 15) # 设置最小化按钮大小
    self.left_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
    self.left_visit.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
    self.left_mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
    self.left_widget.setStyleSheet('''
     QPushButton{border:none;color:white;}
     QPushButton#left_label{
        border:none;
        border-bottom:1px solid white;
        font-size:18px;
        font-weight:700;
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                }
          QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
          QPushButton#left_label:hover{border-left:6px solid blue;font-weight:700;}
                ''')


    self.right_widget.setStyleSheet('''
        QWidget#right_widget{
        color:#232C51;
        background:white;
        border-top:1px solid darkGray;
        border-bottom:1px solid darkGray;
        border-right:1px solid darkGray;
        border-top-right-radius:10px;
        border-bottom-right-radius:10px;
                 }
          QLabel#right_lable{
            border:none;
            font-size:16px;
            font-weight:700;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
         ''')
    self.setWindowOpacity(0.9) # 设置窗口透明度
    self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
    self.setWindowFlag(QtCore.Qt.FramelessWindowHint) # 隐藏边框

    self.main_widget.setStyleSheet('''
            QWidget#left_widget{
            background:gray;
            border-top:1px solid white;
            border-bottom:1px solid white;
            border-left:1px solid white;
            border-top-left-radius:10px;
            border-bottom-left-radius:10px;
            }
        ''')
    self.main_layout.setSpacing(0)
  def page1(self):

    sender =self.sender()
    self.main_widget.close()
    self.setFixedSize(960,700)
    self.main_widget = QtWidgets.QWidget() # 创建窗口主部件
    self.main_layout = QtWidgets.QGridLayout() # 创建主部件的网格布局
    self.main_widget.setLayout(self.main_layout) # 设置窗口主部件布局为网格布局

    self.left_widget = QtWidgets.QWidget() # 创建左侧部件
    self.left_widget.setObjectName('left_widget')
    self.left_layout = QtWidgets.QGridLayout() # 创建左侧部件的网格布局层
    self.left_widget.setLayout(self.left_layout) # 设置左侧部件布局为网格

    self.right_widget = QtWidgets.QWidget() # 创建右侧部件
    self.right_widget.setObjectName('right_widget')
    self.right_layout = QtWidgets.QGridLayout()
    self.right_widget.setLayout(self.right_layout) # 设置右侧部件布局为网格

    self.main_layout.addWidget(self.left_widget,0,0,12,2) # 左侧部件在第0行第0列，占8行3列
    self.main_layout.addWidget(self.right_widget,0,2,12,10) # 右侧部件在第0行第3列，占8行9列
    self.setCentralWidget(self.main_widget) # 设置窗口主部件
    self.left_close = QtWidgets.QPushButton("X") # 关闭按钮
    self.left_close.clicked.connect(self.closeClick)
    self.left_visit = QtWidgets.QPushButton("") # 空白按钮
    self.left_mini = QtWidgets.QPushButton("-") # 最小化按钮
    self.left_mini.clicked.connect(self.hiddeClick)
    self.left_label_1 = QtWidgets.QPushButton("信息收集")
    self.left_label_1.setObjectName('left_label')
    self.left_label_1.clicked.connect(self.page1)
    self.left_label_2 = QtWidgets.QPushButton("查寝签到")
    self.left_label_2.clicked.connect(self.page2)
    self.left_label_2.setObjectName('left_label')
    self.left_label_3 = QtWidgets.QPushButton("首页👉")
    self.left_label_3.clicked.connect(self.backpagehome)
    self.left_label_3.setObjectName('left_label')
    self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.comment',color='white'),"联系作者")
    self.left_button_7.clicked.connect(self.skipurl)
    self.left_button_7.setObjectName('left_button')
    self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.star',color='white'),"检查版本")
    self.left_button_8.clicked.connect(self.checkVersion)
    self.left_button_8.setObjectName('left_button')
    self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa.question',color='white'),"遇到问题")
    self.left_button_9.clicked.connect(self.skipurl)
    self.left_button_9.setObjectName('left_button')
    self.left_xxx = QtWidgets.QPushButton("作者:小新")
    self.left_xxx.setObjectName('left_button')
    self.left_layout.addWidget(self.left_xxx, 13, 0, 1, 3)
    self.left_layout.addWidget(self.left_mini, 0, 0,1,1)
    self.left_layout.addWidget(self.left_close, 0, 2,1,1)
    self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
    self.left_layout.addWidget(self.left_label_1,1,0,1,3)
    self.left_layout.addWidget(self.left_label_2, 5, 0,1,3)
    self.left_layout.addWidget(self.left_label_3, 9, 0,1,3)
    self.left_layout.addWidget(self.left_button_7, 10, 0,1,3)
    self.left_layout.addWidget(self.left_button_8, 11, 0,1,3)
    self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)
    



  

    self.right_recommend_label = QtWidgets.QLabel("校区")
    self.right_recommend_label.setObjectName('right_lable')
    self.right_layout.addWidget(self.right_recommend_label, 0, 1, 1, 1,QtCore.Qt.AlignCenter)
    self.comboBox= QtWidgets.QComboBox()
    self.comboBox.addItem("")
    self.comboBox.addItem("")
    self.comboBox.setObjectName("comboBox")
    _translate = QtCore.QCoreApplication.translate
    self.comboBox.setItemText(0, _translate("MainWindow", "方山校区"))
    self.comboBox.setItemText(1, _translate("MainWindow", "莫愁校区"))
    self.right_layout.addWidget(self.comboBox, 1, 1, 1, 1,QtCore.Qt.AlignCenter)
    self.right_recommend_labe2 = QtWidgets.QLabel("学号")
    self.right_recommend_labe2.setObjectName('right_lable')
    self.right_layout.addWidget(self.right_recommend_labe2, 2, 1, 1, 1,QtCore.Qt.AlignCenter)
    self.line_edit_obj1 = QLineEdit()
    self.line_edit_obj1.setObjectName('line_edit')
    self.line_edit_obj1.setMaxLength(8)
    self.line_edit_obj1.setValidator(QIntValidator())
    self.right_layout.addWidget(self.line_edit_obj1, 3, 1, 1, 1,QtCore.Qt.AlignCenter)
    self.right_recommend_labe3 = QtWidgets.QLabel("密码")
    self.right_recommend_labe3.setObjectName('right_lable')
    self.right_layout.addWidget(self.right_recommend_labe3, 4, 1, 1, 1,QtCore.Qt.AlignCenter)
    self.line_edit_obj2 = QLineEdit()
    self.line_edit_obj2.setEchoMode(QLineEdit.Password)
    self.line_edit_obj2.setObjectName('line_edit')
    self.right_layout.addWidget(self.line_edit_obj2, 5, 1, 1, 1,QtCore.Qt.AlignCenter)
    self.right_recommend_labe4 = QtWidgets.QLabel("邮箱")
    self.right_recommend_labe4.setObjectName('right_lable')
    self.right_layout.addWidget(self.right_recommend_labe4, 6, 1, 1, 1,QtCore.Qt.AlignCenter)
    self.line_edit_obj3 = QLineEdit()
    self.line_edit_obj3.setObjectName('line_edit')
    self.right_layout.addWidget(self.line_edit_obj3, 7, 1, 1, 1,QtCore.Qt.AlignCenter)
    #self.right_recommend_labe5 = QtWidgets.QLabel("start")
    #self.right_recommend_labe5.setObjectName('right_lable')
    #self.right_layout.addWidget(self.right_recommend_labe5, 4, 1, 1, 1,QtCore.Qt.AlignCenter)



    self.recommend_button_1 = QtWidgets.QPushButton()
    self.recommend_button_1.setText("Start") # 设置按钮文本
    #self.recommend_button_1.setIcon(QtGui.QIcon('按钮.png')) # 设置按钮图标
    #self.recommend_button_1.setIconSize(QtCore.QSize(96,37)) # 设置图标大小
    #self.recommend_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon) # 设置按钮形式为上图下文
    self.right_layout.addWidget(self.recommend_button_1, 8, 1, 1, 1,QtCore.Qt.AlignCenter)
    self.recommend_button_1.clicked.connect(self.collection)

    

   
    

    self.left_close.setFixedSize(15,15) # 设置关闭按钮的大小
    self.left_visit.setFixedSize(15, 15) # 设置按钮大小
    self.left_mini.setFixedSize(15, 15) # 设置最小化按钮大小
    self.left_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
    self.left_visit.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
    self.left_mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
    self.left_widget.setStyleSheet('''
    QPushButton{border:none;color:white;}
     QPushButton#left_label{
     border:none;
     border-bottom:1px solid white;
     font-size:18px;
     font-weight:700;
     font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
              }
      QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
      QPushButton#left_label:hover{border-left:6px solid blue;font-weight:700;}
         ''')

    self.right_widget.setStyleSheet('''
          QWidget#right_widget{
            color:#232C51;
            background:white;
            border-top:1px solid darkGray;
            border-bottom:1px solid darkGray;
            border-right:1px solid darkGray;
            border-top-right-radius:10px;
            border-bottom-right-radius:10px;
          }
          QLabel#right_lable{
            border:none;
            font-size:16px;
            font-weight:700;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
          }
        ''')
    self.setWindowOpacity(0.9) # 设置窗口透明度
    self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
    self.setWindowFlag(QtCore.Qt.FramelessWindowHint) # 隐藏边框

    self.main_widget.setStyleSheet('''
            QWidget#left_widget{
            background:gray;
            border-top:1px solid white;
            border-bottom:1px solid white;
            border-left:1px solid white;
            border-top-left-radius:10px;
            border-bottom-left-radius:10px;
            }
            ''')
    self.main_layout.setSpacing(0)
  def page2(self):
    sender =self.sender()
    self.main_widget.close()
    self.setFixedSize(960,700)
    self.main_widget = QtWidgets.QWidget() # 创建窗口主部件
    self.main_layout = QtWidgets.QGridLayout() # 创建主部件的网格布局
    self.main_widget.setLayout(self.main_layout) # 设置窗口主部件布局为网格布局

    self.left_widget = QtWidgets.QWidget() # 创建左侧部件
    self.left_widget.setObjectName('left_widget')
    self.left_layout = QtWidgets.QGridLayout() # 创建左侧部件的网格布局层
    self.left_widget.setLayout(self.left_layout) # 设置左侧部件布局为网格

    self.right_widget = QtWidgets.QWidget() # 创建右侧部件
    self.right_widget.setObjectName('right_widget')
    self.right_layout = QtWidgets.QGridLayout()
    self.right_widget.setLayout(self.right_layout) # 设置右侧部件布局为网格

    self.main_layout.addWidget(self.left_widget,0,0,12,2) # 左侧部件在第0行第0列，占8行3列
    self.main_layout.addWidget(self.right_widget,0,2,12,10) # 右侧部件在第0行第3列，占8行9列
    self.setCentralWidget(self.main_widget) # 设置窗口主部件
    self.left_close = QtWidgets.QPushButton("X") # 关闭按钮
    self.left_close.clicked.connect(self.closeClick)
    self.left_visit = QtWidgets.QPushButton("") # 空白按钮
    self.left_mini = QtWidgets.QPushButton("-") # 最小化按钮
    self.left_mini.clicked.connect(self.hiddeClick)
    self.left_label_1 = QtWidgets.QPushButton("信息收集")
    self.left_label_1.clicked.connect(self.page1)
    self.left_label_1.setObjectName('left_label')
    self.left_label_1.clicked.connect(self.page1)
    self.left_label_2 = QtWidgets.QPushButton("查寝签到")
    self.left_label_2.setObjectName('left_label')
    self.left_label_3 = QtWidgets.QPushButton("首页👉")
    self.left_label_3.clicked.connect(self.backpagehome)
    self.left_label_3.setObjectName('left_label')
    self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.comment',color='white'),"联系作者")
    self.left_button_7.clicked.connect(self.skipurl)
    self.left_button_7.setObjectName('left_button')
    self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.star',color='white'),"检查版本")
    self.left_button_8.clicked.connect(self.checkVersion)
    self.left_button_8.setObjectName('left_button')
    self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa.question',color='white'),"遇到问题")
    self.left_button_9.clicked.connect(self.skipurl)
    self.left_button_9.setObjectName('left_button')
    self.left_xxx = QtWidgets.QPushButton("作者:小新")
    self.left_xxx.setObjectName('left_button')
    self.left_layout.addWidget(self.left_mini, 0, 0,1,1)
    self.left_layout.addWidget(self.left_close, 0, 2,1,1)
    self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
    self.left_layout.addWidget(self.left_label_1,1,0,1,3)
    self.left_layout.addWidget(self.left_label_2, 5, 0,1,3)
    self.left_layout.addWidget(self.left_label_3, 9, 0,1,3)
    self.left_layout.addWidget(self.left_button_7, 10, 0,1,3)
    self.left_layout.addWidget(self.left_button_8, 11, 0,1,3)
    self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)
    self.left_layout.addWidget(self.left_xxx, 13, 0, 1, 3)

    self.right_recommend_label = QtWidgets.QLabel("校区")
    self.right_recommend_label.setObjectName('right_lable')
    self.right_layout.addWidget(self.right_recommend_label, 0, 1, 1, 1,QtCore.Qt.AlignCenter)
    self.comboBox= QtWidgets.QComboBox()
    self.comboBox.addItem("")
    self.comboBox.addItem("")
    self.comboBox.setObjectName("comboBox")
    _translate = QtCore.QCoreApplication.translate
    self.comboBox.setItemText(0, _translate("MainWindow", "方山校区"))
    self.comboBox.setItemText(1, _translate("MainWindow", "莫愁校区"))
    self.right_layout.addWidget(self.comboBox, 1, 1, 1, 1,QtCore.Qt.AlignCenter)
    self.right_recommend_labe2 = QtWidgets.QLabel("学号")
    self.right_recommend_labe2.setObjectName('right_lable')
    self.right_layout.addWidget(self.right_recommend_labe2, 2, 1, 1, 1,QtCore.Qt.AlignCenter)
    self.line_edit_obj1 = QLineEdit()
    self.line_edit_obj1.setObjectName('line_edit')
    self.line_edit_obj1.setMaxLength(8)
    self.line_edit_obj1.setValidator(QIntValidator())
    self.right_layout.addWidget(self.line_edit_obj1, 3, 1, 1, 1,QtCore.Qt.AlignCenter)
    self.right_recommend_labe3 = QtWidgets.QLabel("密码")
    self.right_recommend_labe3.setObjectName('right_lable')
    self.right_layout.addWidget(self.right_recommend_labe3, 4, 1, 1, 1,QtCore.Qt.AlignCenter)
    self.line_edit_obj2 = QLineEdit()
    self.line_edit_obj2.setEchoMode(QLineEdit.Password)
    self.line_edit_obj2.setObjectName('line_edit')
    self.right_layout.addWidget(self.line_edit_obj2, 5, 1, 1, 1,QtCore.Qt.AlignCenter)
    self.right_recommend_labe4 = QtWidgets.QLabel("邮箱")
    self.right_recommend_labe4.setObjectName('right_lable')
    self.right_layout.addWidget(self.right_recommend_labe4, 6, 1, 1, 1,QtCore.Qt.AlignCenter)
    self.line_edit_obj3 = QLineEdit()
    self.line_edit_obj3.setObjectName('line_edit')
    self.right_layout.addWidget(self.line_edit_obj3, 7, 1, 1, 1,QtCore.Qt.AlignCenter)
    self.right_recommend_labe5 = QtWidgets.QLabel("签到照片")
    self.right_recommend_labe5.setObjectName('right_lable')
    self.right_layout.addWidget(self.right_recommend_labe5, 8, 1, 1, 1,QtCore.Qt.AlignCenter)

    self.file=QtWidgets.QPushButton()
    self.file.setText("请选择...")
    self.file.setObjectName("file")
    self.file.clicked.connect(self.pathmsg)
    self.right_layout.addWidget(self.file,9,1,1,1,QtCore.Qt.AlignCenter)
    self.file.setStyleSheet(
            "QPushButton{background:#6DDF6D;border-radius:5px;}"
            "QPushButton:hover{background:green;}"
             
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{border: None;}"  # 按下时的样式
        )


    
    
    #self.right_recommend_labe5 = QtWidgets.QLabel("start")
    #self.right_recommend_labe5.setObjectName('right_lable')    
    #self.right_layout.addWidget(self.right_recommend_labe5, 4, 1, 1, 1,QtCore.Qt.AlignCenter)
    self.recommend_button_1 = QtWidgets.QPushButton()
    self.recommend_button_1.setText("Start") # 设置按钮文本
    #self.recommend_button_1.setIcon(QtGui.QIcon('按钮.png')) # 设置按钮图标
    self.recommend_button_1.setIconSize(QtCore.QSize(96,37)) # 设置图标大小
    #self.recommend_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon) # 设置按钮形式为上图下文
    self.right_layout.addWidget(self.recommend_button_1, 10, 1, 1, 1,QtCore.Qt.AlignCenter)
    self.recommend_button_1.clicked.connect(self.sleepsign)


    self.left_close.setFixedSize(15,15) # 设置关闭按钮的大小
    self.left_visit.setFixedSize(15, 15) # 设置按钮大小
    self.left_mini.setFixedSize(15, 15) # 设置最小化按钮大小
    self.left_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
    self.left_visit.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
    self.left_mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
    self.left_widget.setStyleSheet('''
    QPushButton{border:none;color:white;}
     QPushButton#left_label{
     border:none;
     border-bottom:1px solid white;
     font-size:18px;
     font-weight:700;
     font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
              }
      QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
      QPushButton#left_label:hover{border-left:6px solid blue;font-weight:700;}
         ''')

    self.right_widget.setStyleSheet('''
          QWidget#right_widget{
            color:#232C51;
            background:white;
            border-top:1px solid darkGray;
            border-bottom:1px solid darkGray;
            border-right:1px solid darkGray;
            border-top-right-radius:10px;
            border-bottom-right-radius:10px;
          }
          QLabel#right_lable{
            border:none;
            font-size:16px;
            font-weight:700;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
          }
        ''')
    self.setWindowOpacity(0.9) # 设置窗口透明度
    self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
    self.setWindowFlag(QtCore.Qt.FramelessWindowHint) # 隐藏边框

    self.main_widget.setStyleSheet('''
            QWidget#left_widget{
            background:gray;
            border-top:1px solid white;
            border-bottom:1px solid white;
            border-left:1px solid white;
            border-top-left-radius:10px;
            border-bottom-left-radius:10px;
            }
            ''')
    self.main_layout.setSpacing(0)
  def checkVersion(self):
    nowVersion='1.0.2（最终版）'

    QMessageBox.warning(self,
                                    "版本"+nowVersion,  
                                    "项目停止，如失效请手动签到！",  
                                    QMessageBox.Yes)
  def skipurl(self):
      sender=self.sender()
      web.open('tencent://message/?uin=2448341003')
  def closeClick(self):
      sender =self.sender()
      qApp=QtWidgets.QApplication.instance()
      qApp.quit()
  def hiddeClick(self):
      sender=self.sender()
      self.showMinimized()
  def mouseMoveEvent(self, e: QMouseEvent): # 重写移动事件
    self._endPos = e.pos() - self._startPos
    self.move(self.pos() + self._endPos)
  def mousePressEvent(self, e: QMouseEvent):
    if e.button() == Qt.LeftButton:
      self._isTracking = True
      self._startPos = QPoint(e.x(), e.y())
  def mouseReleaseEvent(self, e: QMouseEvent):
    if e.button() == Qt.LeftButton:
      self._isTracking = False
      self._startPos = None
      self._endPos = None
  def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Label.setText(_translate("MainWindow", "学号:"))
        self.Label_2.setText(_translate("MainWindow", "密码:"))
        self.Label_3.setText(_translate("MainWindow", "邮箱:"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.comboBox.setItemText(0, _translate("MainWindow", "方山校区"))
        self.comboBox.setItemText(1, _translate("MainWindow", "莫愁校区"))
        self.Label_4.setText(_translate("MainWindow", "校区:"))
  def pathmsg(self,Filepath):
        m = QFileDialog.getOpenFileName()# 起始路径
        if list(m)[0]!='':
         self.file.setText(list(m)[0])
        else:
         self.file.setText('请选择...')
  def collection(self):
      #print(self.comboBox.currentText())
      #print(self.line_edit_obj1.text())
       config={'Version': 'by小新', 'debug': False, 'notifyOption': 
           {'method': 2, 'mailApiUrl': '', 'smtpOption': 
            {'userName': 'imxiaoxin1101@163.com', 'passWord': 
             'LSXFJGOKFFAZGDEZ', 'server': 'smtp.163.com'}, 
             'qmsgOption': {'key': '', 'baseUrl': 'https://qmsg.zendee.cn/'},
            'qywxOption': {'corpid': '', 'corpsecret': '', 'agentid': ''}},
           'ocrOption': {'SecretId': 'APIid', 'SecretKey': 'APIkey'}, 
           'httpProxy': '', 'users': [{'user': {'type': 0, 'schoolName': '南京晓庄学院',
                                               'username': '', 'password': '',
                                              'address': '', 
                                              'notifyOption': {'rcvAcc': ''}, 
                                              'lon': '', 'lat': '', 'checkTitle': 1, 
                                              'onlyRequired': 1, 'forms': 
                                              [{'form': {'title': '你今天的体温状况？', 'value': '正常（37.3℃以下）'}}, 
                                               {'form': {'title': '今天健康码颜色（以当地健康码为准）？', 'value': '绿码'}},
                                              {'form': {'title': '今天你是否位于中高风险地区？', 'value': '否'}}, 
                                              {'form': {'title': '今天你及共同居住人是否有发热、咳嗽、胸闷、腹泻等症状？', 'value': '否'}},
                                             {'form': {'title': '今天你及共同居住人出现体温异常，且有咳嗽、胸闷、腹泻等症状，请填写具体情况', 'value': ''}},
                                            {'form': {'title': '今天你及共同居住人是否有隔离情况？', 'value': '无隔离'}}, 
                                            {'form': {'title': '今天如有隔离情况（居家隔离、集中隔离）请填写具体情况和隔离地点', 'value': ''}}]}}]} 
       #print(config['users'][0]['user']['username'])
       config['users'][0]['user']['username']=self.line_edit_obj1.text()
       config['users'][0]['user']['password']=self.line_edit_obj2.text()
       config['users'][0]['user']['notifyOption']['rcvAcc']=self.line_edit_obj3.text()
       if self.comboBox.currentText() =='方山校区':
          config['users'][0]['user']['adress']='中国江苏省南京市江宁区淳化街道吉祥路'
          config['users'][0]['user']['lon']='118.90998'
          config['users'][0]['user']['lat']='31.89996'
          index.config=config
          message=index.main()
          if 'SUCCESS' in message:
               QMessageBox.warning(self,
                                    "结果通知",  
                                    message+",可在邮箱查看详细信息",  
                                    QMessageBox.Yes)   

          else:
               QMessageBox.warning(self,
                                    "结果通知",  
                                    message+",可在邮箱查看详细信息",  
                                    QMessageBox.Yes)    
       else:
          config['users'][0]['user']['adress']='中国江苏省南京市建邺区梅花街'
          config['users'][0]['user']['lon']='118.758837'
          config['users'][0]['user']['lat']='32.041957'
          index.config=config
          message=index.main()
          if 'SUCCESS' in message:
               QMessageBox.warning(self,
                                    "结果通知",  
                                    message+",可在邮箱查看详细信息",  
                                    QMessageBox.Yes)   

          else:
               QMessageBox.warning(self,
                                    "结果通知",  
                                    message+",可在邮箱查看详细信息",  
                                    QMessageBox.Yes)   
  def sleepsign(self):
       config={'Version': 'by小新', 'debug': False, 'notifyOption': 
           {'method': 2, 'mailApiUrl': '', 'smtpOption': 
            {'userName': 'imxiaoxin1101@163.com', 'passWord': 
             'LSXFJGOKFFAZGDEZ', 'server': 'smtp.163.com'}, 
             'qmsgOption': {'key': '', 'baseUrl': 'https://qmsg.zendee.cn/'},
            'qywxOption': {'corpid': '', 'corpsecret': '', 'agentid': ''}},
           'ocrOption': {'SecretId': 'APIid', 'SecretKey': 'APIkey'}, 
           'httpProxy': '', 'users': [{'user': {'type': 2, 'schoolName': '南京晓庄学院',
                                               'username': '', 'password': '',
                                              'address': '', 
                                              'notifyOption': {'rcvAcc': ''}, 
                                              'lon': '', 'lat': '', 'abnormalReason': '', 
                                              'photo': '', 
                                              }}]} 
       #print(config['users'][0]['user']['username'])
       config['users'][0]['user']['username']=self.line_edit_obj1.text()
       config['users'][0]['user']['password']=self.line_edit_obj2.text()
       config['users'][0]['user']['notifyOption']['rcvAcc']=self.line_edit_obj3.text()
       if self.file.text()!='请选择...':
        config['users'][0]['user']['photo']=self.file.text()
       else:
        QMessageBox.warning(self, "友情提示","你还未选择照片",  QMessageBox.Yes)   
        return False
       if self.comboBox.currentText() =='方山校区':
          config['users'][0]['user']['adress']='中国江苏省南京市江宁区淳化街道吉祥路'
          config['users'][0]['user']['lon']='118.90998'
          config['users'][0]['user']['lat']='31.89996'
          index.config=config
          message=index.main()
          if 'SUCCESS' in message:
               QMessageBox.warning(self,
                                    "结果通知",  
                                    message+",可在邮箱查看详细信息",  
                                    QMessageBox.Yes)   

          else:
               QMessageBox.warning(self,
                                    "结果通知",  
                                    message+",可在邮箱查看详细信息",  
                                    QMessageBox.Yes)    
       else:
          config['users'][0]['user']['adress']='中国江苏省南京市建邺区梅花街'
          config['users'][0]['user']['lon']='118.758837'
          config['users'][0]['user']['lat']='32.041957'
          index.config=config
          message=index.main()
          if 'SUCCESS' in message:
               QMessageBox.warning(self,
                                    "结果通知",  
                                    message+",可在邮箱查看详细信息",  
                                    QMessageBox.Yes)   

          else:
               QMessageBox.warning(self,
                                    "结果通知",  
                                    message+",可在邮箱查看详细信息",  
                                    QMessageBox.Yes)   
      
              
          
      
def main():
  app = QtWidgets.QApplication(sys.argv)
  gui = MainUi()
  gui.show()
  sys.exit(app.exec_())


if __name__ == '__main__':
  main()