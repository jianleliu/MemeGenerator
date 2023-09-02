import random
from requests import get
import json
from urllib import request
from PyQt5 import QtCore, QtGui, QtWidgets
from time import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(254, 279)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.formLayout = QtWidgets.QFormLayout(self.page)
        self.formLayout.setObjectName("formLayout")

        self.label_sort = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_sort.setFont(font)
        self.label_sort.setAutoFillBackground(False)
        self.label_sort.setObjectName("label_sort")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_sort)

        self.combox_sort = QtWidgets.QComboBox(self.page)
        self.combox_sort.setObjectName("combox_sort")
        self.combox_sort.addItem("")
        self.combox_sort.addItem("")
        self.combox_sort.addItem("")
        self.combox_sort.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.combox_sort)

        self.label_within = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_within.setFont(font)
        self.label_within.setAutoFillBackground(False)
        self.label_within.setObjectName("label_within")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_within)

        self.combox_within = QtWidgets.QComboBox(self.page)
        self.combox_within.setObjectName("combox_within")
        self.combox_within.addItem("")
        self.combox_within.addItem("")
        self.combox_within.addItem("")
        self.combox_within.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.combox_within)

        """
        self.label_generate = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_generate.setFont(font)
        self.label_generate.setAutoFillBackground(False)
        self.label_generate.setObjectName("label_generate")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_generate)
        self.combox_generate = QtWidgets.QComboBox(self.page)
        self.combox_generate.setObjectName("combox_generate")
        self.combox_generate.addItem("")
        self.combox_generate.addItem("")
        self.combox_generate.addItem("")
        self.combox_generate.addItem("")
        self.combox_generate.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.combox_generate)
        """

        self.label_repeat = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_repeat.setFont(font)
        self.label_repeat.setAutoFillBackground(False)
        self.label_repeat.setObjectName("label_repeat")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_repeat)

        self.rabtn_true = QtWidgets.QRadioButton(self.page)
        self.rabtn_true.setObjectName("rabtn_true")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.rabtn_true)
        self.label = QtWidgets.QLabel(self.page)
        self.label.setText("")
        self.label.setObjectName("label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label)

        self.rabtn_false = QtWidgets.QRadioButton(self.page)
        self.rabtn_false.setObjectName("rabtn_false")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.rabtn_false)

        self.btn_generate = QtWidgets.QPushButton(self.page)
        self.btn_generate.setObjectName("Generate")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_generate.sizePolicy().hasHeightForWidth())
        self.btn_generate.setSizePolicy(sizePolicy)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.btn_generate)
        self.btn_generate.setText("Generate")

        self.label_settings = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_settings.sizePolicy().hasHeightForWidth())
        self.label_settings.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_settings.setFont(font)
        self.label_settings.setAutoFillBackground(False)
        self.label_settings.setObjectName("label_settings")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_settings)
        

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_display = QtWidgets.QLabel(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_display.sizePolicy().hasHeightForWidth())
        self.label_display.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_display.setFont(font)
        self.label_display.setAutoFillBackground(False)
        self.label_display.setObjectName("label_display")
        self.verticalLayout.addWidget(self.label_display)

        self.label_image = QtWidgets.QLabel(self.page_2)
        self.label_image.setObjectName("label_image")
        self.verticalLayout.addWidget(self.label_image)

        self.btn_download = QtWidgets.QPushButton(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_download.sizePolicy().hasHeightForWidth())
        self.btn_download.setSizePolicy(sizePolicy)
        self.btn_download.setObjectName("btn_download")
        self.verticalLayout.addWidget(self.btn_download)

        self.btn_next_img = QtWidgets.QPushButton(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_next_img.sizePolicy().hasHeightForWidth())
        self.btn_next_img.setSizePolicy(sizePolicy)
        self.btn_next_img.setObjectName("btn_next_img")
        self.verticalLayout.addWidget(self.btn_next_img)

        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.btn_settings = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy)
        self.btn_settings.setObjectName("btn_settings")
        self.horizontalLayout.addWidget(self.btn_settings)

        self.btn_display = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_display.sizePolicy().hasHeightForWidth())
        self.btn_display.setSizePolicy(sizePolicy)
        self.btn_display.setObjectName("btn_display")
        self.horizontalLayout.addWidget(self.btn_display)
        self.verticalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.qmap = QtGui.QPixmap()

        #events
        self.btn_settings.clicked.connect(lambda : self.event_btn_settings())
        self.btn_display.clicked.connect(lambda : self.event_btn_display())
        self.btn_download.clicked.connect(lambda : self.event_btn_download())
        self.btn_next_img.clicked.connect(lambda : self.event_btn_next_img(MainWindow))
        self.btn_generate.clicked.connect(lambda : self.event_btn_generate())

        
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.label_sort.setText(_translate("MainWindow", "Sort By:"))

        self.combox_sort.setItemText(0, _translate("MainWindow", "top"))
        self.combox_sort.setItemText(1, _translate("MainWindow", "hot"))
        self.combox_sort.setItemText(2, _translate("MainWindow", "new"))
        self.combox_sort.setItemText(3, _translate("MainWindow", "rising"))

        self.label_within.setText(_translate("MainWindow", "Within:"))

        self.combox_within.setItemText(0, _translate("MainWindow", "hour"))
        self.combox_within.setItemText(1, _translate("MainWindow", "week"))
        self.combox_within.setItemText(2, _translate("MainWindow", "year"))
        self.combox_within.setItemText(3, _translate("MainWindow", "all"))
        """
        self.label_generate.setText(_translate("MainWindow", "Generate out of:"))

        self.combox_generate.setItemText(0, _translate("MainWindow", "20"))
        self.combox_generate.setItemText(1, _translate("MainWindow", "40"))
        self.combox_generate.setItemText(2, _translate("MainWindow", "60"))
        self.combox_generate.setItemText(3, _translate("MainWindow", "80"))
        self.combox_generate.setItemText(4, _translate("MainWindow", "100"))
        """
        self.label_repeat.setText(_translate("MainWindow", "Repeat:"))

        self.rabtn_true.setText(_translate("MainWindow", "True"))
        self.rabtn_false.setText(_translate("MainWindow", "False"))
        self.rabtn_false.setChecked(True)

        self.label_settings.setText(_translate("MainWindow", "Settings Page"))

        self.label_display.setText(_translate("MainWindow", "Display Page"))

        self.label_image.setText(_translate("MainWindow", "TextLabel"))

        self.btn_download.setText(_translate("MainWindow", "Download"))

        self.btn_next_img.setText(_translate("MainWindow", "Next Image"))

        self.btn_settings.setText(_translate("MainWindow", "Settings"))

        self.btn_display.setText(_translate("MainWindow", "Display"))

        self.btn_display.setEnabled(False)


    #-------------------------------------------------Codes Below-----------------------------------------------
    def __init__(self):
        #check if setting json file exists
        self.list_urls = []
        self.repeat = False
        self.img_count = 1
        self.image_url = None
        self.after = None #stores a code for dynamic pagination
        self.timestamp_1 = None
        self.timestamp_2 = None

    def event_btn_download(self):
        request.urlretrieve(self.image_url, "img" + str(self.img_count) + ".jpg")
        self.img_count += 1

    def event_btn_next_img(self, MainWindow):
        if not self.list_urls:
            self.label_image.setText("No image found(generated).")
            return
        random_index = random.randrange(0, len(self.list_urls))
        self.displayImage(self.list_urls[random.randrange(0, len(self.list_urls))], MainWindow)
        if self.rabtn_false.isChecked():
            self.list_urls.pop(random_index)

    def event_btn_settings(self):
        self.timestamp_2 = int(time())
        if self.timestamp_1:
            if (self.timestamp_2 - self.timestamp_1) > 180:#cool down to avoid spamming
                self.btn_generate.setEnabled(True)
        self.stackedWidget.setCurrentIndex(0)

    def event_btn_display(self):
        self.stackedWidget.setCurrentIndex(1)

    def event_btn_generate(self):
        self.parseJson(self.getJson())
        self.timestamp_1 = int(time())
        self.btn_generate.setEnabled(False)
        self.btn_display.setEnabled(True)

    #display image n pixmap
    #resize mainwindow
    def displayImage(self, url, MainWindow):
        self.image_url = url
        image_data = request.urlopen(url).read()
        self.qmap.loadFromData(image_data)
        self.label_image.setPixmap(self.qmap)
        window_width, window_height = MainWindow.geometry().width(), MainWindow.geometry().width()
        self.label_image.resize(window_width, window_height - 148)
    
    #request a web and retrieve the json file
    def getJson(self):
        param = None
        if self.after: 
            param = {
                    "after": self.after, #stores a code for dynamic pagination
                    "t": self.combox_within.currentText(),
                    "sort": self.combox_sort.currentText(),
                }
        else:
            param = {
                    "t": self.combox_within.currentText(),
                    "sort": self.combox_sort.currentText(),
                }
        source = get("https://gateway.reddit.com/desktopapi/v1/subreddits/memes", params=param).json()
        return source
    
    #parse json and get the urls
    #save the urls into a list
    #return the id for after(dynamic pagination)
    def parseJson(self, source):
        dict_source = {}
        dict_source = json.loads(json.dumps(source))
        with open("temp.json","w") as f:
            f.write(json.dumps(dict_source))
        if not dict_source.get("code"):
            for id in dict_source["posts"].keys():
                self.list_urls.append(dict_source["posts"][id]["thumbnail"]["url"])
            return dict_source["postIds"][-1]
        else:
            print("An error has occuried")
            print("code", dict_source["code"])
            print("reason: ", dict_source["reason"])
            print("explanation: ", dict_source["explanation"])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
