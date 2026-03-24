from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap, QPainter, QPainterPath
from PySide6.QtCore import Qt

colors = {
    "background": "#1C2230",
    "primary": "#252B3B",
    "secondary": "#B9FF66",
    "tertiary": "#444D64",
    "white": "#FFFFFF",
    "black": "#000000",
}
btn_off =f"""
    background-color: {colors['primary']};
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
def on_whatsapp_sender_click():
    all_btns_off()
    print("Button Clicked!")
    btn_whatsapp_sender.setEnabled(False)
    btn_whatsapp_sender.setStyleSheet(btn_on)
def on_daily_sessions_click():
    all_btns_off()
    print("Button Clicked!")
    btn_daily_sessions.setEnabled(False)
    btn_daily_sessions.setStyleSheet(btn_on)



app = QApplication([])

window = QMainWindow()
window.setStyleSheet(f"background-color: {colors['background']};")

center = QWidget()
main_layout = QVBoxLayout(center)

content_area = QWidget()
content_layout = QHBoxLayout(content_area)
main_layout.addWidget(content_area)


left_panel = QWidget()
left_panel.setStyleSheet(f"background-color: {colors['primary']};")
left_panel_layout = QVBoxLayout(left_panel)
left_panel.setFixedWidth(200)


logo = QLabel()
logo.setPixmap(QPixmap("assets/logo.jpeg").scaled(120, 120, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation))
left_panel_layout.addWidget(logo, alignment=Qt.AlignCenter)
left_panel_layout.addSpacing(20)



#btn_whatsapp_sender test
btn_whatsapp_sender = QPushButton("💬Whatsapp")
btn_whatsapp_sender.setStyleSheet(btn_off)
btn_whatsapp_sender.setFixedWidth(180)
btn_whatsapp_sender.clicked.connect(on_whatsapp_sender_click)
left_panel_layout.addWidget(btn_whatsapp_sender, alignment=Qt.AlignCenter)
left_panel_layout.addSpacing(20)

#btn_daily_sessions test
btn_daily_sessions = QPushButton("📚Daily")
btn_daily_sessions.setStyleSheet(btn_off)
btn_daily_sessions.setFixedWidth(180)
btn_daily_sessions.clicked.connect(on_daily_sessions_click)
left_panel_layout.addWidget(btn_daily_sessions, alignment=Qt.AlignCenter)
left_panel_layout.addSpacing(20)


left_panel.setStyleSheet(f"""
    background-color: {colors['primary']};
    border-radius: 15px;
""")
left_panel_layout.addStretch()

content_layout.addWidget(left_panel)

right_panel = QWidget()
right_panel.setStyleSheet(f"background-color: {colors['tertiary']}; border-radius: 15px;")
content_layout.addWidget(right_panel)

footer = QLabel("© 2026  Mostafa Donia. All rights reserved.")
footer.setStyleSheet(f"color: {colors['white']}; font-size: 12px;")
footer.setMaximumHeight(30)
main_layout.addWidget(footer, alignment=Qt.AlignCenter)

window.setCentralWidget(center)
window.showMaximized()   

app.exec()