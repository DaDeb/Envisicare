from algorithm import vision_score
final_score= 0
if vision_score == 1:
    final_score = "20/200"
elif vision_score == 2:
    final_score = "20/100"
elif vision_score == 3:
    final_score = "20/70"
elif vision_score == 4:
    final_score = "20/50"
elif vision_score == 5:
    final_score = "20/40"
elif vision_score == 6:
    final_score = "20/30"
elif vision_score == 7:
    final_score = "20/25"
else:
    final_score = "20/20"
print(final_score)