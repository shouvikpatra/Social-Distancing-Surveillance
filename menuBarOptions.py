from PyQt5 import QtCore, QtGui, QtWidgets

def getCameraWidgetIndices(index):
    rowIndex = index // 2
    columnIndex = index % 2
    columnIndexAttr = QtWidgets.QFormLayout.LabelRole if columnIndex == 0 else QtWidgets.QFormLayout.FieldRole
    return (rowIndex, columnIndexAttr)


class NewDialog(object):
    def setupUi(self, Dialog, layout = None):
        Dialog.setObjectName("Dialog")
        Dialog.resize(825, 227)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.addDescription = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addDescription.sizePolicy().hasHeightForWidth())
        self.addDescription.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.addDescription.setFont(font)
        self.addDescription.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.addDescription.setObjectName("addDescription")
        self.verticalLayout.addWidget(self.addDescription)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tagValue = QtWidgets.QLineEdit(Dialog)
        self.tagValue.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tagValue.setFont(font)
        self.tagValue.setText("")
        self.tagValue.setObjectName("tagValue")
        self.gridLayout.addWidget(self.tagValue, 0, 3, 1, 1)
        self.ipLabel = QtWidgets.QLabel(Dialog)
        self.ipLabel.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ipLabel.setFont(font)
        self.ipLabel.setObjectName("ipLabel")
        self.gridLayout.addWidget(self.ipLabel, 2, 0, 1, 1)
        self.idValue = QtWidgets.QLineEdit(Dialog)
        self.idValue.setReadOnly(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.idValue.sizePolicy().hasHeightForWidth())
        self.idValue.setSizePolicy(sizePolicy)
        self.idValue.setMinimumSize(QtCore.QSize(100, 40))
        self.idValue.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.idValue.setFont(font)
        self.idValue.setText(str(layout.count()))
        self.idValue.setObjectName("idValue")
        self.gridLayout.addWidget(self.idValue, 0, 1, 1, 1)
        self.idLabel = QtWidgets.QLabel(Dialog)
        self.idLabel.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.idLabel.setFont(font)
        self.idLabel.setObjectName("idLabel")
        self.gridLayout.addWidget(self.idLabel, 0, 0, 1, 1)
        self.tagLabel = QtWidgets.QLabel(Dialog)
        self.tagLabel.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tagLabel.setFont(font)
        self.tagLabel.setObjectName("tagLabel")
        self.gridLayout.addWidget(self.tagLabel, 0, 2, 1, 1)
        self.ipValue = QtWidgets.QLineEdit(Dialog)
        self.ipValue.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ipValue.setFont(font)
        self.ipValue.setText("")
        self.ipValue.setObjectName("ipValue")
        self.gridLayout.addWidget(self.ipValue, 2, 1, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)
        self.addButtonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.addButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.addButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Yes)
        self.addButtonBox.setCenterButtons(True)
        self.addButtonBox.setObjectName("addButtonBox")
        self.verticalLayout.addWidget(self.addButtonBox)

        self.retranslateUi(Dialog)
        self.addButtonBox.accepted.connect(Dialog.accept)
        self.addButtonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.makeCamBool = False
        self.addButtonBox.accepted.connect(lambda: self.makeCameraYes())
        self.addButtonBox.rejected.connect(lambda: self.makeCameraNo())
    
    def makeCameraYes(self):
        self.makeCamBool = True
    
    def makeCameraNo(self):
        self.makeCamBool = False

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.addDescription.setText(_translate("Dialog", "Enter the following information of the new camera you want to add:"))
        self.ipLabel.setText(_translate("Dialog", "CAMERA IP: "))
        self.idLabel.setText(_translate("Dialog", "CAMERA ID: "))
        self.tagLabel.setText(_translate("Dialog", "CAMERA TAG: "))


