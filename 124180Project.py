from sys import *
from graphics import *
from random import *
import webbrowser

# 124180 May 17th
# Using Q2 knowledge to learn about proteins
# and using fuctions to present that information

def getCounts(sequence):
#seperating sequence by nuecleotides
    countA= (sequence.count('A'))
    countC= (sequence.count('C'))
    countG= (sequence.count('G'))
    countT= (sequence.count('T'))
    characters= [countA,countC,countG,countT]
    return characters

def getTotalMass(characters,junkCount):
    #putting mass of nucleotides in a list
    massA= round((characters[0])*135.128,2)
    massC= round((characters[1])*111.103,2)
    massG= round((characters[2])*151.128,2)
    massT= round((characters[3])*125.107,2)
    massJunk= round((junkCount)*100,2)
    
    massList= [massA,massC,massG,massT,massJunk]
    return massList

def getPercentages(characters,totalMass):
    #putting percent mass of nucleotides in a list
    perA= round((((characters[0])*135.128)/totalMass)*100,1)
    perC= round((((characters[1])*111.103)/totalMass)*100,1)
    perG= round((((characters[2])*151.128)/totalMass)*100,1)
    perT= round((((characters[3])*125.107)/totalMass)*100,1)
    perList = [perA,perC,perG,perT]
    return perList

def getCodons(sequence):
    #to seperate sequences by 3 letters so codons are made
    codonList=[]
    for i in range(0,len(sequence),3):
        codonList.append(sequence[i:i+3])
    return codonList

def is_protein(codons, percentages):
    #to see if sequence encodes a protein
    if codons[0]=='ATG' and (codons[-1]== 'TAA' or codons[-1]=='TAG' or codons[-1]=='TGA')and len(codons) >= 5 and (percentages[1]+percentages[3])>= 30:
        return True
    else:
        return False
    
def randomColor():
    #using random function for graph later on
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    color = color_rgb(r,g,b)
    return color

def drawGraph(mainList):
    color=[randomColor(),randomColor(),randomColor(),randomColor()]
    widthWin= (len(mainList)*60)
    #title bar
    win=GraphWin("Mass Percentage vs. Nucleotides "+inputFile, widthWin, 500)
    win.setCoords(0,0,widthWin,500)
    #name of graph
    txt=(Text(Point((widthWin-10)/2,480), "Mass Percentage vs. Nucleotides"))
    txt.draw(win)
    #drawing axises
    xAxis=Line(Point(50,50), Point((widthWin)-50,50))
    xAxis.setWidth(5)
    xAxis.draw(win)

    yAxis=Line(Point(50,50), Point(50,450))
    yAxis.setWidth(5)
    yAxis.draw(win)
    
    #loop for length of window so it works with multiple sequence files
    x=30
    y=50
    for num in range(0,51,10):
        line = Line(Point(50,y), Point((widthWin)-50,y))
        line.draw(win)
        label=Text(Point(x,y), str(num))
        label.draw(win)
        y+=70

    x=80
    y=50
    i=0
    j=0
    #loop for bar lengths measured by percent of each nucleotide in a sequence
    for perList in mainList: 
        for percent in perList:
            barOne= Rectangle(Point(x,y), Point(x+10,float(percent)*7+50))
            barOne.setFill(color[j])
            barOne.draw(win)
            j+=1
            x+=10
        x+=10
        i+=1
        j=0
        #labels on x axis
        label= Text(Point(x-30,30),"S"+str(i))
        label.draw(win)
        win.setBackground(randomColor())
    #to close with mouse   
    win.getMouse()
    win.close()

def printResults(name, sequence, characters, massList, perList, codons, protein, fileOut):
#line by line file showing previous functions
    name += "\n"
    sequence += "\n"
    fileOut.write(name)
    fileOut.write(sequence)
    fileOut.write(str(characters))
    fileOut.write("\n")
    fileOut.write(str(massList))
    fileOut.write("\n")
    fileOut.write(str(perList))
    fileOut.write("\n")
    fileOut.write(str(codons))
    fileOut.write("\n")
    fileOut.write(str(protein))
    fileOut.write("\n")

