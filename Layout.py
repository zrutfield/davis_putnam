# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Layout.ui'
#
# Created: Tue May  6 03:00:25 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1021, 695)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.appWidget = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.appWidget.sizePolicy().hasHeightForWidth())
        self.appWidget.setSizePolicy(sizePolicy)
        self.appWidget.setObjectName(_fromUtf8("appWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.appWidget)
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.inputWidget = QtGui.QWidget(self.appWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputWidget.sizePolicy().hasHeightForWidth())
        self.inputWidget.setSizePolicy(sizePolicy)
        self.inputWidget.setObjectName(_fromUtf8("inputWidget"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.inputWidget)
        self.verticalLayout_8.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout_8.setMargin(0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label = QtGui.QLabel(self.inputWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_8.addWidget(self.label)
        self.premiseBox = QtGui.QPlainTextEdit(self.inputWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.premiseBox.sizePolicy().hasHeightForWidth())
        self.premiseBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.premiseBox.setFont(font)
        self.premiseBox.setObjectName(_fromUtf8("premiseBox"))
        self.verticalLayout_8.addWidget(self.premiseBox)
        self.label_2 = QtGui.QLabel(self.inputWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_8.addWidget(self.label_2)
        self.conclusionBox = QtGui.QPlainTextEdit(self.inputWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conclusionBox.sizePolicy().hasHeightForWidth())
        self.conclusionBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.conclusionBox.setFont(font)
        self.conclusionBox.setObjectName(_fromUtf8("conclusionBox"))
        self.verticalLayout_8.addWidget(self.conclusionBox)
        self.horizontalLayout_2.addWidget(self.inputWidget)
        self.outputWidget = QtGui.QWidget(self.appWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputWidget.sizePolicy().hasHeightForWidth())
        self.outputWidget.setSizePolicy(sizePolicy)
        self.outputWidget.setObjectName(_fromUtf8("outputWidget"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.outputWidget)
        self.verticalLayout_7.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_3 = QtGui.QLabel(self.outputWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_7.addWidget(self.label_3)
        self.treeDrawView = QtGui.QGraphicsView(self.outputWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.treeDrawView.sizePolicy().hasHeightForWidth())
        self.treeDrawView.setSizePolicy(sizePolicy)
        self.treeDrawView.setSizeIncrement(QtCore.QSize(1, 1))
        self.treeDrawView.setAutoFillBackground(True)
        self.treeDrawView.setInteractive(False)
        self.treeDrawView.setObjectName(_fromUtf8("treeDrawView"))
        self.verticalLayout_7.addWidget(self.treeDrawView)
        self.validityLabel = QtGui.QLabel(self.outputWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.validityLabel.sizePolicy().hasHeightForWidth())
        self.validityLabel.setSizePolicy(sizePolicy)
        self.validityLabel.setText(_fromUtf8(""))
        self.validityLabel.setObjectName(_fromUtf8("validityLabel"))
        self.verticalLayout_7.addWidget(self.validityLabel)
        self.horizontalLayout_2.addWidget(self.outputWidget)
        self.verticalLayout_9.addWidget(self.appWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionImplies = QtGui.QAction(MainWindow)
        self.actionImplies.setObjectName(_fromUtf8("actionImplies"))
        self.actionConjunction = QtGui.QAction(MainWindow)
        self.actionConjunction.setObjectName(_fromUtf8("actionConjunction"))
        self.actionDisjunction = QtGui.QAction(MainWindow)
        self.actionDisjunction.setObjectName(_fromUtf8("actionDisjunction"))
        self.actionNegation = QtGui.QAction(MainWindow)
        self.actionNegation.setObjectName(_fromUtf8("actionNegation"))
        self.actionBiconditional = QtGui.QAction(MainWindow)
        self.actionBiconditional.setObjectName(_fromUtf8("actionBiconditional"))
        self.actionInsert_Premise = QtGui.QAction(MainWindow)
        self.actionInsert_Premise.setObjectName(_fromUtf8("actionInsert_Premise"))
        self.actionInsert_Conclusion = QtGui.QAction(MainWindow)
        self.actionInsert_Conclusion.setObjectName(_fromUtf8("actionInsert_Conclusion"))
        self.actionRun = QtGui.QAction(MainWindow)
        self.actionRun.setObjectName(_fromUtf8("actionRun"))
        self.toolBar.addAction(self.actionConjunction)
        self.toolBar.addAction(self.actionDisjunction)
        self.toolBar.addAction(self.actionNegation)
        self.toolBar.addAction(self.actionImplies)
        self.toolBar.addAction(self.actionBiconditional)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRun)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Davis Putnam Tree", None))
        self.label.setText(_translate("MainWindow", "Premises", None))
        self.label_2.setText(_translate("MainWindow", "Conclusion", None))
        self.label_3.setText(_translate("MainWindow", "Davis-Putnam Tree", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionImplies.setText(_translate("MainWindow", "→", None))
        self.actionImplies.setToolTip(_translate("MainWindow", "<html><head/><body><p>Inserts the → symbol</p></body></html>", None))
        self.actionImplies.setShortcut(_translate("MainWindow", "Ctrl+$", None))
        self.actionConjunction.setText(_translate("MainWindow", "∧", None))
        self.actionConjunction.setToolTip(_translate("MainWindow", "<html><head/><body><p>Inserts the ∧ symbol</p></body></html>", None))
        self.actionConjunction.setShortcut(_translate("MainWindow", "Ctrl+&", None))
        self.actionDisjunction.setText(_translate("MainWindow", "∨", None))
        self.actionDisjunction.setShortcut(_translate("MainWindow", "Ctrl++", None))
        self.actionNegation.setText(_translate("MainWindow", "¬", None))
        self.actionNegation.setToolTip(_translate("MainWindow", "Inserts the ¬ symbol", None))
        self.actionNegation.setShortcut(_translate("MainWindow", "Ctrl+!", None))
        self.actionBiconditional.setText(_translate("MainWindow", "↔", None))
        self.actionBiconditional.setToolTip(_translate("MainWindow", "Inserts the ↔ symbol", None))
        self.actionBiconditional.setShortcut(_translate("MainWindow", "Ctrl+%", None))
        self.actionInsert_Premise.setText(_translate("MainWindow", "Insert Premise", None))
        self.actionInsert_Premise.setToolTip(_translate("MainWindow", "Insert Premise Line", None))
        self.actionInsert_Premise.setShortcut(_translate("MainWindow", "Ctrl+A", None))
        self.actionInsert_Conclusion.setText(_translate("MainWindow", "Insert Conclusion", None))
        self.actionInsert_Conclusion.setToolTip(_translate("MainWindow", "Insert Conclusion Line", None))
        self.actionInsert_Conclusion.setShortcut(_translate("MainWindow", "Ctrl+G", None))
        self.actionRun.setText(_translate("MainWindow", "Run", None))
        self.actionRun.setToolTip(_translate("MainWindow", "Creates the Davis-Putnam Tree", None))
        self.actionRun.setShortcut(_translate("MainWindow", "Ctrl+R", None))

