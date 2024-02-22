import os
import easygui

print("Ready")

type = easygui.buttonbox("Aktion auswählen:", "Aktion", ["Cäsar", "Skytale", "Häufigkeitsanalyse", "Beenden"])

if type == "Cäsar":
  action = easygui.buttonbox("Aktion auswählen:", "Aktion", ["Dekodieren", "Enkodieren", "Cancel"])
    
  if action == "Dekodieren":
    print("Decode")
    os.system("python cdecode.py")
    
  elif action == "Enkodieren":
    print("Encode")
    os.system('python cencode.py')

  elif action == "Cancel":
    os.system('python main.py')
 
elif type == "Skytale":
  action = easygui.buttonbox("Aktion auswählen:", "Aktion", ["Dekodieren", "Enkodieren", "Cancel"])

  if action == "Dekodieren":
    print("Decode")
    os.system("python ddecode.py")
    
  elif action == "Enkodieren":
    print("Encode")
    os.system('python dencode.py')

  elif action == "Cancel":
    os.system('python main.py')

elif type == "Häufigkeitsanalyse":
  print("Frequency")
  os.system("python frequency.py")

elif type == "Beenden":
  exit
