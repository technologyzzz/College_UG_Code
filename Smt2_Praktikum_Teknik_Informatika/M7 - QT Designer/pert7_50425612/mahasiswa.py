import sys
from PyQt5 import QtWidgets, uic
import conndb

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("Mahasiswa.ui", self)
        self.setWindowTitle("MAHASISWA")
        #self.pushButton.clicked.connect(self.loadData)
        self.pushButtonSimpan.clicked.connect(self.createData)
        self.pushButtonUpdate.clicked.connect(self.updateData)
        self.pushButtonDelete.clicked.connect(self.deleteData)
        self.tableWidget.clicked.connect(self.getData)
        self.tableWidget.setColumnWidth(0, 220)
        self.tableWidget.setColumnWidth(3, 220)
        pass
    
    def getData(self):
        row = self.tableWidget.currentRow()
        print(str(row))
        rowItemNama = self.tableWidget.item(row, 0).text()
        rowItemNpm = self.tableWidget.item(row, 1).text()
        rowItemKelas = self.tableWidget.item(row, 2).text()
        rowItemJurusan = self.tableWidget.item(row, 3).text()

        self.lineEdit_nama.setText(rowItemNama)
        self.lineEdit_npm.setText(rowItemNpm)
        self.lineEdit_kelas.setText(rowItemKelas)
        self.lineEdit_jurusan.setText(rowItemJurusan)

    def createData(self):
        nama = self.lineEdit_nama.text()
        npm = self.lineEdit_npm.text()
        kelas = self.lineEdit_kelas.text()
        jurusan = self.lineEdit_jurusan.text()
        strsql = "INSERT INTO tbl_mahasiswa VALUES ('"+nama+"', '"+npm+"', '"+kelas+"', '"+jurusan+"')"
        conn = conndb.conndb()
        conn.queryExecute(strsql)
        self.loadData()

    def updateData(self):
        nama = self.lineEdit_nama.text()
        npm = self.lineEdit_npm.text()
        kelas = self.lineEdit_kelas.text()
        jurusan = self.lineEdit_jurusan.text()
        strsql = "UPDATE tbl_mahasiswa SET npm='"+npm+"', kelas='"+kelas+"', jurusan='"+jurusan+"' WHERE nama='"+nama+"'"
        conn = conndb.conndb()
        conn.queryExecute(strsql)
        self.loadData()

    def loadData(self):
        conn = conndb.conndb()
        strsql = "SELECT * FROM tbl_mahasiswa"
        result = conn.queryResult(strsql)
        print(result)
        row=0
        self.tableWidget.setRowCount(len(result))
        for user in result:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(user[0]))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(user[1]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(user[2]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(user[3]))
            row = row+1

    def deleteData(self):
        nama = self.lineEdit_nama.text()
        strsql = "DELETE FROM tbl_mahasiswa WHERE nama='"+nama+"'"
        conn = conndb.conndb()
        conn.queryExecute(strsql)
        self.loadData()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()