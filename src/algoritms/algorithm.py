amount_letters = []
size = 1
vision_score = 1
gstay = 0
bstay = 0

while size <= 8:
    answers = input('whasd')
    if answers == "yee":
        amount_letters.append("User got it ")
        if gstay == 4:
            size = size + 1
            vision_score = vision_score+1
        else:
            gstay = gstay+1
            bstay = 0
    elif answers == "non":
        amount_letters.append("User didn't get it ")
        if bstay == 4:
            break
        else:
            bstay = bstay+1
            gstay = 0
    elif answers == "stop":
        break
    else:
        print('try again')
