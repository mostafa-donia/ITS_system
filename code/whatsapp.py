def prepare_phones(phones:str):
    table = str.maketrans("٠١٢٣٤٥٦٧٨٩","0123456789")
    phones = phones.translate(table)
    phones = list(phones)
    phone_list =""
    for i,c in enumerate(phones) :
        if c == "," and phones[i+1] == ",":
            phones.pop(i+1)
        phone_list+=(c)
    phone_list = phone_list.split(",")
    corrected_phone_list = []
    for i in phone_list :
        if len(i)>10 and len(i)<12 :
            corrected_phone_list.append(i)
        elif len(i)== 10 and i[0] == "1" :
            corrected_phone_list.append("0"+i)
        elif len(i)== 12 and i[0] =="2" :
            i = i.replace("2","",1)
            corrected_phone_list.append(i)
    return corrected_phone_list

def prepare_messages(messages:str):
    messages = list(messages)
    message_list =""
    for i,c in enumerate(messages) :
        if c == "," and messages[i+1] == ",":
            messages.pop(i+1)
        message_list+=(c)
    message_list = message_list.split(",")
    return message_list

def sending(phones:list,messages:list):
    if len(phones) == 0 or len(messages) == 0 :
        print("No phones or messages to send")
        return "No phones or messages to send"
    if len(phones) != len(messages) and len(messages) != 1:
        print("Number of phones and messages must be the same")
        return "Number of phones and messages must be the same"
    if len(messages) == 1 :
        message = messages[0]
        for phone in phones :
            print(f"Sending {message} to {phone}")
    else :
        for phone in phones :
            for message in messages :
                print(f"Sending {message} to {phone}")

if __name__ == "__main__":
    print(prepare_phones("01080922432,,201094832294,1097855504,,١٠٩٨٥٧٠٣٠٠"))
    print(prepare_messages("01080922432,,201094832294,1097855504,,١٠٩٨٥٧٠٣٠٠"))
    sending(prepare_phones("01080922432,,201094832294,1097855504,,١٠٩٨٥٧٠٣٠٠"), prepare_messages("01080922432,,201094832294,1097855504,,١٠٩٨٥٧٠٣٠٠"))



