from selfdrive.kegman_conf import kegman_conf
import subprocess
import os
BASEDIR = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../"))

letters = { "a":[ "###", "# #", "###", "# #", "# #"], "b":[ "###", "# #", "###", "# #", "###"], "c":[ "###", "#", "#", "#", "###"], "d":[ "##", "# #", "# #", "# #", "##"], "e":[ "###", "#", "###", "#", "###"], "f":[ "###", "#", "###", "#", "#"], "g":[ "###", "# #", "###", "  #", "###"], "h":[ "# #", "# #", "###", "# #", "# #"], "i":[ "###", " #", " #", " #", "###"], "j":[ "###", " #", " #", " #", "##"], "k":[ "# #", "##", "#", "##", "# #"], "l":[ "#", "#", "#", "#", "###"], "m":[ "# #", "###", "###", "# #", "# #"], "n":[ "###", "# #", "# #", "# #", "# #"], "o":[ "###", "# #", "# #", "# #", "###"], "p":[ "###", "# #", "###", "#", "#"], "q":[ "###", "# #", "###", "  #", "  #"], "r":[ "###", "# #", "##", "# #", "# #"], "s":[ "###", "#", "###", "  #", "###"], "t":[ "###", " #", " #", " #", " #"], "u":[ "# #", "# #", "# #", "# #", "###"], "v":[ "# #", "# #", "# #", "# #", " #"], "w":[ "# #", "# #", "# #", "###", "###"], "x":[ "# #", " #", " #", " #", "# #"], "y":[ "# #", "# #", "###", "  #", "###"], "z":[ "###", "  #", " #", "#", "###"], " ":[ " "], "1":[ " #", "##", " #", " #", "###"], "2":[ "###", "  #", "###", "#", "###"], "3":[ "###", "  #", "###", "  #", "###"], "4":[ "#", "#", "# #", "###", "  #"], "5":[ "###", "#", "###", "  #", "###"], "6":[ "###", "#", "###", "# #", "###"], "7":[ "###", "  # ", " #", " #", "#"], "8":[ "###", "# #", "###", "# #", "###"], "9":[ "###", "# #", "###", "  #", "###"], "0":[ "###", "# #", "# #", "# #", "###"], "!":[ " # ", " # ", " # ", "   ", " # "], "?":[ "###", "  #", " ##", "   ", " # "], ".":[ "   ", "   ", "   ", "   ", " # "], "]":[ "   ", "   ", "   ", "  #", " # "], "/":[ "  #", "  #", " # ", "# ", "# "], ":":[ "   ", " # ", "   ", " # ", "   "], "@":[ "###", "# #", "## ", "#  ", "###"], "'":[ " # ", " # ", "   ", "   ", "   "], "#":[ " # ", "###", " # ", "###", " # "], "-":[ "  ", "  ","###","   ","   "] }
# letters stolen from here: http://www.stuffaboutcode.com/2013/08/raspberry-pi-minecraft-twitter.html

def print_letters(text):
    bigletters = []
    for i in text:
        bigletters.append(letters.get(i.lower(),letters[' ']))
    output = ['']*5
    for i in range(5):
        for j in bigletters:
            temp = ' '
            try:
                temp = j[i]
            except:
                pass
            temp += ' '*(5-len(temp))
            temp = temp.replace(' ',' ')
            temp = temp.replace('#','@')
            output[i] += temp
    return '\n'.join(output)
import sys, termios, tty, os, time

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

button_delay = 0.2

kegman = kegman_conf()
kegman.conf['tuneGernby'] = "1"
#kegman.write_config(kegman.conf)
param = ["cameraOffset", "Kp", "Ki", "Kf", "Kp2", "Ki2", "Kf2", "steerRatio", "steerRateCost", \
         "sR_boost", "sR_BP0", "sR_BP1", "sR_time", \
         "sR_Kp", "sR_Ki", "sR_Kf", \
         "sR_Kp2", "sR_Ki2", "sR_Kf2"]

