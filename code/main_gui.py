from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap, QPainter, QPainterPath
from PySide6.QtCore import Qt, QPropertyAnimation,QParallelAnimationGroup

colors = {
    "background": "#1C2230",
    "primary": "#252B3B",
    "secondary": "#B9FF66",
    "tertiary": "#444D64",
    "white": "#FFFFFF",
    "black": "#000000",
    "whatsapp_green": "#25D366",
    "daily_blue": "#007BFF",
    "financial_yellow": "#FFC107",
    "receivables_purple": "#9C27B0",
    "running_red": "#FF5722",
    "orders_orange": "#FF9800",
    "waiting_gray": "#9E9E9E",  
    "tournament_pink": "#E91E63",
    "dashboard_cyan": "#00BCD4",
    "savings_debt_brown": "#795548",
    "salaries_teal": "#009688",
    "students_indigo": "#3F51B5",
    "cash_counter_gray": "#607D8B",
    "settings_lime": "#CDDC39",
    "prices_orange": "#FF5722",
}
btn_off =f"""
    background-color: {colors['primary']};
    color: {colors['white']};
    padding: 10px 20px;
    border: none;
    border-radius: 10px;
    font-size: 10px;
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
    btn_financial.setEnabled(True)
    btn_financial.setStyleSheet(btn_off)
    btn_receivables.setEnabled(True)
    btn_receivables.setStyleSheet(btn_off)
    btn_waiting.setEnabled(True)
    btn_waiting.setStyleSheet(btn_off)
    btn_savings_debt.setEnabled(True)
    btn_savings_debt.setStyleSheet(btn_off)
    btn_salaries.setEnabled(True)
    btn_salaries.setStyleSheet(btn_off)
    btn_students.setEnabled(True)
    btn_students.setStyleSheet(btn_off)
    btn_cash_counter.setEnabled(True)
    btn_cash_counter.setStyleSheet(btn_off)
    btn_settings.setEnabled(True)
    btn_settings.setStyleSheet(btn_off)
    btn_prices.setEnabled(True)
    btn_prices.setStyleSheet(btn_off)
    btn_running.setEnabled(True)
    btn_running.setStyleSheet(btn_off)
    btn_orders.setEnabled(True)
    btn_orders.setStyleSheet(btn_off)
    btn_tournament.setEnabled(True)
    btn_tournament.setStyleSheet(btn_off)
    btn_dashboard.setEnabled(True)
    btn_dashboard.setStyleSheet(btn_off)
    

def on_whatsapp_sender_click():
    fade_to_page(0)
    all_btns_off()
    print("Button Clicked!")
    btn_whatsapp_sender.setEnabled(False)
    btn_whatsapp_sender.setStyleSheet(btn_on)
def on_daily_sessions_click():
    fade_to_page(1)
    all_btns_off()
    print("Button Clicked!")
    btn_daily_sessions.setEnabled(False)
    btn_daily_sessions.setStyleSheet(btn_on)
def on_financial_click():
    fade_to_page(2)
    all_btns_off()
    print("Button Clicked!")
    btn_financial.setEnabled(False)
    btn_financial.setStyleSheet(btn_on)
def on_receivables_click():
    fade_to_page(3)
    all_btns_off()
    print("Button Clicked!")
    btn_receivables.setEnabled(False)
    btn_receivables.setStyleSheet(btn_on)
def on_waiting_click():
    fade_to_page(4)
    all_btns_off()
    print("Button Clicked!")
    btn_waiting.setEnabled(False)
    btn_waiting.setStyleSheet(btn_on)
def on_savings_debt_click():
    fade_to_page(5)
    all_btns_off()
    print("Button Clicked!")
    btn_savings_debt.setEnabled(False)
    btn_savings_debt.setStyleSheet(btn_on)
def on_salaries_click():
    fade_to_page(6)
    all_btns_off()
    print("Button Clicked!")
    btn_salaries.setEnabled(False)
    btn_salaries.setStyleSheet(btn_on)
def on_students_click():
    fade_to_page(7)
    all_btns_off()
    print("Button Clicked!")
    btn_students.setEnabled(False)
    btn_students.setStyleSheet(btn_on)
def on_cash_counter_click():
    fade_to_page(8)
    all_btns_off()
    print("Button Clicked!")
    btn_cash_counter.setEnabled(False)
    btn_cash_counter.setStyleSheet(btn_on)
def on_settings_click():
    fade_to_page(9)
    all_btns_off()
    print("Button Clicked!")
    btn_settings.setEnabled(False)
    btn_settings.setStyleSheet(btn_on)
def on_prices_click():
    fade_to_page(10)
    all_btns_off()
    print("Button Clicked!")
    btn_prices.setEnabled(False)
    btn_prices.setStyleSheet(btn_on)
def on_running_click():
    fade_to_page(11)
    all_btns_off()
    print("Button Clicked!")
    btn_running.setEnabled(False)
    btn_running.setStyleSheet(btn_on)
def on_orders_click():
    fade_to_page(12)
    all_btns_off()
    print("Button Clicked!")
    btn_orders.setEnabled(False)
    btn_orders.setStyleSheet(btn_on)
def on_tournament_click():
    fade_to_page(13)
    all_btns_off()
    print("Button Clicked!")
    btn_tournament.setEnabled(False)
    btn_tournament.setStyleSheet(btn_on)
def on_dashboard_click():
    fade_to_page(14)
    all_btns_off()
    print("Button Clicked!")
    btn_dashboard.setEnabled(False)
    btn_dashboard.setStyleSheet(btn_on)

def create_whatsapp_page():
    page = QWidget()
    page.setStyleSheet(f"background-color: {colors['whatsapp_green']}; border-radius: 15px;")
    layout = QVBoxLayout(page)
    label = QLabel("WhatsApp Sender Page")
    label.setStyleSheet(f"color: {colors['white']}; font-size: 24px;")
    layout.addWidget(label, alignment=Qt.AlignCenter)
    return page
def create_daily_sessions_page():
    page = QWidget()
    page.setStyleSheet(f"background-color: {colors['daily_blue']}; border-radius: 15px;")
    layout = QVBoxLayout(page)
    label = QLabel("Daily Sessions Page")
    label.setStyleSheet(f"color: {colors['white']}; font-size: 24px;")
    layout.addWidget(label, alignment=Qt.AlignCenter)
    return page
def create_financial_page():
    page = QWidget()
    page.setStyleSheet(f"background-color: {colors['financial_yellow']}; border-radius: 15px;")
    layout = QVBoxLayout(page)
    label = QLabel("financial Page")
    label.setStyleSheet(f"color: {colors['black']}; font-size: 24px;")
    layout.addWidget(label, alignment=Qt.AlignCenter)
    return page
def create_receivables_page():
    page = QWidget()
    page.setStyleSheet(f"background-color: {colors['receivables_purple']}; border-radius: 15px;")
    layout = QVBoxLayout(page)
    label = QLabel("Receivables Page")
    label.setStyleSheet(f"color: {colors['white']}; font-size: 24px;")
    layout.addWidget(label, alignment=Qt.AlignCenter)
    return page
def create_waiting_page():
    page = QWidget()
    page.setStyleSheet(f"background-color: {colors['waiting_gray']}; border-radius: 15px;")
    layout = QVBoxLayout(page)
    label = QLabel("Waiting Page")
    label.setStyleSheet(f"color: {colors['white']}; font-size: 24px;")
    layout.addWidget(label, alignment=Qt.AlignCenter)
    return page
def create_savings_debt_page():
    page = QWidget()
    page.setStyleSheet(f"background-color: {colors['savings_debt_brown']}; border-radius: 15px;")
    layout = QVBoxLayout(page)
    label = QLabel("Savings & Debt Page")
    label.setStyleSheet(f"color: {colors['white']}; font-size: 24px;")
    layout.addWidget(label, alignment=Qt.AlignCenter)
    return page
def create_salaries_page():
    page = QWidget()
    page.setStyleSheet(f"background-color: {colors['salaries_teal']}; border-radius: 15px;")
    layout = QVBoxLayout(page)
    label = QLabel("Salaries Page")
    label.setStyleSheet(f"color: {colors['white']}; font-size: 24px;")
    layout.addWidget(label, alignment=Qt.AlignCenter)
    return page
def create_students_page():
    page = QWidget()
    page.setStyleSheet(f"background-color: {colors['students_indigo']}; border-radius: 15px;")
    layout = QVBoxLayout(page)
    label = QLabel("Students Page")
    label.setStyleSheet(f"color: {colors['white']}; font-size: 24px;")
    layout.addWidget(label, alignment=Qt.AlignCenter)
    return page
def create_cash_counter_page():
    page = QWidget()
    page.setStyleSheet(f"background-color: {colors['cash_counter_gray']}; border-radius: 15px;")
    layout = QVBoxLayout(page)
    label = QLabel("Cash Counter Page")
    label.setStyleSheet(f"color: {colors['white']}; font-size: 24px;")
    layout.addWidget(label, alignment=Qt.AlignCenter)
    return page
def create_settings_page():
    page = QWidget()
    page.setStyleSheet(f"background-color: {colors['settings_lime']}; border-radius: 15px;")
    layout = QVBoxLayout(page)
    label = QLabel("Settings Page")
    label.setStyleSheet(f"color: {colors['black']}; font-size: 24px;")
    layout.addWidget(label, alignment=Qt.AlignCenter)
    return page
def create_prices_page():
    page = QWidget()
    page.setStyleSheet(f"background-color: {colors['prices_orange']}; border-radius: 15px;")
    layout = QVBoxLayout(page)
    label = QLabel("Prices Page")
    label.setStyleSheet(f"color: {colors['white']}; font-size: 24px;")
    layout.addWidget(label, alignment=Qt.AlignCenter)
    return page
def create_running_page():
    page = QWidget()
    page.setStyleSheet(f"background-color: {colors['running_red']}; border-radius: 15px;")
    layout = QVBoxLayout(page)
    label = QLabel("Running Page")
    label.setStyleSheet(f"color: {colors['white']}; font-size: 24px;")
    layout.addWidget(label, alignment=Qt.AlignCenter)
    return page
def create_orders_page():
    page = QWidget()
    page.setStyleSheet(f"background-color: {colors['orders_orange']}; border-radius: 15px;")
    layout = QVBoxLayout(page)
    label = QLabel("Orders Page")
    label.setStyleSheet(f"color: {colors['white']}; font-size: 24px;")
    layout.addWidget(label, alignment=Qt.AlignCenter)
    return page
def create_tournament_page():
    page = QWidget()
    page.setStyleSheet(f"background-color: {colors['tournament_pink']}; border-radius: 15px;")
    layout = QVBoxLayout(page)
    label = QLabel("Tournament Page")
    label.setStyleSheet(f"color: {colors['white']}; font-size: 24px;")
    layout.addWidget(label, alignment=Qt.AlignCenter)
    return page
def create_dashboard_page():
    page = QWidget()
    page.setStyleSheet(f"background-color: {colors['dashboard_cyan']}; border-radius: 15px;")
    layout = QVBoxLayout(page)
    label = QLabel("Dashboard Page")
    label.setStyleSheet(f"color: {colors['white']}; font-size: 24px;")
    layout.addWidget(label, alignment=Qt.AlignCenter)
    return page


def fade_to_page(index):
    global fade_group
    current_widget = right_panel.currentWidget()
    next_widget = right_panel.widget(index)

    # effects
    current_effect = QGraphicsOpacityEffect(current_widget)
    next_effect = QGraphicsOpacityEffect(next_widget)

    current_widget.setGraphicsEffect(current_effect)
    next_widget.setGraphicsEffect(next_effect)

    # animations
    fade_out = QPropertyAnimation(current_effect, b"opacity")
    fade_out.setDuration(500)
    fade_out.setStartValue(1)
    fade_out.setEndValue(0)

    fade_in = QPropertyAnimation(next_effect, b"opacity")
    fade_in.setDuration(500)
    fade_in.setStartValue(0)
    fade_in.setEndValue(1)

    # group
    group = QParallelAnimationGroup()
    group.addAnimation(fade_out)
    group.addAnimation(fade_in)

    # قبل ما يبدأ: نجهز الصفحة الجديدة
    next_widget.setGraphicsEffect(next_effect)
    next_effect.setOpacity(0)
    right_panel.setCurrentWidget(next_widget)

    fade_group = group  
    group.start()

fade_group = None  
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



#btn_whatsapp_sender test
btn_whatsapp_sender = QPushButton("💬Whatsapp")
btn_whatsapp_sender.setStyleSheet(btn_off)
btn_whatsapp_sender.setFixedWidth(180)
btn_whatsapp_sender.clicked.connect(on_whatsapp_sender_click)
left_panel_layout.addWidget(btn_whatsapp_sender, alignment=Qt.AlignCenter)

#btn_daily_sessions test
btn_daily_sessions = QPushButton("📚Daily")
btn_daily_sessions.setStyleSheet(btn_off)
btn_daily_sessions.setFixedWidth(180)
btn_daily_sessions.clicked.connect(on_daily_sessions_click)
left_panel_layout.addWidget(btn_daily_sessions, alignment=Qt.AlignCenter)


#btn_financial
# test
btn_financial = QPushButton("💳financial")
btn_financial.setStyleSheet(btn_off)
btn_financial.setFixedWidth(180)
btn_financial.clicked.connect(on_financial_click)
left_panel_layout.addWidget(btn_financial, alignment=Qt.AlignCenter)

#btn_receivables
btn_receivables = QPushButton("📊Receivables")
btn_receivables.setStyleSheet(btn_off)
btn_receivables.setFixedWidth(180)
btn_receivables.clicked.connect(on_receivables_click)
left_panel_layout.addWidget(btn_receivables, alignment=Qt.AlignCenter)

#btn_waiting
btn_waiting = QPushButton("⏳Waiting")
btn_waiting.setStyleSheet(btn_off)
btn_waiting.setFixedWidth(180)
btn_waiting.clicked.connect(on_waiting_click)
left_panel_layout.addWidget(btn_waiting, alignment=Qt.AlignCenter)

#btn_savings_debt
btn_savings_debt = QPushButton("💰Savings & Debt")
btn_savings_debt.setStyleSheet(btn_off)
btn_savings_debt.setFixedWidth(180)
btn_savings_debt.clicked.connect(on_savings_debt_click)
left_panel_layout.addWidget(btn_savings_debt, alignment=Qt.AlignCenter)

#btn_salaries
btn_salaries = QPushButton("👥Salaries")
btn_salaries.setStyleSheet(btn_off)
btn_salaries.setFixedWidth(180)
btn_salaries.clicked.connect(on_salaries_click)
left_panel_layout.addWidget(btn_salaries, alignment=Qt.AlignCenter)

#btn_students
btn_students = QPushButton("🎓Students")
btn_students.setStyleSheet(btn_off)
btn_students.setFixedWidth(180)
btn_students.clicked.connect(on_students_click)
left_panel_layout.addWidget(btn_students, alignment=Qt.AlignCenter)

#btn_cash_counter
btn_cash_counter = QPushButton("💵Cash Counter")
btn_cash_counter.setStyleSheet(btn_off)
btn_cash_counter.setFixedWidth(180)
btn_cash_counter.clicked.connect(on_cash_counter_click)
left_panel_layout.addWidget(btn_cash_counter, alignment=Qt.AlignCenter)

#btn_settings
btn_settings = QPushButton("⚙️Settings")
btn_settings.setStyleSheet(btn_off)
btn_settings.setFixedWidth(180)
btn_settings.clicked.connect(on_settings_click)
left_panel_layout.addWidget(btn_settings, alignment=Qt.AlignCenter)

#btn_prices
btn_prices = QPushButton("🏷️Prices")
btn_prices.setStyleSheet(btn_off)
btn_prices.setFixedWidth(180)
btn_prices.clicked.connect(on_prices_click)
left_panel_layout.addWidget(btn_prices, alignment=Qt.AlignCenter)

#btn_running
btn_running = QPushButton("🏃Running")
btn_running.setStyleSheet(btn_off)
btn_running.setFixedWidth(180)
btn_running.clicked.connect(on_running_click)
left_panel_layout.addWidget(btn_running, alignment=Qt.AlignCenter)

#btn_orders
btn_orders = QPushButton("📦Orders")
btn_orders.setStyleSheet(btn_off)
btn_orders.setFixedWidth(180)
btn_orders.clicked.connect(on_orders_click)
left_panel_layout.addWidget(btn_orders, alignment=Qt.AlignCenter)

#btn_tournament
btn_tournament = QPushButton("🏆Tournament")
btn_tournament.setStyleSheet(btn_off)
btn_tournament.setFixedWidth(180)
btn_tournament.clicked.connect(on_tournament_click)
left_panel_layout.addWidget(btn_tournament, alignment=Qt.AlignCenter)

#btn_dashboard
btn_dashboard = QPushButton("📊Dashboard")
btn_dashboard.setStyleSheet(btn_off)
btn_dashboard.setFixedWidth(180)
btn_dashboard.clicked.connect(on_dashboard_click)
left_panel_layout.addWidget(btn_dashboard, alignment=Qt.AlignCenter)


left_panel.setStyleSheet(f"""
    background-color: {colors['primary']};
    border-radius: 15px;
