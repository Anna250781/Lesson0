def send_email(message, recipient, sender = "university.help@gmail.com"):
    my_list = ["@", ".com", ".ru", ".net"]
    for i in recipient:
        if i == my_list.index("@"):
            continue
    for j in sender:
        if j == my_list.index("@"):
            continue
    for i in my_list:
        if i == recipient.endswith(".com") or i == recipient.endswith(".ru") or i == recipient.endswith(".net"):
            continue
        if i == sender.endswith(".com") or i == sender.endswith(".ru") or i == sender.endswith(".net"):
            continue
        else:
            break
            print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient, ".")

    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    if sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient, ".")
    else:
        print( "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient, ".")



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

#Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com
#НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru
#Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
#Нельзя отправить письмо самому себе!