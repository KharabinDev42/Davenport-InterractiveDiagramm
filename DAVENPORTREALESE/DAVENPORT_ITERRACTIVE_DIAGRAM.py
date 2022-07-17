import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import functools
fp = functools.partial
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
import matplotlib.animation as an
from matplotlib import pyplot as plt
from IPython.display import clear_output
import numpy as np
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfilename
import os
import win32api
import win32print
import tempfile



LanguageBUTTOnFRVARget = 'FR'



def installed_printer():
    printers = win32print.EnumPrinters(2)
    for p in printers:
        return(p)

def locprinter():
    pt = ttk.Toplevel()
    pt.geometry("250x250")
    pt.title("choose printer")
    var1 = tk.StringVar()
    LABEL = ttk.Label(pt, text="select Printer").pack()
    PRCOMBO = ttk.Combobox(pt, width=35,textvariable=var1)
    print_list = []
    printers = list(win32print.EnumPrinters(2))
    for i in printers:
        print_list.append(i[2])
    print(print_list)
    # Put printers in combobox
    PRCOMBO['values'] = print_list
    PRCOMBO.pack()
    def select():
        global printerdef
        printerdef = PRCOMBO.get()
        pt.destroy()
    BUTTON = ttk.Button(pt, text="Done",command=select).pack()

    


def PRRINTTT():
    printText = 'ok'
    print(printText)
    print(printerdef)
    filename = tempfile.mktemp(".png")
    open(filename, "w").write(printText)
    # Bellow is call to print text from T2 textbox
    win32api.ShellExecute(
        0,
        "printto",
        filename,
        '"%s"' % win32print.GetDefaultPrinter(),
        ".",
        0
    )


def print_file():
    
   


    global plot1
    global fig
    file_to_print = asksaveasfile(mode='w', defaultextension=".png")
    abs_path = os.path.abspath(file_to_print.name)
    fig.savefig(abs_path) # saves the image to the input file name.
    
      
    if file_to_print:
        
        # Print Hard Copy of File
        win32api.ShellExecute(0, "print", abs_path, None, ".", 0)




#window  = ttk.Window(themename="marcoooo")
window  = ttk.Window(themename="darkly")


window.title("yoo")
window.geometry("1370x670")

drawn =0


SETINGSFRAME = ttk.Frame(window,bootstyle="dark")
SETINGSFRAME.pack(side=LEFT, padx=15, pady=15)

SETINGLANGUAGE = ttk.Frame(SETINGSFRAME,bootstyle="dark")
SETINGLANGUAGE.pack(side=TOP, padx=0, pady=0)


LanguageBUTTOnFRVAR = tk.StringVar() 
LanguageBUTTOnFRVAR.set('FR')

LanguageBUTTOnFR = ttk.Radiobutton(SETINGLANGUAGE,bootstyle="toolbutton, secondary", text='FR',variable=LanguageBUTTOnFRVAR, value='FR') 
LanguageBUTTOnFR.pack(side=LEFT, padx=1, pady=1)


LanguageBUTTOnEN = ttk.Radiobutton(SETINGLANGUAGE,bootstyle="toolbutton, secondary",text='EN',variable=LanguageBUTTOnFRVAR, value='EN')
LanguageBUTTOnEN.pack(side=LEFT, padx=1, pady=1)



if LanguageBUTTOnFRVAR == 'FR':
    LanguageBUTTOnFRVARget ="Etat du patient"
if LanguageBUTTOnFRVAR=='EN':
    LanguageBUTTOnFRVARget ="Patient state"





CONCLUSIONLabel = ttk.Labelframe(SETINGSFRAME,text ="Etat du patient",bootstyle="light")
CONCLUSIONLabel.pack(side=TOP, padx=2, pady=5, fill =X)

STATTE = ttk.Label(CONCLUSIONLabel,bootstyle="info",text ="EQUILIBRE",font ='-size 25 -weight bold')
STATTE.pack(side=TOP, padx=15, pady=15)

PARAMETERSLabel = ttk.Labelframe(SETINGSFRAME,text ="Paramètres",bootstyle="light")
PARAMETERSLabel.pack(side=BOTTOM, padx=2, pady=5)





BICAR = 24