""")
left_panel_layout.addStretch()

content_layout.addWidget(left_panel)

right_panel = QStackedWidget()
content_layout.addWidget(right_panel)


whatsapp_page = create_whatsapp_page()
right_panel.addWidget(whatsapp_page)

daily_sessions_page = create_daily_sessions_page()
right_panel.addWidget(daily_sessions_page)

financial_page = create_financial_page()
right_panel.addWidget(financial_page)

receivables_page = create_receivables_page()
right_panel.addWidget(receivables_page)

waiting_page = create_waiting_page()
right_panel.addWidget(waiting_page)

savings_debt_page = create_savings_debt_page()
right_panel.addWidget(savings_debt_page)

salaries_page = create_salaries_page()
right_panel.addWidget(salaries_page)

students_page = create_students_page()
right_panel.addWidget(students_page)

cash_counter_page = create_cash_counter_page()
right_panel.addWidget(cash_counter_page)

settings_page = create_settings_page()
right_panel.addWidget(settings_page)

prices_page = create_prices_page()
right_panel.addWidget(prices_page)

running_page = create_running_page()
right_panel.addWidget(running_page)

orders_page = create_orders_page()
right_panel.addWidget(orders_page)

tournament_page = create_tournament_page()
right_panel.addWidget(tournament_page)

dashboard_page = create_dashboard_page()
right_panel.addWidget(dashboard_page)



right_panel.setCurrentIndex(0)


footer = QLabel("© 2026  Mostafa Donia. All rights reserved.")
footer.setStyleSheet(f"color: {colors['white']}; font-size: 12px;")
footer.setMaximumHeight(30)
main_layout.addWidget(footer, alignment=Qt.AlignCenter)

window.setCentralWidget(center)
window.showMaximized()   

app.exec()