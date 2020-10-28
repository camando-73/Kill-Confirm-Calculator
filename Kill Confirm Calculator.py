from tkinter import *
import PySimpleGUI as sg
window = Tk()
window.title("Kill Confirm Calculator")

global oppKilPer

promptLabel = Label(window, text="Select your Opponents Rival").grid(row=1, column=4)
promptLabel1 = Label(window, text="by clicking a Button").grid(row=2, column=4)

#Functions containing each characters different kill percent values
def zet():
     characterLabel = Label(window, text="You Chose: Zetterburn").grid(row=5, column=4)
     global oppKilPer
     oppKilPer = 118
def orc():
     characterLabel = Label(window, text="You Chose: Orcane").grid(row=5, column=4)
     global oppKilPer
     oppKilPer = 118
def fors():
     characterLabel = Label(window, text="You Chose: Forsburn").grid(row=5, column=4)
     global oppKilPer
     oppKilPer = 118
def eta():
     characterLabel = Label(window, text="You Chose: Etalus").grid(row=5, column=4)
     global oppKilPer
     oppKilPer = 133
def cla():
     characterLabel = Label(window, text="You Chose: Clairen").grid(row=5, column=4)
     global oppKilPer
     oppKilPer = 118
def ran():
     characterLabel = Label(window, text="You Chose: Ranno").grid(row=5, column=4)
     global oppKilPer
     oppKilPer = 112
def wra():
     characterLabel = Label(window, text="You Chose: Wrastor").grid(row=5, column=4)
     global oppKilPer
     oppKilPer = 88
def kra():
     characterLabel = Label(window, text="You Chose: Kragg").grid(row=5, column=4)
     global oppKilPer
     oppKilPer = 138
def absa():
     characterLabel = Label(window, text="You Chose: Absa").grid(row=5, column=4)
     global oppKilPer
     oppKilPer = 97
def may():
     characterLabel = Label(window, text="You Chose: Maypul").grid(row=5, column=4)
     global oppKilPer
     oppKilPer = 106
def ell():
     characterLabel = Label(window, text="You Chose: Ellianna").grid(row=5, column=4)
     global oppKilPer
     oppKilPer = 122
def syl():
     characterLabel = Label(window, text="You Chose: Sylvanos").grid(row=5, column=4)
     global oppKilPer
     oppKilPer = 127
def ori():
     characterLabel = Label(window, text="You Chose: Ori and Sein").grid(row=5, column=4)
     global oppKilPer
     oppKilPer = 101
def sho():
     characterLabel = Label(window, text="You Chose: Shovel Knight").grid(row=5, column=4)
     global oppKilPer
     oppKilPer = 125

#calculation of final percent
def calOppPer():
    try:
        percent = int(conOfPer.get())
    except ValueError:
         sg.Popup('Opps!', 'Must enter a whole number!')
        
    finOppPer = oppKilPer - percent
    if finOppPer <= 0:
        succLabel = Label(window, text="Kill Confirm Successful")
        succLabel.grid(row=10, column=4)
    else:
        succLabel = Label(window, text="Kill Confirm Unsucessful")
        succLabel.grid(row=10, column=4)

#individual character buttons for users to choose 
zetButton = Button(window, text="Zetterburn", command=zet)
zetButton.grid(row=2, column=3)
forsButton = Button(window, text="Forsburn", command=fors)
forsButton.grid(row=2, column=2)
claButton = Button(window, text="Clairen", command=cla)
claButton.grid(row=2, column=1)
orcButton = Button(window, text="Orcane", command=orc)
orcButton.grid(row=3, column=5)
etaButton = Button(window, text="Etalus", command=eta)
etaButton.grid(row=3, column=6)
ranButton = Button(window, text="Ranno", command=ran)
ranButton.grid(row=3, column=7)
wraButton = Button(window, text="Wrastor", command=wra)
wraButton.grid(row=2, column=5)
absaButton = Button(window, text="Absa", command=absa)
absaButton.grid(row=2, column=6)
ellButton = Button(window, text="Ellianna", command=ell)
ellButton.grid(row=2, column=7)
kraButton = Button(window, text="Kragg", command=kra)
kraButton.grid(row=3, column=3)
mayButton = Button(window, text="Maypul", command=may)
mayButton.grid(row=3, column=2)
sylButton = Button(window, text="Sylvanos", command=syl)
sylButton.grid(row=3, column=1)
oriButton = Button(window, text="Ori and Sein", command=ori)
oriButton.grid(row=4, column=3)
shoButton = Button(window, text="Shovel Knight", command=sho)
shoButton.grid(row=4, column=5)
#Entry widget for opponents percent 
oppPercentLabel = Label(window, text="Enter your Opponents Percent").grid(row=6,column=4)
conOfPer = StringVar()
entPercent = Entry(window, width=20, textvariable=conOfPer).grid(row=7, column=4)
   

#result button that will display if the kill confirm was succesful
submitButton = Button(window, text="Result", command=calOppPer).grid(row=9, column=4)

window.mainloop()
