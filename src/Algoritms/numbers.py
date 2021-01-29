import math
import random
direction = []
store_letter = []
for i in range(0, 11):
    direction.append(random.randrange(1, 5))
    print(direction)

for c in range(0, 11):
   if direction[c]== 1:
       store_letter.append("E")
   elif direction[c]== 2:
       store_letter.append("Ǝ")
   elif direction[c]== 3:
       store_letter.append("m")
   else:
        store_letter.append("ɯ")
print(store_letter)
