# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Git\ProtocalTool\UI\UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1035, 618)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_dataFrame = QtWidgets.QLabel(self.centralwidget)
        self.label_dataFrame.setTextFormat(QtCore.Qt.AutoText)
        self.label_dataFrame.setObjectName("label_dataFrame")
        self.verticalLayout_3.addWidget(self.label_dataFrame)
        self.Text_dataFrame = QtWidgets.QTextEdit(self.centralwidget)
        self.Text_dataFrame.setObjectName("Text_dataFrame")
        self.verticalLayout_3.addWidget(self.Text_dataFrame)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.KeyDecode = QtWidgets.QPushButton(self.centralwidget)
        self.KeyDecode.setEnabled(True)
        self.KeyDecode.setToolTip("")
        self.KeyDecode.setToolTipDuration(-1)
        self.KeyDecode.setWhatsThis("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/右箭头.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.KeyDecode.setIcon(icon)
        self.KeyDecode.setIconSize(QtCore.QSize(32, 32))
        self.KeyDecode.setCheckable(False)
        self.KeyDecode.setObjectName("KeyDecode")
        self.verticalLayout.addWidget(self.KeyDecode)
        self.KeyClear = QtWidgets.QPushButton(self.centralwidget)
        self.KeyClear.setToolTip("")
        self.KeyClear.setToolTipDuration(-1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../image/回收站.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.KeyClear.setIcon(icon1)
        self.KeyClear.setIconSize(QtCore.QSize(32, 32))
        self.KeyClear.setObjectName("KeyClear")
        self.verticalLayout.addWidget(self.KeyClear)
        self.KeyOpen = QtWidgets.QPushButton(self.centralwidget)
        self.KeyOpen.setToolTip("")
        self.KeyOpen.setToolTipDuration(-1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../image/打开.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.KeyOpen.setIcon(icon2)
        self.KeyOpen.setIconSize(QtCore.QSize(32, 32))
        self.KeyOpen.setObjectName("KeyOpen")
        self.verticalLayout.addWidget(self.KeyOpen)
        self.KeySave = QtWidgets.QPushButton(self.centralwidget)
        self.KeySave.setToolTip("")
        self.KeySave.setToolTipDuration(-1)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../image/保存.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.KeySave.setIcon(icon3)
        self.KeySave.setIconSize(QtCore.QSize(32, 32))
        self.KeySave.setObjectName("KeySave")
        self.verticalLayout.addWidget(self.KeySave)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_protovalView = QtWidgets.QLabel(self.centralwidget)
        self.label_protovalView.setObjectName("label_protovalView")
        self.verticalLayout_2.addWidget(self.label_protovalView)
        self.Text_ProtocalView = QtWidgets.QTextEdit(self.centralwidget)
        self.Text_ProtocalView.setToolTip("")
        self.Text_ProtocalView.setObjectName("Text_ProtocalView")
        self.verticalLayout_2.addWidget(self.Text_ProtocalView)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1035, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_history = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_history.setMaximumSize(QtCore.QSize(524287, 524287))
        self.dockWidget_history.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dockWidget_history.setAutoFillBackground(False)
        self.dockWidget_history.setObjectName("dockWidget_history")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.treeView_history_2 = QtWidgets.QTreeView(self.dockWidgetContents_2)
        self.treeView_history_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.treeView_history_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.treeView_history_2.setBaseSize(QtCore.QSize(0, 0))
        self.treeView_history_2.setMouseTracking(False)
        self.treeView_history_2.setTabletTracking(False)
        self.treeView_history_2.setAutoScroll(True)
        self.treeView_history_2.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.treeView_history_2.setObjectName("treeView_history_2")
        self.verticalLayout_5.addWidget(self.treeView_history_2)
        self.dockWidget_history.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_history)
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionExit.setObjectName("actionExit")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionSelectAll = QtWidgets.QAction(MainWindow)
        self.actionSelectAll.setCheckable(False)
        self.actionSelectAll.setObjectName("actionSelectAll")
        self.actionhelp = QtWidgets.QAction(MainWindow)
        self.actionhelp.setObjectName("actionhelp")
        self.actionHistory = QtWidgets.QAction(MainWindow)
        self.actionHistory.setObjectName("actionHistory")
        self.actionselect = QtWidgets.QAction(MainWindow)
        self.actionselect.setObjectName("actionselect")
        self.actionopenFiles = QtWidgets.QAction(MainWindow)
        self.actionopenFiles.setObjectName("actionopenFiles")
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.actionaddProtocal = QtWidgets.QAction(MainWindow)
        self.actionaddProtocal.setObjectName("actionaddProtocal")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionopenFiles)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addAction(self.actionClear)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menu.addAction(self.actionhelp)
        self.menu.addAction(self.actionabout)
        self.menu_2.addAction(self.actionHistory)
        self.menu_2.addAction(self.actionaddProtocal)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_dataFrame.setText(_translate("MainWindow", "协议数据帧"))
        self.Text_dataFrame.setStatusTip(_translate("MainWindow", "协议数据帧"))
        self.Text_dataFrame.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">将数据帧放在这里(目前只支持utf-8)</p></body></html>"))
        self.KeyDecode.setStatusTip(_translate("MainWindow", "解析协议"))
        self.KeyDecode.setText(_translate("MainWindow", "解析"))
        self.KeyDecode.setShortcut(_translate("MainWindow", "Ctrl+D, Enter"))
        self.KeyClear.setStatusTip(_translate("MainWindow", "清除左右窗口内容"))
        self.KeyClear.setText(_translate("MainWindow", "清除"))
        self.KeyOpen.setStatusTip(_translate("MainWindow", "打开文件"))
        self.KeyOpen.setText(_translate("MainWindow", "打开"))
        self.KeySave.setStatusTip(_translate("MainWindow", "保存到文件"))
        self.KeySave.setText(_translate("MainWindow", "保存"))
        self.label_protovalView.setText(_translate("MainWindow", "协议解析结果"))
        self.Text_ProtocalView.setStatusTip(_translate("MainWindow", "协议解析结果"))
        self.menuFile.setTitle(_translate("MainWindow", "文件"))
        self.menu.setTitle(_translate("MainWindow", "帮助"))
        self.menu_2.setTitle(_translate("MainWindow", "窗口"))
        self.dockWidget_history.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.dockWidget_history.setWindowTitle(_translate("MainWindow", "历史记录"))
        self.actionClear.setText(_translate("MainWindow", "清除"))
        self.actionClear.setStatusTip(_translate("MainWindow", "清除左右窗口内容"))
        self.actionClear.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionOpen.setText(_translate("MainWindow", "打开"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "打开文件"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionClose.setText(_translate("MainWindow", "关闭"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionSave.setText(_translate("MainWindow", "保存"))
        self.actionSave.setStatusTip(_translate("MainWindow", "保存到文件"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSaveAs.setText(_translate("MainWindow", "另存为"))
        self.actionSaveAs.setStatusTip(_translate("MainWindow", "另存为文件"))
        self.actionSaveAs.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionPrint.setText(_translate("MainWindow", "打印"))
        self.actionPrint.setStatusTip(_translate("MainWindow", "打印左右窗口内容"))
        self.actionPrint.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionExit.setText(_translate("MainWindow", "退出"))
        self.actionExit.setStatusTip(_translate("MainWindow", "退出程序"))
        self.actionCopy.setText(_translate("MainWindow", "复制"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionCut.setText(_translate("MainWindow", "剪切"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionPaste.setText(_translate("MainWindow", "粘贴"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionSelectAll.setText(_translate("MainWindow", "全选"))
        self.actionSelectAll.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionhelp.setText(_translate("MainWindow", "使用说明"))
        self.actionhelp.setStatusTip(_translate("MainWindow", "使用说明"))
        self.actionhelp.setShortcut(_translate("MainWindow", "F1"))
        self.actionHistory.setText(_translate("MainWindow", "历史记录"))
        self.actionHistory.setStatusTip(_translate("MainWindow", "打开历史记录窗口"))
        self.actionHistory.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionselect.setText(_translate("MainWindow", "选择"))
        self.actionopenFiles.setText(_translate("MainWindow", "打开多个文件"))
        self.actionopenFiles.setStatusTip(_translate("MainWindow", "打开多个文件"))
        self.actionopenFiles.setShortcut(_translate("MainWindow", "Ctrl+Shift+O"))
        self.actionabout.setText(_translate("MainWindow", "关于"))
        self.actionabout.setStatusTip(_translate("MainWindow", "关于"))
        self.actionaddProtocal.setText(_translate("MainWindow", "增加协议"))
        self.actionaddProtocal.setStatusTip(_translate("MainWindow", "增加协议"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