j = 0
while True:
  print ("")
  print (print_letters(param[j][0:9]))
  print ("")
  print (print_letters(kegman.conf[param[j]]))
  print ("")
  print ("w: +1   1: +0.1   3: +0.05   5: +0.01   7: +0.001   r: +0.00001")
  print ("x: -1   a: -0.1   d: -0.05   g: -0.01   j: -0.001   v: -0.00001")
#  print ("w,1,3,5,7,r to incr 1,0.1,0.05,0.01,0.001,0.00001")
#  print ("x,a,d,g,j,v to decr 1,0.1,0.05,0.01,0.001,0.00001")
  print ("0: 0   L: 1")
#  print ("0 / L to make the value 0 / 1")
  print ("SPACE: next   m: prev")
  print ("z: quit")
  print ("p: reboot")

  char  = getch()
  write_json = False
  if (char == "v"):
    kegman.conf[param[j]] = str(round((float(kegman.conf[param[j]]) - 0.00001),5))
    write_json = True

  if (char == "r"):
    kegman.conf[param[j]] = str(round((float(kegman.conf[param[j]]) + 0.00001),5))
    write_json = True
    
  if (char == "7"):
    kegman.conf[param[j]] = str(round((float(kegman.conf[param[j]]) + 0.001),5))
    write_json = True

  if (char == "5"):
    kegman.conf[param[j]] = str(round((float(kegman.conf[param[j]]) + 0.01),5))
    write_json = True

  elif (char == "3"):
    kegman.conf[param[j]] = str(round((float(kegman.conf[param[j]]) + 0.05),5))
    write_json = True

  elif (char == "1"):
    kegman.conf[param[j]] = str(round((float(kegman.conf[param[j]]) + 0.1),5))
    write_json = True

  elif (char == "w"):
    kegman.conf[param[j]] = str(round((float(kegman.conf[param[j]]) + 1),5))
    write_json = True

  elif (char == "j"):
    kegman.conf[param[j]] = str(round((float(kegman.conf[param[j]]) - 0.001),5))
    write_json = True

  elif (char == "g"):
    kegman.conf[param[j]] = str(round((float(kegman.conf[param[j]]) - 0.01),5))
    write_json = True

  elif (char == "d"):
    kegman.conf[param[j]] = str(round((float(kegman.conf[param[j]]) - 0.05),5))
    write_json = True

  elif (char == "a"):
    kegman.conf[param[j]] = str(round((float(kegman.conf[param[j]]) - 0.1),5))
    write_json = True

  elif (char == "x"):
    kegman.conf[param[j]] = str(round((float(kegman.conf[param[j]]) - 1),5))
    write_json = True

  elif (char == "0"):
    kegman.conf[param[j]] = "0"
    write_json = True

  elif (char == "l"):
    kegman.conf[param[j]] = "1"
    write_json = True

  elif (char == " "):
    if j < len(param) - 1:
      j = j + 1
    else:
      j = 0

  elif (char == "m"):
    if j > 0:
      j = j - 1
    else:
      j = len(param) - 1

  elif (char == "p"):
    print ("")
    print ("system will reboot. continue?(y/n)")
    char2 = getch()
    if (char2 == "y"):
      os.system('LD_LIBRARY_PATH="" svc power reboot')
    else:
      process.kill()

  elif (char == "z"):
    process.kill()
    break


  if float(kegman.conf['tuneGernby']) != 1 and float(kegman.conf['tuneGernby']) != 0:
    kegman.conf['tuneGernby'] = "1"


  if float(kegman.conf['Ki']) < 0 and float(kegman.conf['Ki']) != -1:
    kegman.conf['Ki'] = "0"

  if float(kegman.conf['Ki']) > 2:
    kegman.conf['Ki'] = "2"

  if float(kegman.conf['Ki2']) < 0 and float(kegman.conf['Ki2']) != -1:
    kegman.conf['Ki2'] = "0"

  if float(kegman.conf['Ki2']) > 2:
    kegman.conf['Ki2'] = "2"    

  if float(kegman.conf['Kp']) < 0 and float(kegman.conf['Kp']) != -1:
    kegman.conf['Kp'] = "0"

  if float(kegman.conf['Kp']) > 3:
    kegman.conf['Kp'] = "3"

  if float(kegman.conf['Kp2']) < 0 and float(kegman.conf['Kp2']) != -1:
    kegman.conf['Kp2'] = "0"

  if float(kegman.conf['Kp2']) > 3:
    kegman.conf['Kp2'] = "3"    

  if float(kegman.conf['Kf']) > 0.01:
    kegman.conf['Kf'] = "0.01"    
    
  if float(kegman.conf['Kf']) < 0:
    kegman.conf['Kf'] = "0"

  if float(kegman.conf['Kf2']) > 0.01:
    kegman.conf['Kf2'] = "0.01"    
    
  if float(kegman.conf['Kf2']) < 0:
    kegman.conf['Kf2'] = "0"
      

  if float(kegman.conf['sR_Kp']) < 0:
    kegman.conf['sR_Kp'] = "0" 

  if float(kegman.conf['sR_Kp']) > 3:
    kegman.conf['sR_Kp'] = "3"

  if float(kegman.conf['sR_Kp2']) < 0:
    kegman.conf['sR_Kp2'] = "0" 

  if float(kegman.conf['sR_Kp2']) > 3:
    kegman.conf['sR_Kp2'] = "3"    

  if float(kegman.conf['sR_Ki']) < 0:
    kegman.conf['sR_Ki'] = "0" 

  if float(kegman.conf['sR_Ki']) > 2:
    kegman.conf['sR_Ki'] = "2"  

  if float(kegman.conf['sR_Ki2']) < 0:
    kegman.conf['sR_Ki2'] = "0" 

  if float(kegman.conf['sR_Ki2']) > 2:
    kegman.conf['sR_Ki2'] = "2"      

  if float(kegman.conf['sR_Kf']) > 0.01:
    kegman.conf['sR_Kf'] = "0.01"    
    
  if float(kegman.conf['sR_Kf']) < 0:
    kegman.conf['sR_Kf'] = "0"    

  if float(kegman.conf['sR_Kf2']) > 0.01:
    kegman.conf['sR_Kf2'] = "0.01"    
    
  if float(kegman.conf['sR_Kf2']) < 0:
    kegman.conf['sR_Kf2'] = "0"


  if float(kegman.conf['steerRatio']) < 1 and float(kegman.conf['steerRatio']) != -1:
    kegman.conf['steerRatio'] = "1"
    
  if float(kegman.conf['steerRateCost']) < 0.01 and float(kegman.conf['steerRateCost']) != -1:
    kegman.conf['steerRateCost'] = "0.01"
    
  if float(kegman.conf['deadzone']) < 0:
    kegman.conf['deadzone'] = "0"

  if float(kegman.conf['sR_boost']) < 0:
    kegman.conf['sR_boost'] = "0"
    
  if float(kegman.conf['sR_BP0']) < 0:
    kegman.conf['sR_BP0'] = "0"
    
  if float(kegman.conf['sR_BP1']) < 0:
    kegman.conf['sR_BP1'] = "0"
    
  if float(kegman.conf['sR_time']) < 0.1:
    kegman.conf['sR_time'] = "0.1"

  #if float(kegman.conf['Kf']) < 0.00001:
  kegman.conf['Kf'] = str("{:.5f}".format(float(kegman.conf['Kf'])))
  kegman.conf['Kf2'] = str("{:.5f}".format(float(kegman.conf['Kf2'])))
  kegman.conf['sR_Kf'] = str("{:.5f}".format(float(kegman.conf['sR_Kf'])))
  kegman.conf['sR_Kf2'] = str("{:.5f}".format(float(kegman.conf['sR_Kf2'])))
  


  if write_json:
    kegman.write_config(kegman.conf)

  time.sleep(button_delay)

else:
  process.kill()