from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap, QPainter, QPainterPath
from PySide6.QtCore import Qt

colors = {
    "background": "#1C2230",
    "primary": "#2C3449",
    "secondary": "#B9FF66",
    "tertiary": "#444D64",
    "white": "#FFFFFF",
    "black": "#000000",
}
btn_off =f"""
    background-color: {colors['tertiary']};
    color: {colors['white']};
    padding: 10px 20px;
    border: none;
    border-radius: 10px;
    font-size: 16px;
    font-weight: bold;
"""
btn_on = f"""
    background-color: {colors['secondary']};
    color: {colors['black']};
    padding: 10px 20px;
    border: none;
    border-radius: 10px;
    font-size: 16px;
    font-weight: bold;
"""

def circular_pixmap(path, size):
    original = QPixmap(path).scaled(size, size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

    circular = QPixmap(size, size)
    circular.fill(Qt.transparent)

    painter = QPainter(circular)
    painter.setRenderHint(QPainter.Antialiasing)

    path_circle = QPainterPath()
    path_circle.addEllipse(0, 0, size, size)

    painter.setClipPath(path_circle)
    painter.drawPixmap(0, 0, original)
    painter.end()

    return circular
def debug_widget(text, color):
    
    w = QLabel(text)
    w.setStyleSheet(f"""
        border: 1px solid white;
    """)
    return w
def all_btns_off():
    btn_whatsapp_sender.setEnabled(True)
    btn_whatsapp_sender.setStyleSheet(btn_off)
    btn_daily_sessions.setEnabled(True)
    btn_daily_sessions.setStyleSheet(btn_off)
app = QApplication([])

window = QMainWindow()
window.setStyleSheet(f"background-color: {colors['background']};")

center = QWidget()
main_grid = QGridLayout(center)

menu = QWidget()
menu.styleSheet()
menu_grid = QGridLayout(menu)


logo = QLabel()
logo.setPixmap(QPixmap("assets/logo.jpeg").scaled(120, 120, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation))
menu_grid.addWidget(logo,1,1,2,2, Qt.AlignCenter)

#btn_whatsapp_sender test
btn_whatsapp_sender = QPushButton("💬 Whatsapp Sender")
btn_whatsapp_sender.setStyleSheet(btn_off)
def on_whatsapp_sender_click():
    all_btns_off()
    print("Button Clicked!")
    btn_whatsapp_sender.setEnabled(False)
    btn_whatsapp_sender.setStyleSheet(btn_on)
    
btn_whatsapp_sender.clicked.connect(on_whatsapp_sender_click)
menu_grid.addWidget(btn_whatsapp_sender,4,1,2,2)

#btn_daily_sessions test
btn_daily_sessions = QPushButton("📚 Daily Sessions")
btn_daily_sessions.setStyleSheet(btn_off)
def on_daily_sessions_click():
    all_btns_off()
    print("Button Clicked!")
    btn_daily_sessions.setEnabled(False)
    btn_daily_sessions.setStyleSheet(btn_on)

btn_daily_sessions.clicked.connect(on_daily_sessions_click)
menu_grid.addWidget(btn_daily_sessions,6,1,2,2)

menu.setStyleSheet(f"""
    background-color: {colors['primary']};
    border-radius: 15px;
""")
menu_grid.addWidget(debug_widget("Menu", colors['secondary']), 8,0, 25, 4)


main_grid.addWidget(menu, 0,0, 25, 4)
main_grid.addWidget(debug_widget("Main Content Area", colors['secondary']), 0,4, 25, 21)


"""used = [(1,1), (2,1), (2,2), (1,2),(4,1), (5,1), (5,2), (4,2)]
for row in range(20):
    for col in range(25):
        if (row, col) in used:
            continue
        
        main_grid.addWidget(debug_widget(f"{row},{col}", "#875F5F"), row, col)"""
window.setCentralWidget(center)
window.showMaximized()   

app.exec()