import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6.uic import loadUi
from database import connect_google_sheets

class AdvisorPage(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("AdminAdvisor.ui", self) 
        
        self.all_data = [] 
        self.lineArama.mousePressEvent = lambda event: self.lineArama.clear()
        self.buttonGorusmeler.clicked.connect(self.populate_table) 
        self.buttonAra.clicked.connect(self.search_function)
        self.buttonTercihler.clicked.connect(self.close) 
        self.buttonExit.clicked.connect(lambda: QApplication.instance().quit())
        self.boxTercihler.currentIndexChanged.connect(self.filter_by_result)

    def populate_table(self):
        try:
            ss = connect_google_sheets()
            sheet = ss.worksheet("Mentorluk") 
            self.all_data = sheet.get_all_records() 
            self.display_data(self.all_data)
            print("System: Advisor data loaded.")
        except Exception as e:
            print(f"!!! Advisor Table Error: {e}")

    def display_data(self, data_list):
        if not data_list: return
        self.tableWidget.setRowCount(len(data_list))
        for row, entry in enumerate(data_list):
            self.tableWidget.setRowHidden(row, False)
            # Database keys must match your Google Sheet column headers exactly
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(entry.get('GORUSME-TARIHI', ''))))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(entry.get('AD-SOYAD', ''))))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(entry.get('MENTOR-GORUSU', ''))))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(str(entry.get('IT-BILGISI', ''))))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(str(entry.get('YOGUNLUK', ''))))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(str(entry.get('YORUMLAR', ''))))
        self.tableWidget.resizeColumnsToContents()

    def search_function(self):
        search_text = self.lineArama.text().strip().lower()
        if not search_text or search_text == "enter search text...":
            return
        for r in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(r, 1) # Searching in Name column
            self.tableWidget.setRowHidden(r, not (item and search_text in item.text().lower()))

    def filter_by_result(self):
        """Filters rows based on the 'Result' score selected in the ComboBox."""
        try:
            target_result = str(self.boxTercihler.currentIndex() + 1)
            
            if self.tableWidget.rowCount() == 0: 
                return

            for r in range(self.tableWidget.rowCount()):
                full_name = self.tableWidget.item(r, 1).text().strip()
                candidate_data = next((item for item in self.all_data if item.get('AD-SOYAD') == full_name), None)
                
                if candidate_data:
                    result_value = str(candidate_data.get('SONUC', '')).strip()
                    self.tableWidget.setRowHidden(r, result_value != target_result)
                else:
                    self.tableWidget.setRowHidden(r, True)

        except Exception as e:
            print(f"Filtering error: {e}")
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = AdvisorPage()
    win.show()
    sys.exit(app.exec())