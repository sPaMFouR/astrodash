# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1205, 692)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 150))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnBrowse = QtWidgets.QPushButton(self.groupBox_2)
        self.btnBrowse.setMinimumSize(QtCore.QSize(100, 0))
        self.btnBrowse.setMaximumSize(QtCore.QSize(100, 50))
        self.btnBrowse.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnBrowse.setObjectName("btnBrowse")
        self.gridLayout_2.addWidget(self.btnBrowse, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.lineEditInputFilename = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditInputFilename.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.lineEditInputFilename.setFont(font)
        self.lineEditInputFilename.setAutoFillBackground(False)
        self.lineEditInputFilename.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditInputFilename.setReadOnly(False)
        self.lineEditInputFilename.setObjectName("lineEditInputFilename")
        self.horizontalLayout_8.addWidget(self.lineEditInputFilename)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_2)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 390))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 240))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 223, 198))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.checkBoxKnownZ = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBoxKnownZ.setChecked(True)
        self.checkBoxKnownZ.setObjectName("checkBoxKnownZ")
        self.horizontalLayout_13.addWidget(self.checkBoxKnownZ)
        self.lineEditKnownZ = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditKnownZ.setObjectName("lineEditKnownZ")
        self.horizontalLayout_13.addWidget(self.lineEditKnownZ)
        self.horizontalLayout_13.setStretch(0, 2)
        self.horizontalLayout_13.setStretch(1, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBoxClassifyHost = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBoxClassifyHost.setObjectName("checkBoxClassifyHost")
        self.horizontalLayout.addWidget(self.checkBoxClassifyHost)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.lineEditMinWave = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditMinWave.setObjectName("lineEditMinWave")
        self.gridLayout.addWidget(self.lineEditMinWave, 0, 1, 1, 1)
        self.lineEditMaxWave = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditMaxWave.setObjectName("lineEditMaxWave")
        self.gridLayout.addWidget(self.lineEditMaxWave, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lineEditSmooth = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditSmooth.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineEditSmooth.setObjectName("lineEditSmooth")
        self.horizontalLayout_4.addWidget(self.lineEditSmooth)
        self.horizontalSliderSmooth = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.horizontalSliderSmooth.setMaximum(20)
        self.horizontalSliderSmooth.setProperty("value", 6)
        self.horizontalSliderSmooth.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderSmooth.setObjectName("horizontalSliderSmooth")
        self.horizontalLayout_4.addWidget(self.horizontalSliderSmooth)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBoxRlap = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBoxRlap.setObjectName("checkBoxRlap")
        self.verticalLayout_3.addWidget(self.checkBoxRlap)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_5.setStretch(2, 2)
        self.verticalLayout_5.setStretch(3, 1)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_6.addWidget(self.scrollArea)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btnRefit = QtWidgets.QPushButton(self.groupBox)
        self.btnRefit.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btnRefit.setObjectName("btnRefit")
        self.horizontalLayout_6.addWidget(self.btnRefit)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btnCancel = QtWidgets.QPushButton(self.groupBox)
        self.btnCancel.setMinimumSize(QtCore.QSize(0, 0))
        self.btnCancel.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout_7.addWidget(self.btnCancel)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.verticalLayout.addWidget(self.groupBox)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.btnQuit = QtWidgets.QPushButton(self.centralwidget)
        self.btnQuit.setMaximumSize(QtCore.QSize(120, 16777215))
        self.btnQuit.setObjectName("btnQuit")
        self.horizontalLayout_15.addWidget(self.btnQuit)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 6)
        self.verticalLayout.setStretch(4, 2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayout_5.addWidget(self.listWidget)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(-1, -1, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_10.addWidget(self.label_6)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.labelBestHostType = QtWidgets.QLabel(self.groupBox_3)
        self.labelBestHostType.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.labelBestHostType.setScaledContents(False)
        self.labelBestHostType.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBestHostType.setWordWrap(False)
        self.labelBestHostType.setObjectName("labelBestHostType")
        self.horizontalLayout_10.addWidget(self.labelBestHostType)
        self.labelBestSnType = QtWidgets.QLabel(self.groupBox_3)
        self.labelBestSnType.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBestSnType.setObjectName("labelBestSnType")
        self.horizontalLayout_10.addWidget(self.labelBestSnType)
        self.labelBestAgeRange = QtWidgets.QLabel(self.groupBox_3)
        self.labelBestAgeRange.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBestAgeRange.setObjectName("labelBestAgeRange")
        self.horizontalLayout_10.addWidget(self.labelBestAgeRange)
        self.verticalLayout_10.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_14.addWidget(self.label)
        self.labelBestRedshift = QtWidgets.QLabel(self.groupBox_3)
        self.labelBestRedshift.setObjectName("labelBestRedshift")
        self.horizontalLayout_14.addWidget(self.labelBestRedshift)
        self.verticalLayout_10.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_11.addWidget(self.label_2)
        self.labelBestRelProb = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.labelBestRelProb.setFont(font)
        self.labelBestRelProb.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelBestRelProb.setObjectName("labelBestRelProb")
        self.horizontalLayout_11.addWidget(self.labelBestRelProb)
        self.verticalLayout_10.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.labelRlapWarning = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setItalic(True)
        self.labelRlapWarning.setFont(font)
        self.labelRlapWarning.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRlapWarning.setObjectName("labelRlapWarning")
        self.horizontalLayout_12.addWidget(self.labelRlapWarning)
        self.labelInconsistentWarning = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setItalic(True)
        self.labelInconsistentWarning.setFont(font)
        self.labelInconsistentWarning.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInconsistentWarning.setObjectName("labelInconsistentWarning")
        self.horizontalLayout_12.addWidget(self.labelInconsistentWarning)
        self.verticalLayout_10.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_5.addLayout(self.verticalLayout_10)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.comboBoxSNType = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBoxSNType.setEditable(False)
        self.comboBoxSNType.setObjectName("comboBoxSNType")
        self.horizontalLayout_9.addWidget(self.comboBoxSNType)
        self.comboBoxAge = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBoxAge.setObjectName("comboBoxAge")
        self.horizontalLayout_9.addWidget(self.comboBoxAge)
        self.comboBoxHost = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBoxHost.setObjectName("comboBoxHost")
        self.horizontalLayout_9.addWidget(self.comboBoxHost)
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.lineEditHostFraction = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEditHostFraction.setObjectName("lineEditHostFraction")
        self.horizontalLayout_9.addWidget(self.lineEditHostFraction)
        self.horizontalSliderHostFraction = QtWidgets.QSlider(self.groupBox_4)
        self.horizontalSliderHostFraction.setMaximum(100)
        self.horizontalSliderHostFraction.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderHostFraction.setObjectName("horizontalSliderHostFraction")
        self.horizontalLayout_9.addWidget(self.horizontalSliderHostFraction)
        self.horizontalLayout_9.setStretch(0, 2)
        self.horizontalLayout_9.setStretch(1, 10)
        self.horizontalLayout_9.setStretch(2, 10)
        self.horizontalLayout_9.setStretch(3, 10)
        self.horizontalLayout_9.setStretch(4, 1)
        self.horizontalLayout_9.setStretch(5, 2)
        self.horizontalLayout_9.setStretch(6, 3)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 3, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelTemplateName = QtWidgets.QLabel(self.groupBox_4)
        self.labelTemplateName.setMinimumSize(QtCore.QSize(270, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.labelTemplateName.setFont(font)
        self.labelTemplateName.setObjectName("labelTemplateName")
        self.horizontalLayout_2.addWidget(self.labelTemplateName)
        self.labelRlapScore = QtWidgets.QLabel(self.groupBox_4)
        self.labelRlapScore.setObjectName("labelRlapScore")
        self.horizontalLayout_2.addWidget(self.labelRlapScore)
        self.pushButtonLeftTemplate = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtonLeftTemplate.setObjectName("pushButtonLeftTemplate")
        self.horizontalLayout_2.addWidget(self.pushButtonLeftTemplate)
        self.pushButtonRightTemplate = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtonRightTemplate.setObjectName("pushButtonRightTemplate")
        self.horizontalLayout_2.addWidget(self.pushButtonRightTemplate)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEditRedshift = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEditRedshift.setObjectName("lineEditRedshift")
        self.horizontalLayout_2.addWidget(self.lineEditRedshift)
        self.horizontalSliderRedshift = QtWidgets.QSlider(self.groupBox_4)
        self.horizontalSliderRedshift.setMaximum(10000)
        self.horizontalSliderRedshift.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderRedshift.setObjectName("horizontalSliderRedshift")
        self.horizontalLayout_2.addWidget(self.horizontalSliderRedshift)
        self.horizontalLayout_2.setStretch(6, 1)
        self.horizontalLayout_2.setStretch(7, 6)
        self.verticalLayout_9.addLayout(self.horizontalLayout_2)
        self.graphicsView_2 = PlotWidget(self.groupBox_4)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout_9.addWidget(self.graphicsView_2)
        self.graphicsView = PlotWidget(self.groupBox_4)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_9.addWidget(self.graphicsView)
        self.verticalLayout_9.setStretch(2, 1)
        self.verticalLayout_9.setStretch(3, 5)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 11)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.setStretch(0, 9)
        self.horizontalLayout_3.setStretch(1, 32)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1205, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DASH"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Select Spectrum"))
        self.btnBrowse.setText(_translate("MainWindow", "Browse"))
        self.lineEditInputFilename.setText(_translate("MainWindow", "Select SN File..."))
        self.groupBox.setTitle(_translate("MainWindow", "Priors"))
        self.checkBoxKnownZ.setText(_translate("MainWindow", "Known Redshift"))
        self.lineEditKnownZ.setText(_translate("MainWindow", "0"))
        self.checkBoxClassifyHost.setText(_translate("MainWindow", "Classify Host"))
        self.label_8.setText(_translate("MainWindow", "Max wave"))
        self.label_7.setText(_translate("MainWindow", "Min wave"))
        self.lineEditMinWave.setText(_translate("MainWindow", "3000"))
        self.lineEditMaxWave.setText(_translate("MainWindow", "10000"))
        self.label_3.setText(_translate("MainWindow", "Smooth"))
        self.lineEditSmooth.setText(_translate("MainWindow", "6"))
        self.checkBoxRlap.setText(_translate("MainWindow", "Calculate rlap scores"))
        self.btnRefit.setText(_translate("MainWindow", "Fit with priors"))
        self.btnCancel.setText(_translate("MainWindow", "Cancel"))
        self.btnQuit.setText(_translate("MainWindow", "Quit"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Best Matches"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Best Matches"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_6.setText(_translate("MainWindow", "Best Match"))
        self.labelBestHostType.setText(_translate("MainWindow", "Host Type"))
        self.labelBestSnType.setText(_translate("MainWindow", "SN Type"))
        self.labelBestAgeRange.setText(_translate("MainWindow", "Age Range"))
        self.label.setText(_translate("MainWindow", "Redshift:"))
        self.labelBestRedshift.setText(_translate("MainWindow", "0.0"))
        self.label_2.setText(_translate("MainWindow", "Softmax:"))
        self.labelBestRelProb.setText(_translate("MainWindow", "Rel. Prob."))
        self.labelRlapWarning.setText(_translate("MainWindow", "Warning"))
        self.labelInconsistentWarning.setText(_translate("MainWindow", "Labels"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Analyse selection"))
        self.label_9.setText(_translate("MainWindow", "Plot Template"))
        self.label_5.setText(_translate("MainWindow", "Host Fraction"))
        self.lineEditHostFraction.setText(_translate("MainWindow", "0%"))
        self.labelTemplateName.setText(_translate("MainWindow", "Template Name"))
        self.labelRlapScore.setText(_translate("MainWindow", "rlap: "))
        self.pushButtonLeftTemplate.setText(_translate("MainWindow", "<"))
        self.pushButtonRightTemplate.setText(_translate("MainWindow", ">"))
        self.label_4.setText(_translate("MainWindow", "Redshift"))
        self.lineEditRedshift.setText(_translate("MainWindow", "0"))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