PHFRAME = ttk.Labelframe(PARAMETERSLabel,text ="PH",bootstyle="PRIMARY")
PHFRAME.pack(expand = YES,side=BOTTOM, padx=2, pady=3)




BICFRAME = ttk.Labelframe(PARAMETERSLabel,text ="HCO3-",bootstyle="PRIMARY")
BICFRAME.pack(side=LEFT, padx=2, pady=2)


radioValuePHH = tk.IntVar() 
radioValuePHH.set(7)

SIXXPH = ttk.Radiobutton(PHFRAME,bootstyle="toolbutton, warning", text='6',variable=radioValuePHH, value=6) 
SIXXPH.pack(side=LEFT, padx=3, pady=5,fill= X)


SEPTTTPH = ttk.Radiobutton(PHFRAME,bootstyle="toolbutton, warning",text='7',variable=radioValuePHH, value=7)
SEPTTTPH.pack(side=LEFT, padx=3, pady=5,fill= X)

COMAA = ttk.Label(PHFRAME,bootstyle=" warning",text=',')
COMAA.pack(side=LEFT, padx=3, pady=10)




test43 = ttk.Meter(PHFRAME,
    metersize=180,amounttotal = 99,
    padding=5,amountused=40,
    stepsize=1,
    metertype="full",
    subtext="fine tuning",
    interactive=False,stripethickness =2,bootstyle=SUCCESS)
test43.pack(side=RIGHT, padx=2, pady=10)

test44 = ttk.Meter(BICFRAME,
    metersize=180,amounttotal = 50,
    padding=5,amountused=24,
    stepsize=0.5,
    metertype="full",
    subtext="mmol/L",
    interactive=True,
    stripethickness =2,bootstyle=SUCCESS)
test44.pack(side=LEFT, padx=3, pady=10)

PENTEFRAME = ttk.LabelFrame(PARAMETERSLabel,text ="PENTE",bootstyle="PRIMARY")
PENTEFRAME.pack(side=BOTTOM, padx=2, pady=2)

radioValue = tk.IntVar() 
radioValue.set(25)
cinq = ttk.Radiobutton(PENTEFRAME,bootstyle="toolbutton, warning",text='5',
variable=radioValue, value=5)
cinq.pack(side=LEFT, padx=3, pady=10)

dixx = ttk.Radiobutton(PENTEFRAME,bootstyle="toolbutton, warning", text='10',variable=radioValue, value=10) 
dixx.pack(side=LEFT, padx=3, pady=10)

quinze = ttk.Radiobutton(PENTEFRAME,bootstyle="toolbutton, warning", text='15',variable=radioValue, value=15) 
quinze.pack(side=LEFT, padx=3, pady=10)

vingt = ttk.Radiobutton(PENTEFRAME,bootstyle="toolbutton, warning", text='20',variable=radioValue, value=20) 
vingt.pack(side=LEFT, padx=3, pady=10)

trente = ttk.Radiobutton(PENTEFRAME,bootstyle="toolbutton, warning", text='25',variable=radioValue, value=25) 
trente.pack(side=RIGHT, padx=3, pady=10)






def browsefunc():
    global plot1
    global fig
    file = asksaveasfile(mode='w', defaultextension=".png")
    if file :
        abs_path = os.path.abspath(file.name)
        fig.savefig(abs_path) # saves the image to the input file name.
        

PURETEEFRAME = ttk.Labelframe(PARAMETERSLabel,text ="Puretée",bootstyle="light")
PURETEEFRAME.pack(side=TOP, padx=2, pady=10, fill =X)

PURETEESTATTE = ttk.Label(PURETEEFRAME,bootstyle="info",text =" ",font ='-size 15 -weight bold')
PURETEESTATTE.pack(side=TOP, padx=15, pady=15)

PRINTT2 = ttk.Button(PARAMETERSLabel,text ="Enregistrer + imprimer",bootstyle="PRIMARY", command = print_file)
PRINTT2.pack(side=BOTTOM, padx=1, pady=3, fill =X)


SAVEEE = ttk.Button(PARAMETERSLabel,text ="Enregistrer l'image sous",bootstyle="PRIMARY", command = browsefunc)
SAVEEE.pack(side=BOTTOM, padx=1, pady=3, fill =X)


