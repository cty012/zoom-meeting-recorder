import PyQt5.QtWidgets as qw


class MainWindow(qw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('Zoom Meeting Recorder')
        self.setGeometry(200, 200, 1000, 600)

        self.table_widget = TableWidget(self)
        self.setCentralWidget(self.table_widget)


class TableWidget(qw.QWidget):

    def __init__(self, parent):
        super(TableWidget, self).__init__(parent)

        # Initialize tab screen
        self.tabs = qw.QTabWidget(self)
        self.tabs.setGeometry(0, 0, 800, 50)
        self.tab1 = qw.QWidget()
        self.tab2 = qw.QWidget()
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")
        self.tab1.setStyleSheet('QTabBar::tab { height: 100px; width: 100px; }')
        self.tab2.setStyleSheet('QTabBar::tab { height: 100px; width: 100px; }')
