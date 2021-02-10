from Numbers import store_letter
from Numbers import direction
import numpy
intext_displayer = ["Swipe any way",
        "The pupose of this test is to determine your eye power.",
        "To meet the purpose of this test you need to follow the specified instructions",
        "1. You will see an E shapped letter",
        "2. Upon seeing this E shaped object you need to determine the direction the open ended side of the letter is facing",
        "3. Slide the card to the direction of the open ended side",
        "For example you see M you have to slide the card downward",
        "Now give it a try, Which way do you slide the next card",
        "E",
        "Ǝ",
        "m",
        ]
for i in range(len(store_letter)):
    intext_displayer.append(store_letter[i-1])
print(intext_displayer)