m = ttk.Menu(window, tearoff = 0)
m.add_command(label ="Cut")
m.add_command(label ="Copy")
m.add_command(label ="Paste")
m.add_command(label ="Reload")
m.add_separator()
m.add_command(label ="Rename")



def _on_mousewheel(event):
    steppQ = (-1 *(event.delta/ 120))
    test43.step(steppQ)
    

    

stateclickR = None
def Activate_change(event):
    
    
    global stateclickR 

    if stateclickR == None:
        stateclickR = True
        
    elif stateclickR == False:
        stateclickR = True
        
    elif stateclickR == True:
        stateclickR = False
        
    print(stateclickR)
    if stateclickR == True:

        test43.configure(bootstyle=WARNING)
        stateclickR = False
        test43.configure(interactive=True, textfont ='-size 35 -weight bold', stripethickness=3)
        test43.bind_all("<MouseWheel>", _on_mousewheel)

    

def _on_mousewheelBIC(event):
    test44.step((-1 *(event.delta/ 120)))
    

stateclickRBIC = None
def Activate_changeBIC(event):
    
    
    global stateclickRBIC 

    if stateclickRBIC == None:
        stateclickRBIC = True
        
    elif stateclickRBIC == False:
        stateclickRBIC = True
        
    elif stateclickRBIC == True:
        stateclickRBIC = False
        
    print(stateclickRBIC)
    if stateclickRBIC == True:

        test44.configure(bootstyle=WARNING)
        stateclickRBIC = False
        test44.configure(interactive=True, textfont ='-size 35 -weight bold', stripethickness=3)
        test44.bind_all("<MouseWheel>", _on_mousewheelBIC)


   
        
   

def HighlightAndGo(event):
    
    test43.configure(bootstyle=INFO)
    #test43.unbind_all("<Button-1>")
    test43.unbind_all("<MouseWheel>")
    

def hover_this_enter(event):
    
    #test43.configure(interactive=True)
    test43.configure(bootstyle=WARNING)
    test43.bind_all("<Button-1>",Activate_change)
    
                           
def hover_this_leave(event):   
    
    test43.configure(bootstyle=SUCCESS,interactive=False)
    test43.unbind_all("<MouseWheel>")
    test43.configure( textfont ='-size 20 -weight bold', stripethickness=2)
    test43.unbind_all("<Button-1>")
    
    ph= test43.amountusedvar.get()

   
    
    BICAR = test44.amountusedvar.get()

    
    global radioValue
    radioValueee = radioValue.get()
   


    global radioValuePHH
    radioValuePHHHH = radioValuePHH.get()
    phbase = radioValuePHHHH


    plot(phbase,ph,BICAR,radioValueee)
    Back = STATEDEFINER(ph,BICAR,radioValueee,phbase)
    etat =Back[0]
    pureteee =Back[1]

    STATTE.config(text=etat)
    PURETEESTATTE.config(text=pureteee)



def hover_this_enterBIC(event):
    
    test44.configure(bootstyle=WARNING)
    test44.bind_all("<Button-1>",Activate_changeBIC)

def hover_this_leaveBIC(event):
    
    test44.configure(bootstyle=SUCCESS,interactive=False)
    test44.unbind_all("<MouseWheel>")
    test44.configure( textfont ='-size 20 -weight bold', stripethickness=2)
    test44.unbind_all("<Button-1>")
    
    ph= test43.amountusedvar.get()

 
    
    BICAR = test44.amountusedvar.get()

   
    global radioValue
    radioValueee = radioValue.get()
   


    global radioValuePHH
    radioValuePHHHH = radioValuePHH.get()
    phbase = radioValuePHHHH


    plot(phbase,ph,BICAR,radioValueee)

    Back = STATEDEFINER(ph,BICAR,radioValueee,phbase)
    etat =Back[0]
    pureteee =Back[1]

    STATTE.config(text=etat)
    PURETEESTATTE.config(text=pureteee)

    


    

test43.bind("<Enter>", hover_this_enter)
test43.bind("<Leave>", hover_this_leave)

test44.bind("<Enter>", hover_this_enterBIC)
test44.bind("<Leave>", hover_this_leaveBIC)




  
def do_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()
  
