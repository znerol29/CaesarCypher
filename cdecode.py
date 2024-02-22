import os
import sys
import easygui

position = 0
letter = 0
result = ""
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if len(sys.argv) > 2:
  if sys.argv[2].isnumeric():
    key = int(sys.argv[2])
else: 
  key = easygui.enterbox("Schlüssel")
  if key == None:
    os.system("python main.py")
  elif not key.isnumeric():
    raise ValueError("Key is not numeric.")
  key = int(key)

if len(sys.argv) > 1:
  if sys.argv[1].replace(' ', '').isalpha():
    input = sys.argv[1]
else: 
  input = easygui.textbox("Eingabe").upper()
  if input == None:
    os.system("python main.py")
  elif not input.replace(' ', '').isalpha():
    raise ValueError("Input is not made up of letters.")

for i in range(0, len(input)):
  nextletter = 0
  while True:
    nextletter = 0
    if input[position] == " ":
      result = result + " "
      nextletter = 1
    if input[position] == alphabet[letter]:
      if letter - key < 0:
        letter += 26
      result = result + alphabet[letter - key]
      nextletter = 1
    if nextletter == 1:
      break
    letter += 1
  if nextletter == 1:
    letter = 0
    position += 1

print(result)
action = easygui.buttonbox(('Dekodieren\nSchlüssel: ' + str(key) + '\n' + result), "Ergebnis", ["Ok", "Schlüssel ändern"])

if action == "Ok":
  os.system("python main.py")
elif action == "Schlüssel ändern":
  os.system("python cdecode.py " + input)