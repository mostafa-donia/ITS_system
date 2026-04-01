from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap, QPainter, QPainterPath
from PySide6.QtCore import Qt, QPropertyAnimation,QParallelAnimationGroup
from time import strftime,sleep
from threading import Thread
from whatsapp import prepare_messages, prepare_phones, sending

clock  =  strftime("%I:%M:%S")
date =  strftime("%a.%d/%m")
time =  "🕰️ "+clock+" 📆 "+ date
time_label = ""

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
    font-size: 30px;
    font-weight: bold;
"""
btn_on = f"""
    background-color: {colors['secondary']};
    color: {colors['black']};
    padding: 10px 20px;
    border: none;
    border-radius: 10px;
    font-size: 30px;
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
def time_update():
    global time,time_label
    clock  =  strftime("%I:%M:%S")
    date =  strftime("%a.%d/%m")
    time =  "🕰️ "+clock+" 📆 "+ date
    time_label.setText(time)
    sleep(1)
    time_update()

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

bulk_phone_entry = None
text_box = None
def send_bulk_message():
    global bulk_phone_entry, text_box
    print("Sending Bulk Message...")
    print("Raw Phones:", bulk_phone_entry.text())
    print("Raw Messages:", text_box.toPlainText())
    phones = prepare_phones(bulk_phone_entry.text())
    messages = prepare_messages(text_box.toPlainText())
    bulk_phone_entry.clear()
    text_box.clear()
    sending(phones, messages)
    

