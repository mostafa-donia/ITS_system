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

print(prepare_phones("01080922432,,201094832294,1097855504,,١٠٩٨٥٧٠٣٠٠"))