window.bind("<Button-3>", do_popup)  


  
def plot(phbase,ph,BICAR,radioValue): 
    global plot1
    global fig

    global drawn
    global canvas

    if drawn !=0:
       
        canvas.get_tk_widget().destroy()
       
     

    
    
    fig = Figure(figsize = (160, 160), 
                 dpi = 110) 
  
    
    
    x = np.linspace(6,9)
    
   
    y = ((10**(x-6.1))*(0.03*40))
 
    plot1 = fig.add_subplot() 
  
    plot1.set_xlim([6.8, 7.8])
    plot1.set_ylim([0, 50])
    

    plot1.xaxis.set_major_locator(MultipleLocator(0.2))
    plot1.yaxis.set_major_locator(MultipleLocator(10))
    
    plot1.xaxis.set_minor_locator(MultipleLocator(0.01))
    plot1.yaxis.set_minor_locator(MultipleLocator(1))
    plot1.grid(which='major', color='#CCCCCC', linestyle='--',linewidth=1)
    plot1.grid(which='minor', color='#CCCCCC', linestyle=':')

    plot1.set_xlabel('PH')
    plot1.set_ylabel('HCO3-')
    

    plot1.plot(x,y) 
    

    pphh = 10
    while pphh != 90:

        x = np.linspace(6,9)
        y = ((10**(x-6.1))*(0.03*pphh))
        if pphh == 40:
            
            plot1.plot(x,y,color='black', linewidth=2, markersize=2)
        else:
            plot1.plot(x,y,linestyle='dashed',color='grey')
        pphh = pphh+10

        
    
    coef =5
    conteur = 0
    list = [61,98,135,172,209,246]
    while coef != 30 :
        DIR =list[conteur]
        x = np.linspace(6,9)
        y = -coef*x+DIR       
        plot1.plot(x,y,linestyle='dotted',color='steelblue',linewidth=1)
        coef=coef+5
        conteur = conteur +1
    
   
    if ph !=0:
        
        y = BICAR
        x = phbase+(ph*0.01)
        plot1.plot(x,y,'ro',markersize=7, color = 'salmon')


        PCO2=((BICAR)/(10**((phbase+(ph*0.01))-6.1)))/0.03
        x = np.linspace(6,9)
        y = ((10**(x-6.1))*(0.03*PCO2))

        plot1.plot(x,y,color='salmon',linewidth=2)
        xu= (phbase+(ph*0.01))
        plot1.axvline(x = xu, color = "salmon",linestyle='dashed',linewidth=0.9)
        
        plot1.axhline(y = BICAR, color = "salmon",linestyle='dashed',linewidth=0.9)
        plot1.annotate(xu,((xu+0.01),1),color = "seagreen",weight="bold")
        plot1.annotate(BICAR,(6.8,(BICAR+0.5)),color = "seagreen",weight="bold")
       
        PCO2=round(PCO2,2)
        PCO2 = str(PCO2)
        plot1.annotate((PCO2+'mmHg (PaC02)'),((xu+0.02),(BICAR+0.5)),color = "darkgreen",weight="bold")


        if radioValue ==5:
            x = np.linspace(6,9)
            y = (-5*(x-(xu-7.4))+(61)) +(BICAR-24) 

        if radioValue ==10:
            x = np.linspace(6,9)
            y = (-10*(x-(xu-7.4))+(98)) +(BICAR-24)

        if radioValue ==15:
            x = np.linspace(6,9)
            y = (-15*(x-(xu-7.4))+(135)) +(BICAR-24)

        if radioValue ==20:
            x = np.linspace(6,9)
            y = (-20*(x-(xu-7.4))+(172)) +(BICAR-24)

        if radioValue ==25:
            x = np.linspace(6,9)
            y = (-25*(x-(xu-7.4))+(209)) +(BICAR-24)
        
         
 
        plot1.plot(x,y,color='darkorange',linewidth=2)

        if radioValue ==5:
            x = np.linspace(6,9)
            y = (-5*(x)+(61))

        if radioValue ==10:
            x = np.linspace(6,9)
            y = (-10*(x)+(98))

        if radioValue ==15:
            x = np.linspace(6,9)
            y = (-15*(x)+(135)) 

        if radioValue ==20:
            x = np.linspace(6,9)
            y = (-20*(x))+(172) 

        if radioValue ==25:
            x = np.linspace(6,9)
            y = (-25*(x))+(209) 

        plot1.plot(x,y,color='burlywood',linewidth=1)



    plot1.axvline(x = 7.4, color = "black",)
    plot1.axhline(y = 24, color = "black",)
    
    
    
    canvas = FigureCanvasTkAgg(fig, master = window) 
    
 
    
    canvas.get_tk_widget().pack() 
    canvas.get_tk_widget().pack() 

    
    drawn =1
    
