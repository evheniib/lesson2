def ask_user():
    quation = ""
    while quation != "Хорошо":
        quation = input("Как дела? \n")
    
    chat_dict = {
        "Как дела?": "Хорошо!",
        "Что делаешь?": "Программирую"
    }
    chat_keys = list(chat_dict.keys())
    
    quation = input("Спроси меня \n") 
    key = 0
    while key <= len(chat_keys):
        try:
            if quation == chat_keys[key]:
                print(chat_dict[quation])
                quation = input("Хочешь спросить что-то еще? \n")
                key = 0 
            else:
                key = key + 1
        except KeyboardInterrupt:
            print("Пока")
            break  


ask_user()


