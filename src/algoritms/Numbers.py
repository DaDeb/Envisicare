
import random
from algorithm import amount_letters
direction = [1]
store_letter = []
for i in range(len(amount_letters)):
    direction.append(random.randrange(1, 5))

for c in range(len(direction)):
   if direction[c] == 1:
    store_letter.append("E")
   elif direction[c] == 2:
    store_letter.append("Ǝ")
   elif direction[c] == 3:
    store_letter.append("m")
   else:
    store_letter.append("ɯ")
print(store_letter)