class EditDialog(object):
    def setupUi(self, Dialog, layout = None):
        Dialog.setObjectName("Dialog")
        Dialog.resize(885, 265)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.editDescription = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editDescription.sizePolicy().hasHeightForWidth())
        self.editDescription.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.editDescription.setFont(font)
        self.editDescription.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.editDescription.setObjectName("editDescription")
        self.verticalLayout.addWidget(self.editDescription)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.ipLabel = QtWidgets.QLabel(Dialog)
        self.ipLabel.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ipLabel.setFont(font)
        self.ipLabel.setObjectName("ipLabel")
        self.gridLayout.addWidget(self.ipLabel, 2, 0, 1, 1)
        self.idValues = QtWidgets.QComboBox(Dialog)
        self.idValues.setMinimumSize(QtCore.QSize(0, 40))
        self.idValues.setEditable(False)
        self.idValues.setIconSize(QtCore.QSize(20, 20))
        self.idValues.setObjectName("idValues")
        for i in range(layout.count()):
            self.idValues.addItem(str(i))
        self.gridLayout.addWidget(self.idValues, 0, 1, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.idValues.setFont(font)
        self.tagValue = QtWidgets.QLineEdit(Dialog)
        self.tagValue.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tagValue.setFont(font)
        self.tagValue.setText("")
        self.tagValue.setObjectName("tagValue")
        self.gridLayout.addWidget(self.tagValue, 0, 3, 1, 1)
        self.ipValue = QtWidgets.QLineEdit(Dialog)
        self.ipValue.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ipValue.setFont(font)
        self.ipValue.setText("")
        self.ipValue.setObjectName("ipValue")
        self.gridLayout.addWidget(self.ipValue, 2, 1, 1, 3)
        self.tagLabel = QtWidgets.QLabel(Dialog)
        self.tagLabel.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tagLabel.setFont(font)
        self.tagLabel.setObjectName("tagLabel")
        self.gridLayout.addWidget(self.tagLabel, 0, 2, 1, 1)
        self.idLabel = QtWidgets.QLabel(Dialog)
        self.idLabel.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.idLabel.setFont(font)
        self.idLabel.setObjectName("idLabel")
        self.gridLayout.addWidget(self.idLabel, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.editButtonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.editButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.editButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.editButtonBox.setCenterButtons(True)
        self.editButtonBox.setObjectName("editButtonBox")
        self.verticalLayout.addWidget(self.editButtonBox)

        self.retranslateUi(Dialog)
        self.editButtonBox.accepted.connect(Dialog.accept)
        self.editButtonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.selectIdCam(self.idValues.currentIndex(), layout)


        self.editCamBool = False
        self.editButtonBox.accepted.connect(lambda: self.editCameraYes())
        self.editButtonBox.rejected.connect(lambda: self.editCameraNo())
        self.idValues.activated.connect(lambda: self.selectIdCam(self.idValues.currentIndex(), layout))

    def editCameraYes(self):
        self.editCamBool = True
    
    def editCameraNo(self):
        self.editCamBool = False

    def selectIdCam(self, selected, layout = None):
        i,j = getCameraWidgetIndices(int(selected))
        widget = layout.itemAt(i, j).widget()
        self.tagValue.setText(str(widget.camera_tag))
        self.ipValue.setText(str(widget.camera_ip))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.editDescription.setText(_translate("Dialog", "Please select a camera to edit and enter the new values:"))
        self.ipLabel.setText(_translate("Dialog", "CAMERA IP: "))
        self.tagLabel.setText(_translate("Dialog", "CAMERA TAG: "))
        self.idLabel.setText(_translate("Dialog", "CAMERA ID: "))


class RemoveDialog(object):
    def setupUi(self, Dialog, layout = None):
        Dialog.setObjectName("Dialog")
        Dialog.resize(885, 265)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.removeDescription = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeDescription.sizePolicy().hasHeightForWidth())
        self.removeDescription.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.removeDescription.setFont(font)
        self.removeDescription.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.removeDescription.setObjectName("removeDescription")
        self.verticalLayout.addWidget(self.removeDescription)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.ipValue = QtWidgets.QLineEdit(Dialog)
        self.ipValue.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ipValue.setFont(font)
        self.ipValue.setText("")
        self.ipValue.setReadOnly(True)
        self.ipValue.setObjectName("ipValue")
        self.gridLayout.addWidget(self.ipValue, 2, 1, 1, 3)
        self.idValues = QtWidgets.QComboBox(Dialog)
        self.idValues.setMinimumSize(QtCore.QSize(65, 40))
        for i in range(layout.count()):
            self.idValues.addItem(str(i))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.idValues.setFont(font)
        self.idValues.setEditable(False)
        self.idValues.setIconSize(QtCore.QSize(20, 20))
        self.idValues.setObjectName("idValues")
        self.gridLayout.addWidget(self.idValues, 0, 1, 1, 1)
        self.ipLabel = QtWidgets.QLabel(Dialog)
        self.ipLabel.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ipLabel.setFont(font)
        self.ipLabel.setObjectName("ipLabel")
        self.gridLayout.addWidget(self.ipLabel, 2, 0, 1, 1)
        self.tagLabel = QtWidgets.QLabel(Dialog)
        self.tagLabel.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tagLabel.setFont(font)
        self.tagLabel.setObjectName("tagLabel")
        self.gridLayout.addWidget(self.tagLabel, 0, 2, 1, 1)
        self.idLabel = QtWidgets.QLabel(Dialog)
        self.idLabel.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.idLabel.setFont(font)
        self.idLabel.setObjectName("idLabel")
        self.gridLayout.addWidget(self.idLabel, 0, 0, 1, 1)
        self.tagValue = QtWidgets.QLineEdit(Dialog)
        self.tagValue.setEnabled(True)
        self.tagValue.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tagValue.setFont(font)
        self.tagValue.setText("")
        self.tagValue.setReadOnly(True)
        self.tagValue.setObjectName("tagValue")
        self.gridLayout.addWidget(self.tagValue, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.removeButtonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.removeButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.removeButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.removeButtonBox.setCenterButtons(True)
        self.removeButtonBox.setObjectName("removeButtonBox")
        self.verticalLayout.addWidget(self.removeButtonBox)

        self.retranslateUi(Dialog)
        self.removeButtonBox.accepted.connect(Dialog.accept)
        self.removeButtonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.selectIdCam(self.idValues.currentIndex(), layout)

        self.removeCamBool = False
        self.removeButtonBox.accepted.connect(lambda: self.removeCameraYes())
        self.removeButtonBox.rejected.connect(lambda: self.removeCameraNo())
        self.idValues.activated.connect(lambda: self.selectIdCam(self.idValues.currentIndex(), layout))
    
    def removeCameraYes(self):
        self.removeCamBool = True
    
    def removeCameraNo(self):
        self.removeCamBool = False

    def selectIdCam(self, selected, layout = None):
        i,j = getCameraWidgetIndices(int(selected))
        widget = layout.itemAt(i, j).widget()
        self.tagValue.setText(str(widget.camera_tag))
        self.ipValue.setText(str(widget.camera_ip))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.removeDescription.setText(_translate("Dialog", "Please select a camera to remove:"))
        self.ipLabel.setText(_translate("Dialog", "CAMERA IP: "))
        self.tagLabel.setText(_translate("Dialog", "CAMERA TAG: "))
        self.idLabel.setText(_translate("Dialog", "CAMERA ID: "))

