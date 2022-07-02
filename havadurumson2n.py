# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\havadurumu.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget

from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

from PyQt5.QtWidgets import QFileDialog

# import Opencv module
import cv2
import datetime
import time
import numpy as np
import os


import random
import time
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS
import pyaudio
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from datetime import datetime


r=sr.Recognizer()
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1082, 685)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 0, 521, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_dosyasec = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dosyasec.setGeometry(QtCore.QRect(140, 550, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_dosyasec.setFont(font)
        self.btn_dosyasec.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.btn_dosyasec.setObjectName("btn_dosyasec")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 80, 491, 411))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_yolo = QtWidgets.QLabel(self.groupBox)
        self.label_yolo.setGeometry(QtCore.QRect(20, 20, 461, 381))
        self.label_yolo.setText("")
        self.label_yolo.setObjectName("label_yolo")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(540, 80, 511, 411))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 20, 491, 101))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 160, 491, 241))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.bbtn_siriac = QtWidgets.QPushButton(self.centralwidget)
        self.bbtn_siriac.setGeometry(QtCore.QRect(690, 550, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bbtn_siriac.setFont(font)
        self.bbtn_siriac.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.bbtn_siriac.setObjectName("bbtn_siriac")
        self.bbtn_siriac_2 = QtWidgets.QPushButton(self.centralwidget)
        self.bbtn_siriac_2.setGeometry(QtCore.QRect(410, 550, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bbtn_siriac_2.setFont(font)
        self.bbtn_siriac_2.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.bbtn_siriac_2.setObjectName("bbtn_siriac_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1082, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "WEATHER FORECAST "))
        self.btn_dosyasec.setText(_translate("MainWindow", "SELECT FİLE"))
        self.groupBox.setTitle(_translate("MainWindow", "YOLO PREDİCTİON"))
        self.groupBox_2.setTitle(_translate("MainWindow", "REAL WEATHER"))
        self.bbtn_siriac.setText(_translate("MainWindow", "SIRI OPEN"))
        self.bbtn_siriac_2.setText(_translate("MainWindow", "WEATHER FORECAST KONYA"))
        self.bbtn_siriac_2.clicked.connect(self.yazdir)
        self.bbtn_siriac.clicked.connect(self.asistan)
        self.btn_dosyasec.clicked.connect( self.image)


    def image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        fileName, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        # img = cv2.imread("C:\\YOLO\\yolo_rainy\\rainy3.jpg")  # BGR hali
        img = cv2.imread(fileName)
        img = cv2.resize(img, (640, 420))
        print(img.shape[0:2])
        img_widht = img.shape[1]  # enini aldım
        img_height = img.shape[0]  # boyunu aldım

        img_blob = cv2.dnn.blobFromImage(img, 1 / 255, (416, 416), swapRB=True,
                                         crop=False)  # yolo algoritmasını kullanmak icin resimi blob formata ceviriyorum
        # resmim, scalefactor yolo yazarları bunun dogru degeri 1/255 olarak bulmus, egitimim 413,413 resimler yani kullndiğim model, resmimi BGR dan RGB'ye ceviriyorum.
        # ,crop=false resmim kırpılmasın

        labels = ["Rainy", "Sunny", "Cloudy"]

        colors = ["0,255,255", "0,0,255", "255,0,0", "255,255,0", "255,255,255", "0,255,0"]
        colors = [np.array(color.split(",")).astype("int") for color in colors]
        colors = np.array(colors)
        colors = np.tile(colors, (18, 1))  # 5 kere 1 kez yan yana ekleme tail cogaltma isleminde kullanıllıyor
        #        #%% 3.Bölüm  ile kodu bölümlere ayırabiliyoruz
        # model=cv2.dnn.readNetFromDarknet("C:\YOLO\yolo_weather\yolov4.cfg","C:\YOLO\yolo_weather\yolov4_2000.weights")
        model = cv2.dnn.readNetFromDarknet("C:\YOLO\yolo_weather\weather2\yolov4.cfg",
                                           "C:\YOLO\yolo_weather\weather2\yolov4_2000.weights")

        # model = cv2.dnn.readNetFromDarknet("C:/YOLO/pretrained_model/yolov3.cfg", "C:/YOLO/pretrained_model/yolov3.weights")
        layers = model.getLayerNames()  # layers degisşkenine modeldeki layers atadım
        output_layer = [layers[layer[0] - 1] for layer in
                        model.getUnconnectedOutLayers()]  # Layers hespsine ihtiyacım yok sadece cıktıları alacagım
        # model.getUnconnectedOutLayers() ->  array([200, 227, 254]) bu degrelerin 1 eksiginde yolo cıktım katmanım var

        model.setInput(img_blob)

        detection_layers = model.forward(
            output_layer)  # cıktı katmanımdaki (output_layer) bir takım degerlere erişiyorum

        ############################ Non Maximim Suppression  Oeration-1 ###########################☺
        ids_list = []
        bocces_list = []
        confidences_list = []

        ############################ END OF Non Maximim Suppression  Oeration-1 ###########################☺

        for detection_layer in detection_layers:
            for object_detection in detection_layer:
                scores = object_detection[5:]
                predicted_id = np.argmax(scores)  # maksimum degerdeki ndeksi veriyor
                confidence = scores[predicted_id]
                print(confidence)
                if confidence > 0:
                    label = labels[predicted_id]
                    bounding_box = object_detection[0:4] * np.array([img_widht, img_height, img_widht, img_height])
                    (box_center_x, box_center_y, box_width, box_height) = bounding_box.astype(
                        "int")  # float degerlerle calısamıyorum int olması gerekiyor

                    start_x = int(box_center_x - (box_width / 2))
                    start_y = int(box_center_y - (box_height / 2))
                    ############################ Non Maximim Suppression  Oeration-2 ###########################☺
                    ids_list.append(predicted_id)
                    confidences_list.append(float(confidence))
                    bocces_list.append([start_x, start_y, int(box_width), int(box_height)])

                    ############################ END OF Non Maximim Suppression  Oeration-2 ###########################☺

        ############################ Non Maximim Suppression  Oeration-3 ###########################☺
        max_ids = cv2.dnn.NMSBoxes(bocces_list, confidences_list, 0,
                                   0)  # ♥makimium boudibox bir array içinde veriyor. önerilen thrashold degeri 0.5,0.4

        for max_id in max_ids:
            max_class_id = max_id[0]
            box = bocces_list[max_class_id]

            start_x = box[0]
            start_y = box[1]
            box_width = box[2]
            box_height = box[3]

            predicted_id = ids_list[max_class_id]
            label = labels[predicted_id]
            confidence = confidences_list[max_class_id]

            ############################ END OF Non Maximim Suppression  Oeration-3 ###########################☺

            end_x = start_x + box_width
            end_y = start_y + box_height

            box_color = colors[predicted_id]
            box_color = [int(each) for each in box_color]

            labelx = "{}:{:.2f}%".format(label, confidence * 100)

            print("predicted object {}".format(labelx))

            # cv2.rectangle(img, (start_x, start_y),(end_x,end_y),box_color,1)
            cv2.putText(img, labelx, (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, box_color, 2)



        frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # get image infos
        height, width, channel = frame.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(frame.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.label_yolo.setPixmap(QPixmap.fromImage(qImg))



    def asistan(self):
        class SesliAsistan():


            def seslendirme(self, metin):
                xtts = gTTS(text=metin, lang="tr")
                dosya = "dosya" + str(random.randint(0, 1242312412312)) + ".mp3"
                xtts.save(dosya)
                playsound(dosya)
                # os.remove("C:/Users/apoba/Desktop/PythonProje/dosya")

            def ses_kayit(self):

                with sr.Microphone() as kaynak:
                    print("Sizi dinliyoruz...")

                    listen = r.listen(kaynak)
                    voice = " "

                    try:
                        voice = r.recognize_google(listen, language="tr-TR")

                    except sr.UnknownValueError:
                        self.seslendirme("Ne söylediğinizi anlayamadım.Lutfen tekrar ediniz")
                    print("1" + voice)
                    return voice

            def ses_karsilik(self, gelen_ses):
                if "selam" in gelen_ses:
                    self.seslendirme("Size de selamlar")



                elif "hava durumu" in gelen_ses or "hava durumu tahmini" in gelen_ses:

                    try:
                        self.seslendirme("hangi şehrin hava durumunu istersiniz")
                        cevap = self.ses_kayit()
                        url = "https://www.ntvhava.com/{}-hava-durumu".format(cevap)
                        request = requests.get(url)
                        html_icerigi = request.content
                        soup = BeautifulSoup(html_icerigi, "html.parser")
                        gunduz_sicakliklari = soup.find_all("div",
                                                            {
                                                                "class": "daily-report-tab-content-pane-item-box-bottom-degree-big"})
                        gece_sicakliklari = soup.find_all("div",
                                                          {
                                                              "class": "daily-report-tab-content-pane-item-box-bottom-degree-small"})
                        hava_durumları = soup.find_all("div", {"class": "daily-report-tab-content-pane-item-text"})

                        gun_isimleri = soup.find_all("div", {"class": "daily-report-tab-content-pane-item-date"})

                        gunduz = []
                        gece = []
                        hava = []
                        gunler = []

                        for x in gunduz_sicakliklari:
                            x = x.text
                            gunduz.append(x)
                        for y in gece_sicakliklari:
                            y = y.text
                            gece.append(y)
                        for z in hava_durumları:
                            z = z.text
                            hava.append(z)

                        for a in gun_isimleri:
                            a = a.text
                            a = a[0:3:]
                            if (a == "Cmt"):
                                a = "Cumartesi"
                            elif (a == "Paz"):
                                a = "Pazar"
                            elif (a == "Pzt"):
                                a = "Pazartesi"
                            elif (a == "Sal"):
                                a = "Salı"
                            elif (a == "Çar"):
                                a = "Çarşamba"
                            elif (a == "Per"):
                                a = "Perşembe"
                            elif (a == "Cum"):
                                a = "Cuma"
                            gunler.append(a)

                        self.seslendirme(
                            "{} şehiri için günlük , yarının ya da 5 günlük hava raporlarını mı istersiniz".format(
                                cevap))
                        cevap2 = self.ses_kayit()

                        if (cevap2 == "bugünün" or cevap2 == "günlük"):
                            saat = datetime.now().strftime("%H:%M")
                            if (saat <= "17:00"):
                                self.seslendirme(
                                    "{} için hava durumu bugün şöyle: {} gündüz sıcaklığı: {} gece sıcaklığı: {}".format(
                                        cevap, hava[0], gunduz[0], gece[0]))
                            else:
                                self.seslendirme(
                                    "{} için hava durumu bu akşam şöyle: {} gece sıcaklığı :{}".format(cevap, hava[0],
                                                                                                       gece[0]))

                        elif (cevap2 == "yarın" or cevap2 == "yarınınki" or cevap2 == "ertesi günün"):
                            self.seslendirme(
                                "{} için yarın hava durumu şöyle: {} gündüz sıcaklığı: {} gece sıcaklığı: {}".format(
                                    cevap, hava[1], gunduz[1], gece[1]))

                        elif (cevap2 == "beş günlük" or cevap2 == "haftalık"):
                            saat = datetime.now().strftime("%H:%M")
                            if (saat <= "17:00"):
                                self.seslendirme(
                                    "{} için hava durumu bugün şöyle: {} gündüz sıcaklığı {} gece sıcaklığı: {}"
                                    "yarın {} gündüz sıcaklığı: {} gece sıcaklığı: {}"
                                    "{} {} gündüz sıcaklığı: {} gece sıcaklığı: {}"
                                    "{} {} gündüz sıcaklığı: {} gece sıcaklığı: {}"
                                    "{} {} gündüz sıcaklığı: {} gece sıcaklığı: {}".format(cevap, hava[0], gunduz[0],
                                                                                           gece[0], hava[1], gunduz[1],
                                                                                           gece[1], gunler[2], hava[2],
                                                                                           gunduz[2], gece[2],
                                                                                           gunler[3], hava[3],
                                                                                           gunduz[3], gece[3],
                                                                                           gunler[4], hava[4],
                                                                                           gunduz[4], gece[4]))

                            else:
                                self.seslendirme("{} için hava durumu bugün şöyle: {} gece sıcaklığı: {}"
                                                 "yarın {} gündüz sıcaklığı: {} gece sıcaklığı: {}"
                                                 "{} {} gündüz sıcaklığı: {} gece sıcaklığı: {}"
                                                 "{} {} gündüz sıcaklığı: {} gece sıcaklığı: {}"
                                                 "{} {} gündüz sıcaklığı: {} gece sıcaklığı: {}".format(cevap, hava[0],
                                                                                                        gece[0],
                                                                                                        hava[1],
                                                                                                        gunduz[1],
                                                                                                        gece[1],
                                                                                                        gunler[2],
                                                                                                        hava[2],
                                                                                                        gunduz[2],
                                                                                                        gece[2],
                                                                                                        gunler[3],
                                                                                                        hava[3],
                                                                                                        gunduz[3],
                                                                                                        gece[3],
                                                                                                        gunler[4],
                                                                                                        hava[4],
                                                                                                        gunduz[4],
                                                                                                        gece[4]))
                    except:
                        self.seslendirme(
                            "istediğinz şehre göre bir içerik bulunamadı.lütfen istediğinz şehri veya internetinizi kontrol ediniz")

        asistan = SesliAsistan()

        def uyanma_fonksiyonu(metin):
            if (metin == "hey siri" or metin == "siri"):
                asistan.seslendirme("dinliyorum...")
                cevap = asistan.ses_kayit()
                if (cevap != ""):
                    asistan.ses_karsilik(cevap)

        while True:
            ses = asistan.ses_kayit()
            if (ses != " "):
                ses = ses.lower()

                print(ses)
                uyanma_fonksiyonu(ses)

    def yazdir(self):
        url = "https://www.ntvhava.com/konya-hava-durumu"
        request = requests.get(url)
        html_içeriği = request.content
        soup = BeautifulSoup(html_içeriği, "html.parser")
        gunduz_sicakliklari = soup.find_all("div",
                                            {"class": "daily-report-tab-content-pane-item-box-bottom-degree-big"})
        hava_durumları = soup.find_all("div", {"class", "daily-report-tab-content-pane-item-text"})
        gunduz = []
        havadurumu = []
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)


        for x in gunduz_sicakliklari:
            x = x.text
            gunduz.append(x)
        self.plainTextEdit.appendPlainText(gunduz[1])
        for y in hava_durumları:
            y = y.text
            havadurumu.append(y)
        self.plainTextEdit.appendPlainText("                                             "+havadurumu[1])
        img2 = cv2.imread("C:\\YOLO\\yolo_rainy\\resimler_havadurumu_iconarayuz\\indir.png")
        img2 = cv2.resize(img2, (491, 241))
        frame = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

        # get image infos
        height, width, channel = frame.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(frame.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.label_2.setPixmap(QPixmap.fromImage(qImg))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

