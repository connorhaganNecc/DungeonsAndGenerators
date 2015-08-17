#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

In this script, we use pack manager
to position two buttons in the
bottom right corner of the window. 

author: Jan Bodnar
last modified: December 2010
website: www.zetcode.com
"""

import random
from Tkinter import *
from ttk import Frame, Button, Style


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()


    def generateNPC(self) :
        random.seed()
        self.text.delete('1.0', END)
        tempInt = random.randrange(1, 100)
        tempString = ""
        if(tempInt <=5):
            tempString = "Achievement: To overcome obstacles and succeed; to become the best"
        if(tempInt>=6):
            if(tempInt<=10):
                tempString = "Aquisition: To obtain possessions/wealth"
        if(tempInt>=11):
            if(tempInt<=15):
                tempString = "Balace/Pease: To bring all things into harmony and equilibrium"
        if(tempInt>=16):
            if(tempInt<=20):
                tempString = "Beneficence: To protect the helpless, heal the sick, feed the hungry, etc."
        if(tempInt>=16):
            if(tempInt<=20):
                tempString = "Beneficence: To protect the helpless, heal the sick, feed the hungry, etc."
        if(tempInt>=21):
            if(tempInt<=25):
                tempString = "Chaos: To disrupt, to cause confusion and discord."
        if(tempInt>=26):
            if(tempInt<=30):
                tempString = "Creation: To build or make new, such as art, culture, invention, design,etc.."
        if(tempInt>=31):
            if(tempInt<=35):
                tempString = "Destruction: To annihilate, exterminate, unmake, and bring to ruin."
        if(tempInt>=36):
            if(tempInt<=40):
                tempString = "Discovery/Adventure: To explore, uncover mysteries, and pioneer."
        if(tempInt>=41):
            if(tempInt<=45):
                tempString = "Education: To provide information, teach, enlighten, or train"
        if(tempInt>=46):
            if(tempInt<=50):
                tempString = "Enslavement: To provide information, teach, enlighten, or train"
        if(tempInt>=51):
            if(tempInt<=55):
                tempString = "Hedoinism: To enjoy all things sensuous"
        if(tempInt>=51):
            if(tempInt<=55):
                tempString = "Liberation: To free the self and/or others from perceived captivity or enslavement"
        if(tempInt>=56):
            if(tempInt<=60):
                tempString = "Nobility/Honor: To exalt ideals such as generosity, honesty, bravery, and courtliness"
        if(tempInt>=61):
            if(tempInt<=65):
                tempString = "Order: To arrange, organize, and reduce chaos"
        if(tempInt>=66):
            if(tempInt<=70):
                tempString = "Play: To have fun, to enjoy life"
        if(tempInt>=71):
            if(tempInt<=75):
                tempString = "Power: To control and lead others"
        if(tempInt>=76):
            if(tempInt<=80):
                tempString = "Recognition: To gain approval, social status, or fame"
        if(tempInt>=81):
            if(tempInt<=85):
                tempString = "Service: To follow a person, government, order, religion, etc."
        if(tempInt>=86):
            if(tempInt<=90):
                tempString = "Torment: To inflict pain and suffering, on others and/or the self"
        if(tempInt>=91):
            if(tempInt<=95):
                tempString = "Understanding: To seek knowledge or wisdom (spiritual, scientific, magical,etc)"
        if(tempInt>=96):
            if(tempInt<=100):
                tempString = "Rebellion: to act out against or contrary to any and all forms of authority"

        self.text.insert(END,"Primary Motivator: ")
        self.text.insert(END, tempString)
        self.text.insert(END, "\n")
        self.text.insert(END, "\n")

        self.text.insert(END,"Core Traits")
        self.text.insert(END, "\n")

        tempInt = random.randrange(1, 100)
        if(tempInt>=1):
            if(tempInt<=10):
                tempString = "Joyful"
        if(tempInt>=11):
            if(tempInt<=20):
                tempString = "Anxious"
        if(tempInt>=21):
            if(tempInt<=30):
                tempString = "Melancholy"
        if(tempInt>=31):
            if(tempInt<=40):
                tempString = "Curious"
        if(tempInt>=41):
            if(tempInt<=50):
                tempString = "Calm"
        if(tempInt>=51):
            if(tempInt<=60):
                tempString = "Angry"
        if(tempInt>=61):
            if(tempInt<=70):
                tempString = "Contemptuous"
        if(tempInt>=71):
            if(tempInt<=80):
                tempString = "Excited"
        if(tempInt>=81):
            if(tempInt<=90):
                tempString = "Apathetic"
        if(tempInt>=91):
            if(tempInt<=100):
                tempString = "Ashamed"

        self.text.insert(END,"Emotional Disposition: ")
        self.text.insert(END, tempString)
        self.text.insert(END, "\n")

        tempInt = random.randrange(1, 100)
        if(tempInt <= 33):
            tempString = "Unstable, prone to extreme emotions"
        if(tempInt >= 34):
            if(tempInt <= 66):
                tempString = "Even-Tempered"
        if(tempInt >=67):
            tempString = "Unemotional"

        self.text.insert(END,"Moodiness: ")
        self.text.insert(END, tempString)
        self.text.insert(END, "\n")

        random.seed()
        tempInt = random.randrange(1, 3)
        if(tempInt == 1):
            tempString = "Optimistic: idealistic, confident, trusting, hopeful, upbeat"
        if(tempInt == 2):
            tempString = "Pessimistic: cynical, bleak, distrustful, foreboding, resigned"

        self.text.insert(END,"Outlook: ")
        self.text.insert(END, tempString)
        self.text.insert(END, "\n")

        random.seed()
        tempInt = random.randrange(1, 3)
        if(tempInt == 1):
            tempString = "Conscientious: industrious, honest, responsible, meticulous, pragmatic"
        if(tempInt == 2):
            tempString = "Unscrupulous: lazy, deceitful, unreliable, manipulative, slipshod, impractical"

        self.text.insert(END,"Integrity: ")
        self.text.insert(END, tempString)
        self.text.insert(END, "\n")

        random.seed()
        tempInt = random.randrange(1, 3)
        if(tempInt == 1):
            tempString = "Controlled: deliberate, focused, steady, thoughtful"
        if(tempInt == 2):
            tempString = "Spontaneous: capricious, flighty, hyperactive, rash"

        self.text.insert(END,"Impulsiveness: ")
        self.text.insert(END, tempString)
        self.text.insert(END, "\n")

        random.seed()
        tempInt = random.randrange(1, 3)
        if(tempInt == 1):
            tempString = "Intrepid: daring, reckless, chivalrous"
        if(tempInt == 2):
            tempString = "Cautious: timid, paranoid, vigilant"

        self.text.insert(END,"Boldness: ")
        self.text.insert(END, tempString)
        self.text.insert(END, "\n")


        random.seed()
        tempInt = random.randrange(1, 3)
        if(tempInt == 1):
            tempString = "Flexible: nonchalant, tolerant, forgiving, open-minded, adaptable"
        if(tempInt == 2):
            tempString = "Stubborn: rigid, tense, relentless, intractable, narrow-minded"

        self.text.insert(END,"Flexibility: ")
        self.text.insert(END, tempString)
        self.text.insert(END, "\n")

        random.seed()
        tempInt = random.randrange(1, 3)
        if(tempInt == 1):
            tempString = "Warm: altruistic, nurturing, empathic, supportiveble"
        if(tempInt == 2):
            tempString = "Cold: self absorbed, needy, greedy, stingy, uncaring"

        self.text.insert(END,"Affinity: ")
        self.text.insert(END, tempString)
        self.text.insert(END, "\n")

        random.seed()
        tempInt = random.randrange(1, 3)
        if(tempInt == 1):
            tempString = "Agreeable: courteous, cultured, modest, charming, humorous"
        if(tempInt == 2):
            tempString = "Discordant: gruff, critical, arrogant, crude, defensive, sanctimonious"

        self.text.insert(END,"Comportment: ")
        self.text.insert(END, tempString)
        self.text.insert(END, "\n")

        random.seed()
        tempInt = random.randrange(1, 3)
        if(tempInt == 1):
            tempString = "Engaging: talkative, listener, entertaining, touchy"
        if(tempInt == 2):
            tempString = "Reserved: shy, loner, taciturn"

        self.text.insert(END,"Interactivity: ")
        self.text.insert(END, tempString)
        self.text.insert(END, "\n")

        random.seed()
        tempInt = random.randrange(1, 3)
        if(tempInt == 1):
            tempString = "Candid: open book, unreserved, frank"
        if(tempInt == 2):
            tempString = "Secretive: closed, mysterious, evasive, cryptic"

        self.text.insert(END,"Disclosure: ")
        self.text.insert(END, tempString)
        self.text.insert(END, "\n")

        random.seed()
        tempInt = random.randrange(1, 3)
        if(tempInt == 1):
            tempString = "Conventional: orthodox, formal, down-to-earth, mainstream, traditional"
        if(tempInt == 2):
            tempString = "Heterodox: rebellious, arty, shocking, freethinking, exotic"

        self.text.insert(END,"Conformity: ")
        self.text.insert(END, tempString)
        self.text.insert(END, "\n")
        self.text.insert(END, "\n")

        self.text.insert(END,"Secondary Traits: ")
        self.text.insert(END, "\n")

        tempInt = random.randrange(1, 100)
        if(tempInt>=1):
            if(tempInt<=10):
                tempString = "Crude"
        if(tempInt>=11):
            if(tempInt<=20):
                tempString = "Dry"
        if(tempInt>=21):
            if(tempInt<=30):
                tempString = "Slapstick"
        if(tempInt>=31):
            if(tempInt<=40):
                tempString = "Jokery"
        if(tempInt>=41):
            if(tempInt<=50):
                tempString = "Cynical"
        if(tempInt>=51):
            if(tempInt<=60):
                tempString = "Pranks"
        if(tempInt>=61):
            if(tempInt<=70):
                tempString = "Mean-Spirited"
        if(tempInt>=71):
            if(tempInt<=80):
                tempString = "Gleeful"
        if(tempInt>=81):
            if(tempInt<=90):
                tempString = "Sureal"
        if(tempInt>=91):
            if(tempInt<=100):
                tempString = "None"

        self.text.insert(END,"Sense of Humor: ")
        self.text.insert(END, tempString)
        self.text.insert(END, "\n")
        self.text.insert(END, "\n")

        self.text.insert(END,"Religion")
        self.text.insert(END, "\n")

        tempInt = random.randrange(1, 100)
        if(tempInt>=1):
            if(tempInt<=25):
                tempString = "Atheist"
        if(tempInt>=26):
            if(tempInt<=50):
                tempString = "Agnostic"
        if(tempInt>=51):
            if(tempInt<=75):
                tempString = "Casual Adherant"
        if(tempInt>=76):
            if(tempInt<=100):
                tempString = "Orthodox Adherant"

        self.text.insert(END,"Adherence: ")
        self.text.insert(END, tempString)
        self.text.insert(END, "\n")

        tempInt = random.randrange(1, 100)
        if(tempInt <= 33):
            tempString = "Inclusive"
        if(tempInt >= 34):
            if(tempInt <= 66):
                tempString = "Tolerant"
        if(tempInt >=67):
            tempString = "Intolerant"

        self.text.insert(END,"Tolerance: ")
        self.text.insert(END, tempString)
        self.text.insert(END, "\n")

        tempInt = random.randrange(1, 100)
        if(tempInt <= 33):
            tempString = "None"
        if(tempInt >= 34):
            if(tempInt <= 66):
                tempString = "Occasional"
        if(tempInt >=67):
            tempString = "Constant"

        self.text.insert(END,"Expression of beliefs: ")
        self.text.insert(END, tempString)
        self.text.insert(END, "\n")

        tempInt = random.randrange(1, 100)
        if(tempInt <= 33):
            tempString = "Never"
        if(tempInt >= 34):
            if(tempInt <= 66):
                tempString = "Casual"
        if(tempInt >=67):
            tempString = "Aggressive"

        self.text.insert(END,"Converting Others: ")
        self.text.insert(END, tempString)
        self.text.insert(END, "\n")


    def initUI(self):

        self.parent.title("Buttons")
        self.style = Style()
        self.style.theme_use("default")

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack()

        frame2 = Frame(self, relief= RAISED, borderwidth = 5)
        frame2.pack(fill=BOTH, expand=1)



        self.pack(fill=BOTH, expand=1)

        generateButton = Button(frame, text="Generate", command=self.generateNPC)
        generateButton.pack()

        self.text = Text(frame2, padx = 5, height = 50)
        self.text.pack(fill=BOTH)

        closeButton = Button(self, text="Close")
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="OK")
        okButton.pack(side=RIGHT)



              

def main():
  
    root = Tk()
    root.geometry("300x200+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  