import os
import easygui

letter = -1
position = -1
nextletter = 0
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

lettercount = []
for i in range(0, len(alphabet)):
  lettercount.extend([0])
  
letterfrequency = [
  6.51, 
  1.89, 
  3.06, 
  5.08, 
  17.4,
  1.66,
  3.01,
  4.76,
  7.55,
  0.27,
  1.21,
  3.44,
  2.53,
  9.78,
  2.51,
  0.79,
  0.02,
  7,
  7.27,
  0.31,
  6.15,
  4.35,
  0.67,
  1.89,
  0.03,
  0.04,
  1.13
]

input = easygui.textbox("Eingabe").upper()

for i in range(0, len(input)):
  nextletter = 0
  while True:
    nextletter = 0
    if input[position] == " ":
      nextletter = 1
    if input[position] == alphabet[letter]:
      lettercount[letter] = lettercount[letter] + 1
      nextletter = 1
    if nextletter == 1:
      break
    letter += 1
  if nextletter == 1:
    letter = 0
    position += 1

frequency = []
highest = 0
key = 0
for i in range(0, len(alphabet)):
  frequency.extend([round(lettercount[letter] / sum(lettercount) * 100, 2)])
  if round(lettercount[letter] / sum(lettercount) * 100, 2) > highest:
    highest = letter
  letter += 1
letter = 0
key = highest - 4

result = []
for i in range(0, len(alphabet)):
  result.extend(alphabet[letter] + " = " + str(lettercount[letter]) + "    " + str(frequency[letter]) + "/" + str(letterfrequency[letter]) + '\n')
  print(alphabet[letter] + " = " + str(lettercount[letter]))
  letter +=1
letter = 0

action = easygui.buttonbox(("Häufigkeitsanalyse\n" + ''.join(result) + "\nVorgeschlagener Schlüssel: " + str(key)), "Ergebnis", ["Ok", "Schlüssel anwenden"])

if action == "Ok":
  os.system("python main.py")
elif action == "Schlüssel anwenden":
  os.system("python cdecode.py " + input + " " + str(key))