import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    sen = input("Input: ")
    f = random.choice(fonts)
    figlet.setFont(font=f)
    print(figlet.renderText(sen))
elif (len(sys.argv) == 3) and (sys.argv[1] in ['-f', '--font']) and (sys.argv[2] in fonts):
    sen = input("Input: ")
    f = sys.argv[2]
    figlet.setFont(font=f)
    print(figlet.renderText(sen))
else:
    sys.exit("Invalid usage")

