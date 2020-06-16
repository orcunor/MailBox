from PyQt5.QtWidgets import *
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib,ssl


class Ana_Pencere(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.pencere1 = QWidget()
        self.pencere1_tasarım()
        self.setCentralWidget(self.pencere1)
        self.show()


    def pencere1_tasarım(self):

        form = QFormLayout()
        self.kullanici_mail = QLineEdit()
        form.addRow(QLabel("Mail Adresiniz:"),self.kullanici_mail)

        self.kullanici_sifre = QLineEdit()
        self.kullanici_sifre.setEchoMode(QLineEdit.Password)
        form.addRow(QLabel("Şifreniz"),self.kullanici_sifre)

        self.gonderilen_mail = QLineEdit()
        form.addRow(QLabel("Kime:"),self.gonderilen_mail)

        self.konu = QLineEdit()
        form.addRow(QLabel("Konu:"),self.konu)

        self.ileti = QTextEdit()
        form.addRow(QLabel("İleti:"),self.ileti)

        self.gonder = QPushButton("Gönder")
        self.gonder.clicked.connect(self.gonder_clk)
        form.addWidget(self.gonder)



        self.pencere1.setLayout(form)

    
    def gonder_clk(self):
        mesaj = MIMEMultipart()
        mesaj["From"] = self.kullanici_mail.text()
        mesaj["To"] = self.gonderilen_mail.text()
        mesaj["Subject"] = self.konu.text()

        yazi = self.ileti.toPlainText()

        mesaj_govdesi = MIMEText(yazi,"plain")
        mesaj.attach(mesaj_govdesi)

        try:
            mail = smtplib.SMTP("smtp.gmail.com",587)
            mail.ehlo()
            mail.starttls()
            mail.login(self.kullanici_mail.text(),self.kullanici_sifre.text())
            mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
            print("{} adresine mailiniz başarıyla gönderildi..".format(self.gonderilen_mail))
            mail.close()


        except:
            print("Mail Gönderilemedi.")








app = QApplication(sys.argv)
ana_pencere = Ana_Pencere()
sys.exit(app.exec_())
