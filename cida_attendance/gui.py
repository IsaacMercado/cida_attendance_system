import signal
import sys

from PySide6.QtCore import QTimer
from PySide6.QtGui import QAction, QIcon, QIntValidator
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMenu,
    QMessageBox,
    QPushButton,
    QSystemTrayIcon,
    QVBoxLayout,
    QWidget,
)

from cida_attendance import tasks
from cida_attendance.config import check_config, load_config, save_config


class FormWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Formulario")
        self.setGeometry(100, 100, 300, 200)

        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
                font-size: 14px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px;
            }
        """)

        layout = QVBoxLayout()
        config = load_config()

        self.label_user = QLabel("User:")
        self.entry_user = QLineEdit(text=config["user"])
        layout.addWidget(self.label_user)
        layout.addWidget(self.entry_user)

        self.label_password = QLabel("Password:")
        self.entry_password = QLineEdit(
            text=config["password"],
            echoMode=QLineEdit.Password,
        )
        layout.addWidget(self.label_password)
        layout.addWidget(self.entry_password)

        self.label_ip = QLabel("IP:")
        self.entry_ip = QLineEdit(text=config["ip"])
        layout.addWidget(self.label_ip)
        layout.addWidget(self.entry_ip)

        self.label_port = QLabel("Port:")
        self.entry_port = QLineEdit(text=str(config["port"]))
        self.entry_port.setValidator(QIntValidator(bottom=0, top=65535))
        layout.addWidget(self.label_port)
        layout.addWidget(self.entry_port)

        self.label_uri_db = QLabel("URI DB:")
        self.entry_uri_db = QLineEdit(text=config["uri_db"])
        layout.addWidget(self.label_uri_db)
        layout.addWidget(self.entry_uri_db)

        self.label_name = QLabel("Name:")
        self.entry_name = QLineEdit(text=config["name"])
        layout.addWidget(self.label_name)
        layout.addWidget(self.entry_name)

        self.submit_button = QPushButton("Guardar")
        self.submit_button.clicked.connect(self.submit_form)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit_form(self):
        save_config(
            self.entry_uri_db.text(),
            self.entry_user.text(),
            self.entry_password.text(),
            self.entry_ip.text(),
            int(self.entry_port.text()),
            self.entry_name.text(),
        )
        self.close()


class App:
    def __init__(self):
        self.app = QApplication(sys.argv)

        self.app.setQuitOnLastWindowClosed(False)

        if not QSystemTrayIcon.isSystemTrayAvailable():
            QMessageBox.critical(
                None,
                "Error",
                "La bandeja del sistema no está disponible en este sistema.",
            )
            sys.exit(1)

        self.icon = QIcon("cida_attendance/assets/cida-logo.png")
        self.app.setWindowIcon(self.icon)

        self.tray_icon = QSystemTrayIcon(self.icon, parent=self.app)
        self.tray_icon.setToolTip("Sincronización de Dispositivos")

        menu = QMenu()

        check_database_action = QAction("Check database", menu)
        check_database_action.triggered.connect(self.check_database)
        menu.addAction(check_database_action)

        check_device_action = QAction("Check device", menu)
        check_device_action.triggered.connect(self.check_device)
        menu.addAction(check_device_action)

        synchronize_action = QAction("Synchronize", menu)
        synchronize_action.triggered.connect(self.synchronize)
        menu.addAction(synchronize_action)

        set_up_action = QAction("Set up", menu)
        set_up_action.triggered.connect(self.open_form)
        menu.addAction(set_up_action)

        exit_action = QAction("Exit", menu)
        exit_action.triggered.connect(self.exit_app)
        menu.addAction(exit_action)

        self.tray_icon.setContextMenu(menu)
        self.tray_icon.show()
        self.timer = QTimer()

    def open_form(self):
        self.form_window = FormWindow()
        self.form_window.show()

    def check_database(self):
        if not check_config():
            self.tray_icon.showMessage(
                "Required configuration is missing",
                "Please set up the configuration",
                icon=QSystemTrayIcon.Critical,
            )
            return

        if tasks.check_db():
            self.tray_icon.showMessage(
                "Database is OK",
                "Database is OK",
            )
        else:
            self.tray_icon.showMessage(
                "Database is not OK",
                "Database is not OK",
                icon=QSystemTrayIcon.Critical,
            )

    def check_device(self):
        if not check_config():
            self.tray_icon.showMessage(
                "Required configuration is missing",
                "Please set up the configuration",
                icon=QSystemTrayIcon.Critical,
            )
            return

        if tasks.check_device():
            self.tray_icon.showMessage(
                "Device is OK",
                "Device is OK",
            )
        else:
            self.tray_icon.showMessage(
                "Device is not OK",
                "Device is not OK",
            )

    def synchronize(self):
        if not check_config():
            self.tray_icon.showMessage(
                "Required configuration is missing",
                "Please set up the configuration",
                icon=QSystemTrayIcon.Critical,
            )
            return

        if tasks.synchronize():
            self.tray_icon.showMessage(
                "Synchronized",
                "Synchronized",
            )
        else:
            self.tray_icon.showMessage(
                "Not synchronized",
                "Not synchronized",
                icon=QSystemTrayIcon.Critical,
            )

    def exit_app(self):
        self.tray_icon.hide()
        if self.timer.isActive():
            self.timer.stop()
        self.app.quit()

    def run(self):
        signal.signal(signal.SIGINT, self.handle_interrupt)
        sys.exit(self.app.exec())

    def handle_interrupt(self, signum, frame):
        self.exit_app()


if __name__ == "__main__":
    App().run()
