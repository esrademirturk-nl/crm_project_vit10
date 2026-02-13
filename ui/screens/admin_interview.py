import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6.uic import loadUi
from database import connect_google_sheets

class InterviewPage(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("AdminInterview.ui", self)
        
        # Clear search box on first click
        if hasattr(self, 'lineSearch'): # UI'da adını lineSearch olarak güncellediğini varsaydım
            self.lineSearch.cursorPositionChanged.connect(self.clear_on_first_click)
        
        self.load_table_data()
        
        # BUTTON CONNECTIONS
        self.buttonSearch.clicked.connect(self.search_function)
        self.buttonSentProjects.clicked.connect(self.filter_sent_projects)
        self.buttonReceivedProjects.clicked.connect(self.filter_received_projects)
        self.buttonBack.clicked.connect(self.close) 
        self.buttonExit.clicked.connect(self.exit_app)

    def clear_on_first_click(self):
        self.lineSearch.clear()
        try:
            self.lineSearch.cursorPositionChanged.disconnect(self.clear_on_first_click)
        except:
            pass

    def load_table_data(self):
        try:
            ss = connect_google_sheets()
            sheet = ss.worksheet("Interviews") 
            data = sheet.get_all_records()
            
            if not data:
                print("WARNING: No data found in the sheet!")
                return

            self.tableWidget.setRowCount(len(data))
            for row, entry in enumerate(data):
                # Using .get() with English headers
                self.tableWidget.setItem(row, 0, QTableWidgetItem(str(entry.get('FULL-NAME', ''))))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(str(entry.get('PROJECT-SENT-DATE', ''))))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(str(entry.get('PROJECT-RECEIVED-DATE', ''))))
            
            self.tableWidget.resizeRowsToContents()
            self.tableWidget.resizeColumnsToContents()
            print(f"System: {len(data)} rows loaded successfully.")
                    
        except Exception as e:
            print(f"!!! CRITICAL ERROR (Table): {e}")

    def search_function(self):
        search_text = self.lineSearch.text().lower()
        for r in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(r, 0) # Column 0: FULL-NAME
            hide_row = search_text not in item.text().lower() if item else True
            self.tableWidget.setRowHidden(r, hide_row)

    def filter_sent_projects(self):
        # Column 1: PROJECT-SENT-DATE
        self.apply_filter(1)

    def filter_received_projects(self):
        # Column 2: PROJECT-RECEIVED-DATE
        self.apply_filter(2)

    def apply_filter(self, column_index):
        for r in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(r, column_index)
            if not item or item.text().strip() == "" or item.text().lower() == "none":
                self.tableWidget.setRowHidden(r, True)
            else:
                self.tableWidget.setRowHidden(r, False)
            
    def exit_app(self):
        print("System: Closing application...")
        QApplication.instance().quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = InterviewPage()
    win.show()
    sys.exit(app.exec())