def STATEDEFINER(ph,bic,pente,phbase):

    Language = LanguageBUTTOnFRVAR.get()

   
    purete =''

    
    state = ''
    PCO2=((bic)/(10**((phbase+(ph*0.01))-6.1)))/0.03
    ph = phbase+(ph*0.01)

    if ph< 7.38:
        if Language == 'FR':
             state ='Acidose'

        if Language == 'EN':
             state ='Acidosis'

        
        if bic >= 26:
            if Language == 'FR':
                state ='Acidose respiratoire'
            if Language == 'EN':
                state ='respiratory acidosis'
            if ph<7.15:
                state ='Acidose'
                purete ='MIXTE'
            if ph>7.15:
                state ='Acidose respiratoire'
                purete =''
            
            

        if bic < 24:
            state ='Acidose métabolique'
            if PCO2>40:
                state ='Acidose'
                purete ='MIXTE'
            if PCO2<40:
                state ='Acidose métabolique'
                purete =''
            if PCO2==40:
                state ='Acidose métabolique '
                purete ='pure'

        

    if ph> 7.42:
        if bic > 26:
            if PCO2<40:
                state ='Alcalose'
                purete ='MIXTE'
            if PCO2>40:
                state ='Alcalose métabolique'
                purete =''
            if PCO2==40:
                state ='Alcalose métabolique'
                purete ='pure'
        if bic < 22:
            state ='Alcalose respiratoire'
        if bic>22 and bic<26:
            state ='Alcalose'
            purete ='MIXTE'

    if ph> 7.4 and ph<= 7.42:
        if bic>26:
            state='Alcalose métabolique'
            purete ='comppensée'
        if bic<22:
            state='Alcalose Respiratoire'
            purete ='comppensée'

    if ph< 7.4 and ph>= 7.38:
        if bic>26:
            state='Acidose respiratoire '
            purete ='comppensée'
        if bic<22:
            state='Acidose métabolique'
            purete ='comppensée'

    if ph>=7.38 and ph <=7.42:
        if bic>=22 and bic <=26:
            state='EQUILIBRE'
            purete =''

    packk =[state,purete]
    return packk


plot(7,40,24,25)


def UpdatePlot(ph):
    print('test')



def TRADUCTOR(event): 
    LanguageBUTTOnFRVARget = LanguageBUTTOnFRVAR.get()

    if LanguageBUTTOnFRVARget == 'FR':
        CONCLUSIONLabel.config(text = "Etat du patient")
        #STATTE.config(text = "")
        PARAMETERSLabel.config(text = "paramètres")
        PHFRAME.config(text = "PH")
        BICFRAME.config(text = "HCO3-")
        PENTEFRAME.config(text = "Pente")
        PURETEEFRAME.config(text = "Compensation")
        #PURETEESTATTE.config(text = "")
        PRINTT2.config(text = "Enregistrer et imprimer")
        SAVEEE.config(text = "Enregistrer l'image sous")
        test43.configure(subtext='ph étalonage fin')
    if LanguageBUTTOnFRVARget == 'EN':
        CONCLUSIONLabel.config(text = "Patient State")
        #STATTE.config(text = "")
        PARAMETERSLabel.config(text = "settings")
        PHFRAME.config(text = "PH")
        BICFRAME.config(text = "HCO3-")
        PENTEFRAME.config(text = "PENTE")
        PURETEEFRAME.config(text = "Compensation")
        #PURETEESTATTE.config(text = "")
        PRINTT2.config(text = "Save and print")
        SAVEEE.config(text = "Save image as")
        test43.configure(subtext='fine ph tunning')



LanguageBUTTOnFR.bind("<Button-1>", TRADUCTOR)
LanguageBUTTOnEN.bind("<Button-1>", TRADUCTOR)

window.mainloop()

