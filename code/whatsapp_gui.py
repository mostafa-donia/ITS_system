def create_whatsapp_page():
    page = QWidget()
    layout = QVBoxLayout(page)
    label = QLabel("WhatsApp Sender Page")
    label.setAlignment(Qt.AlignCenter)
    layout.addWidget(label)
    return page