#printing a page
def customPage():
    f=open("summary.html","w")
    #user input to customize page
    backColor= input("Give me background color: ")
    fontColor= input('Give me a font color: ')
    fontSize= int(input('Give me a font size in px: '))
    imgH= fontSize*(5)
    fontType= input('Give me a font type: ')
    #to code html in python
    #using user input to dynamically code page
    #not hardcoding height
    message= """<!DOCTYPE html>
<html>
<head>
<title> DNA </title>
<style>
body {{background-image: linear-gradient(to right, {0} , {1}); color:{1}; font-size:{2}px; font-family:{3}; text-align: center;}}
img {{height:500px; width:500px;}}
h1 {{font-size:{2}+30}}
img.left {{float: left; width: {4}px; height: {4}px;}}
img.right {{float: right; width: {4}px; height: {4}px;}}
#header {{height: (30*40)px; background-color: white; text-align: center; margin:auto;}}
#words {{width:90%; height: ({2}*500)px; margin: auto; padding: 10px; background-color: white;}}
#graph {{width: 1200px; height: 500px; border: 8px solid white; margin:15px auto auto auto; padding: 10px;}}
</style>
</head>
<body>

<div id= "header">
<h1> Sequences </h1>
</div>

<div id= "words">

<a href= "https://medlineplus.gov/genetics/understanding/howgeneswork/protein/#:~:text=Proteins%20are%20large%2C%20complex%20molecules,the%20body's%20tissues%20and%20organs." target="_blank">
<img src = "protein.jpg" alt= "protein" class= "left">
</a>

<a href= "https://www.sciencedirect.com/topics/neuroscience/dna-strand" target="_blank">
<img src = "strand.jpg" alt= "strand" class= "right">
</a>

<p> DNA, Deoxyribonucleic acid, is quite literally the foundation of all life. It is made out of three nucleotides; Adenine, Cystosine,
Guanine, and Thymine. Most sequences of these encode proteins if they have the right requirements of their codons. For example, proteins have
codons that start with ATG, end in TAA, TAG, or TGA, are at least 5 codons in length, and Cytosine and Guanine account for 30% or more of the
total mass. Not only do codons have form proteins they also aid in medical research in
<a href = "https://youtu.be/4VThNjOBPNA" target="_blank"> AIDS and chemotherapy. </a>
Understanding sequences helps us
understand biology and the fundamentals of life.
</p>
</div>

<div id= "graph">
<img src="dnaGraph.png">
<img src="ecoliGraph.png">
</div>

</body>
</html>""".format(backColor, fontColor, fontSize, fontType, imgH)
    f.write(message)
    f.close()
    #from webbrowser module to open new tab
    webbrowser.open_new_tab("summary.html")


def main():
    print("This program reports information about DNA nucleotide sequences that may encode proteins")
    ans=input("do you want to run my program? y/n: ").lower()
    #using while loop to print user inputted information from file
    while ans[0] == 'y':
        #sets global variable so title bar of graph can have input file
        global inputFile
        #user input
        inputFile= input("Input File name? ")
        outputFile =input("Output File name? ")
        file= open(inputFile, "r")
        #for writing a file in getResults()
        fileOut = open(outputFile, "a")
        #to read the sequences not the lines
        lines = file.read().split("\n")
        mainList=[]
        #loop for reading all lines in a file
        for i in range(0,len(lines)-1,2):
            #so lines of names are read
            name = lines[i]
            #so sequences are read
            sequence = lines[i+1].upper()
            #to seperate junk count
            junkCount= int(sequence.count('-'))
            #stuff for fuctions above
            characters = getCounts(sequence)
            
            massList= getTotalMass(characters,junkCount)
            totalMass= (massList[0]+ massList[1]+ massList[2]+ massList[3] + massList[4])
            
            perList= getPercentages(characters,totalMass)
            mainList.append(perList)
        
            sequence2 = sequence.replace('-','')
            codons= getCodons(sequence2)
            
            protein = is_protein(codons, perList)            
            printResults(name, sequence, characters, massList, perList, codons, protein, fileOut)
        fileOut.close()
        drawGraph(mainList)
        ans=input("do you want to run my program again? y/n: ").lower()
    else:
        #prints page if user says no or anything else than answer starting with y
        customPage()
main()
#print statement that ends the program every time
print("Thank you for using my program :)")




    
        
    
    

        