def create_whatsapp_page():
    global time,time_label,bulk_phone_entry,text_box
    page = QWidget()
    page.setStyleSheet(f"background-color: {colors['background']}; border-radius: 15px;")
    layout_page = QVBoxLayout(page)
    
    top_bar = QHBoxLayout()
    layout_page.addLayout(top_bar)
    
    icon_path = r"assets\whatsapp.ico"
    icon_label = QLabel()
    icon_label.setPixmap(QPixmap(icon_path).scaled(60, 60, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
)
    top_bar.addWidget(icon_label)
    top_bar.addSpacing(20)
    
    label = QLabel("WhatsApp Sender Page")
    label.setStyleSheet(f"color: {colors['white']}; font-size: 30px;  font-weight: bold;")
    top_bar.addWidget(label)
    top_bar.addStretch()
    
    clock  =  strftime("%I:%M:%S")
    date =  strftime("%d/%m")
    time =  "🕰️ "+clock+" 📆 "+ date
    time_label =  QLabel(time)
    time_label.setStyleSheet(f"color: {colors['white']}; font-size: 20px;  font-weight: bold;")
    top_bar.addWidget(time_label)
    Thread(target=time_update).start()
    
    layout_page.addSpacing(10)
    main_content = QHBoxLayout()
    layout_page.addLayout(main_content)
    
    bulk_send = QWidget()
    bulk_send.setMinimumHeight(screenh*0.65)
    bulk_send.setStyleSheet(f"background-color: {colors['primary']}; border-radius: 15px;")
    bulk_send_layout = QVBoxLayout(bulk_send)

    
    label = QLabel("Multi Phone Numbers📞")
    label.setStyleSheet(f"color: {colors['white']}; font-size: 20px;  font-weight: bold;")
    bulk_send_layout.addWidget(label,alignment=Qt.AlignCenter)
    bulk_send_layout.addSpacing(30)
    
    label = QLabel("  Phone Numbers : ")
    label.setStyleSheet(f"color: {colors['white']}; font-size: 15px;")
    bulk_send_layout.addWidget(label)
    bulk_send_layout.addSpacing(15)
    
    bulk_phone_entry = QLineEdit()
    bulk_phone_entry.setPlaceholderText("Enter phones seprated by comma....")   
    bulk_phone_entry.setStyleSheet(f"QLineEdit {{padding: 8px;border: 2px solid #555;border-radius: 6px; background-color: {colors['background']}; color: white; font-size: 14px; }}")
    bulk_send_layout.addWidget(bulk_phone_entry)
    bulk_send_layout.addSpacing(15)
    
    label = QLabel("  Messages : ")
    label.setStyleSheet(f"color: {colors['white']}; font-size: 15px;")
    bulk_send_layout.addWidget(label)
    bulk_send_layout.addSpacing(15)

    
    text_frame = QFrame()
    text_frame.setStyleSheet(f"""
        QFrame {{
            background-color: {colors['background']};
            border: 2px solid #555;
            border-radius: 8px;
        }}
    """)
    frame_layout = QVBoxLayout(text_frame)
    frame_layout.setContentsMargins(8, 8, 8, 8)
    text_box = QTextEdit(lineWrapColumnOrWidth=20)
    text_box.setPlaceholderText("Messages separated by comma or one message for all...")
    text_box.setLineWrapMode(QTextEdit.WidgetWidth)
    text_box.setFrameStyle(QFrame.NoFrame)
    text_box.setStyleSheet("""
        QTextEdit {
            background: transparent;
            color: white;
            border: none;
            font-size: 14px;
        }
    """)
    frame_layout.addWidget(text_box)
    bulk_send_layout.addWidget(text_frame)
    bulk_send_layout.addSpacing(15)
    
    send_button = QPushButton("Send Messages")
    send_button.setStyleSheet(f"""
        QPushButton {{
            background-color: {colors['secondary']};
            color: {colors['black']};
            padding: 10px 20px;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            font-weight: bold;
        }}
        QPushButton:hover {{
            background-color: {colors['white']};
        }}
    """)    
    send_button.clicked.connect(send_bulk_message)
    bulk_send_layout.addWidget(send_button, alignment=Qt.AlignCenter)
    bulk_send_layout.addSpacing(15)
    bulk_send_layout.addStretch()
    

    main_content.addWidget(bulk_send)
    main_content.addSpacing(10)
    
    course_send = QWidget()
    course_send.setMinimumHeight(screenh*0.65)
    course_send.setStyleSheet(f"background-color: {colors['primary']}; border-radius: 15px;")
    course_send_layout = QVBoxLayout(course_send)

    course_phone_entry = QLineEdit()
    course_phone_entry.setPlaceholderText(" 🚧 Under Construction 🚩")
    course_send_layout.addWidget(course_phone_entry)
    
    
    main_content.addWidget(course_send)
    main_content.addSpacing(10)
    
    byid = QWidget()
    byid.setMinimumHeight(screenh*0.65)
    byid.setStyleSheet(f"background-color: {colors['primary']}; border-radius: 15px;")
    byid_send_layout = QVBoxLayout(byid)
    byid_phone_entry = QLineEdit()
    byid_phone_entry.setPlaceholderText(" 🚧 Under Construction 🚩")
    byid_send_layout.addWidget(byid_phone_entry)
    
    main_content.addWidget(byid)
    main_content.addSpacing(10)

    
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
screenw,screenh =  app.primaryScreen().size().toTuple()
print(screenw,screenh)
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
left_panel.setFixedWidth(210)


logo = QLabel()
logo.setPixmap(QPixmap("assets/logo.jpeg").scaled(120, 120, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation))
left_panel_layout.addWidget(logo, alignment=Qt.AlignCenter)


button_grid = QWidget()
button_layout = QGridLayout(button_grid)
#btn_whatsapp_sender test
btn_whatsapp_sender = QPushButton("💬")
btn_whatsapp_sender.setStyleSheet(btn_on)
btn_whatsapp_sender.setFixedWidth(80)
btn_whatsapp_sender.clicked.connect(on_whatsapp_sender_click)
button_layout.addWidget(btn_whatsapp_sender, 0, 0, alignment=Qt.AlignCenter)

#btn_daily_sessions test
btn_daily_sessions = QPushButton("📚")
btn_daily_sessions.setStyleSheet(btn_off)
btn_daily_sessions.setFixedWidth(80)
btn_daily_sessions.clicked.connect(on_daily_sessions_click)
button_layout.addWidget(btn_daily_sessions, 0, 1, alignment=Qt.AlignCenter)


#btn_financial
# test
btn_financial = QPushButton("💳")
btn_financial.setStyleSheet(btn_off)
btn_financial.setFixedWidth(80)
btn_financial.clicked.connect(on_financial_click)
button_layout.addWidget(btn_financial, 1, 0, alignment=Qt.AlignCenter)

#btn_receivables
btn_receivables = QPushButton("📊")
btn_receivables.setStyleSheet(btn_off)
btn_receivables.setFixedWidth(80)
btn_receivables.clicked.connect(on_receivables_click)
button_layout.addWidget(btn_receivables, 1, 1, alignment=Qt.AlignCenter)

#btn_waiting
btn_waiting = QPushButton("⏳")
btn_waiting.setStyleSheet(btn_off)
btn_waiting.setFixedWidth(80)
btn_waiting.clicked.connect(on_waiting_click)
button_layout.addWidget(btn_waiting, 2, 0, alignment=Qt.AlignCenter)

#btn_savings_debt
btn_savings_debt = QPushButton("💰")
btn_savings_debt.setStyleSheet(btn_off)
btn_savings_debt.setFixedWidth(80)
btn_savings_debt.clicked.connect(on_savings_debt_click)
button_layout.addWidget(btn_savings_debt, 2, 1, alignment=Qt.AlignCenter)

#btn_salaries
btn_salaries = QPushButton("👥")
btn_salaries.setStyleSheet(btn_off)
btn_salaries.setFixedWidth(80)
btn_salaries.clicked.connect(on_salaries_click)
button_layout.addWidget(btn_salaries, 3, 0, alignment=Qt.AlignCenter)

print("Buttons Created")


#btn_students
btn_students = QPushButton("🎓")
btn_students.setStyleSheet(btn_off)
btn_students.setFixedWidth(80)
btn_students.clicked.connect(on_students_click)
button_layout.addWidget(btn_students, 3, 1, alignment=Qt.AlignCenter)

#btn_cash_counter
btn_cash_counter = QPushButton("💵")
btn_cash_counter.setStyleSheet(btn_off)
btn_cash_counter.setFixedWidth(80)
btn_cash_counter.clicked.connect(on_cash_counter_click)
button_layout.addWidget(btn_cash_counter, 4, 0, alignment=Qt.AlignCenter)

#btn_settings
btn_settings = QPushButton("⚙️")
btn_settings.setStyleSheet(btn_off)
btn_settings.setFixedWidth(80)
btn_settings.clicked.connect(on_settings_click)
button_layout.addWidget(btn_settings, 4, 1, alignment=Qt.AlignCenter)

#btn_prices
btn_prices = QPushButton("🏷️")
btn_prices.setStyleSheet(btn_off)
btn_prices.setFixedWidth(80)
btn_prices.clicked.connect(on_prices_click)
button_layout.addWidget(btn_prices, 5, 0, alignment=Qt.AlignCenter)

#btn_running
btn_running = QPushButton("🏃")
btn_running.setStyleSheet(btn_off)
btn_running.setFixedWidth(80)
btn_running.clicked.connect(on_running_click)
button_layout.addWidget(btn_running, 5, 1, alignment=Qt.AlignCenter)

#btn_orders
btn_orders = QPushButton("📦")
btn_orders.setStyleSheet(btn_off)
btn_orders.setFixedWidth(80)
btn_orders.clicked.connect(on_orders_click)
button_layout.addWidget(btn_orders, 6, 0, alignment=Qt.AlignCenter)

#btn_tournament
btn_tournament = QPushButton("🏆")
btn_tournament.setStyleSheet(btn_off)
btn_tournament.setFixedWidth(80)
btn_tournament.clicked.connect(on_tournament_click)
button_layout.addWidget(btn_tournament, 6, 1, alignment=Qt.AlignCenter)

#btn_dashboard
btn_dashboard = QPushButton("📈")
btn_dashboard.setStyleSheet(btn_off)
btn_dashboard.setFixedWidth(180)
btn_dashboard.clicked.connect(on_dashboard_click)
button_layout.addWidget(btn_dashboard, 7, 0, alignment=Qt.AlignCenter)

left_panel_layout.addWidget(button_grid)

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


footer = QLabel("© 2026  Eng. Mostafa Donia. All rights reserved.")
footer.setStyleSheet(f"color: {colors['white']}; font-size: 12px;")
footer.setMaximumHeight(30)
main_layout.addWidget(footer, alignment=Qt.AlignCenter)

window.setCentralWidget(center)
window.showMaximized()   

app.exec()