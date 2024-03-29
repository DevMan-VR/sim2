from tkinter import StringVar
import ServerSequential
import ServerParallel
from SimLogic import Simulation
import numpy as np
import pandas as pd

from distributions.Normal import NormalClass
from distributions.Pascal import PascalClass

try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
    from tkinter import ttk
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2


from distributions.Exponential import ExponentialClass
from distributions.Uniforme_Discreta import UniformeDiscretaClass
from distributions.Uniforme_Continua import UniformeContinuaClass
from distributions.Bernoulli import BernoulliClass
from distributions.Normal import NormalClass
from distributions.Normal_Standard import NormalStandardClass
from distributions.Binomial import BinomialClass
from distributions.Poisson import PoissonClass
from distributions.Geometrica import GeometricaClass
from distributions.Erlang import ErlangClass
from distributions.Weibull import WeibullClass
from distributions.Pareto import ParetoClass
from distributions.Tstudent import TstudentClass

#Constants
SERVER_CONFIG_OPTIONS = ["Serie", "Paralelo"]
SERVER_DIST_OPTIONS = ["Uniforme Discreta","Uniforme Continua","Bernoulli","Exponencial","Normal","Normal Estandar","Binomial","Poisson","Geometrica","Erlang","Weibull","Pareto","T-Student", "Pascal"]


#Selections & Configuration
#global selected_server_config_option
#global selected_n_sequential_servers
#global selected_n_paralell_servers
#global server_current_index
#global server_current_configuration
#global server_list

selected_server_config_option = SERVER_CONFIG_OPTIONS[0] #Por defecto en serie
server_current_index = 0
server_current_configuration = None
server_current_service_distribution = None
server_current_arrival_distribution = None
server_current_has_queue = None
server_current_queue_capacity = None
server_current_queue_is_infinite = None
server_current_arrival_time_list = []
server_current_service_time_list = []

server_current_service_distribution_instance = None
server_current_arrival_distribution_instance = None

server_list = []

SIZE_OF_TIMES = 100

simulation_instance = None













class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=12)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)



        self.frames = {}
        for F in (Config_1, Config_2, Config_3_A,Config_4, Config_5, Config_6, Config_7, Config_8, Config_9, Config_10, Config_11):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Config_1")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Config_1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="Defina el tipo de configuración", font=controller.title_font)
        self.label.grid(row=1, column=1)

        global SERVER_CONFIG_OPTIONS

        self.server_config_option_combobox = ttk.Combobox(self, values=SERVER_CONFIG_OPTIONS)
        self.server_config_option_combobox.grid(row=1, column=2)
        self.server_config_option_combobox.current(0)

        self.nextBtn = tk.Button(self, text="Siguiente",command=lambda: self.saveDataAndNext())
        self.nextBtn.grid(row=3, column=2)



    def saveDataAndNext(self):
        global server_current_configuration
        server_current_configuration = self.server_config_option_combobox.get()
        print(server_current_configuration)
        self.controller.show_frame("Config_2")



class Config_2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        global SERVER_DIST_OPTIONS

        title1 = ""
        if(len(server_list) == 0):
            title1 = "Elige la distribución del tiempo de servicio del primer servidor"
        else:
            title1 = "Elige la distribución del tiempo de servicio del nuevo servidor"
        
        label = tk.Label(self, text=title1, font=controller.title_font)
        label.grid(row=1,column=1)
        self.combobox = ttk.Combobox(self, values=SERVER_DIST_OPTIONS)
        self.combobox.grid(row=1, column=2)
        self.combobox.current(0)

        button3 = tk.Button(self, text="Atras",command=lambda:self.goBack())
        button3.grid(row=2,column=1)

        
        button2 = tk.Button(self, text="Guardar",command=lambda:self.saveData())
        button2.grid(row=2,column=2)

        button = tk.Button(self, text="Siguiente",command=lambda:self.next())
        button.grid(row=2,column=3)

    def goBack(self):
        self.controller.show_frame("Config_1")

    def next(self):
        self.controller.show_frame("Config_3_A")
        

    def saveData(self):
        global server_current_service_distribution

        print("server dist current options: ", self.combobox.get())
        server_current_service_distribution = self.combobox.get()

        print("server current srvide cd: ", server_current_service_distribution)

class Config_3_A(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        global server_current_service_distribution
        
        label2 = tk.Label(self, text="Define los parametros de la distribución de servicio", font=controller.title_font)
        label2.grid(row=0, column=1)

        button2 = tk.Button(self, text="Atras",command=lambda:self.goBack())
        button2.grid(row=3,column=1)

        button1 = tk.Button(self, text="Mostrar",command=lambda:self.show())
        button1.grid(row=3,column=2)

        button = tk.Button(self, text="Siguiente",command=lambda:self.saveDataAndNext())
        button.grid(row=3,column=3)

    def goBack(self):
        self.controller.show_frame("Config_2")

    def show(self):
        print("Server current sd: ",server_current_service_distribution)
        print("comparison is: ",server_current_service_distribution == "Exponencial")

        if(server_current_service_distribution == "Exponencial"):
            self.label_exp = tk.Label(self, text="Lambda", font=self.controller.title_font)
            self.label_exp.grid(row=1, column=1)
            self.entry_exp = tk.Entry(self)
            self.entry_exp.grid(row=2, column=1)

        elif(server_current_service_distribution == "Uniforme Discreta"):
            self.label_ud = tk.Label(self, text="n° de posibilidades", font=self.controller.title_font)
            self.label_ud.grid(row=1, column=1)
            self.entry_ud = tk.Entry(self)
            self.entry_ud.grid(row=2, column=1)

        elif(server_current_service_distribution == "Uniforme Continua"):
            self.label_uc_1 = tk.Label(self, text="a", font=self.controller.title_font)
            self.label_uc_1.grid(row=1, column=1)
            self.entry_uc_1 = tk.Entry(self)
            self.entry_uc_1.grid(row=2, column=1)

            self.label_uc_2 = tk.Label(self, text="b", font=self.controller.title_font)
            self.label_uc_2.grid(row=1, column=2)
            self.entry_uc_2 = tk.Entry(self)
            self.entry_uc_2.grid(row=2, column=2)

        elif(server_current_service_distribution == "Bernoulli"):
            self.label_ber = tk.Label(self, text="No hay parametros", font=self.controller.title_font)
            self.label_ber.grid(row=1, column=1)
        
        elif(server_current_service_distribution == "Normal"):
            self.label_nor_1 = tk.Label(self, text="mu", font=self.controller.title_font)
            self.label_nor_1.grid(row=1, column=1)
            self.entry_nor_1 = tk.Entry(self)
            self.entry_nor_1.grid(row=2, column=1)

            self.label_nor_2 = tk.Label(self, text="ro", font=self.controller.title_font)
            self.label_nor_2.grid(row=1, column=2)
            self.entry_nor_2 = tk.Entry(self)
            self.entry_nor_2.grid(row=2, column=2)

        elif(server_current_service_distribution == "Normal Estandar"):
            self.label_nores_1 = tk.Label(self, text="mu", font=self.controller.title_font)
            self.label_nores_1.grid(row=1, column=1)
            self.entry_nores_1 = tk.Entry(self)
            self.entry_nores_1.grid(row=2, column=1)

            self.label_nores_2 = tk.Label(self, text="ro", font=self.controller.title_font)
            self.label_nores_2.grid(row=1, column=2)
            self.entry_nores_2 = tk.Entry(self)
            self.entry_nores_2.grid(row=2, column=2)

        elif(server_current_service_distribution == "Binomial"):
            self.label_bin_1 = tk.Label(self, text="n", font=self.controller.title_font)
            self.label_bin_1.grid(row=1, column=1)
            self.entry_bin_1 = tk.Entry(self)
            self.entry_bin_1.grid(row=2, column=1)

            self.label_bin_2 = tk.Label(self, text="m", font=self.controller.title_font)
            self.label_bin_2.grid(row=1, column=2)
            self.entry_bin_2 = tk.Entry(self)
            self.entry_bin_2.grid(row=2, column=2)
        
        elif(server_current_service_distribution == "Poisson"):
            self.label_pos_1 = tk.Label(self, text="lambda", font=self.controller.title_font)
            self.label_pos_1.grid(row=1, column=1)
            self.entry_pos_1 = tk.Entry(self)
            self.entry_pos_1.grid(row=2, column=1)

            self.label_pos_2 = tk.Label(self, text="k", font=self.controller.title_font)
            self.label_pos_2.grid(row=1, column=2)
            self.entry_pos_2 = tk.Entry(self)
            self.entry_pos_2.grid(row=2, column=2)

        elif(server_current_service_distribution == "Geometrica"):
            self.label_geo = tk.Label(self, text="k", font=self.controller.title_font)
            self.label_geo.grid(row=1, column=2)
            self.entry_geo = tk.Entry(self)
            self.entry_geo.grid(row=2, column=2)

        elif(server_current_service_distribution == "Erlang"):
            self.label_er_1 = tk.Label(self, text="n", font=self.controller.title_font)
            self.label_er_1.grid(row=1, column=1)
            self.entry_er_1 = tk.Entry(self)
            self.entry_er_1.grid(row=2, column=1)

            self.label_er_2 = tk.Label(self, text="lambda", font=self.controller.title_font)
            self.label_er_2.grid(row=1, column=2)
            self.entry_er_2 = tk.Entry(self)
            self.entry_er_2.grid(row=2, column=2)

        elif(server_current_service_distribution == "Weibull"):
            self.label_wei_1 = tk.Label(self, text="tasa de fallos", font=self.controller.title_font)
            self.label_wei_1.grid(row=1, column=1)
            self.entry_wei_1 = tk.Entry(self)
            self.entry_wei_1.grid(row=2, column=1)

            self.label_wei_2 = tk.Label(self, text="lambda", font=self.controller.title_font)
            self.label_wei_2.grid(row=1, column=2)
            self.entry_wei_2 = tk.Entry(self)
            self.entry_wei_2.grid(row=2, column=2)

        elif(server_current_service_distribution == "Pareto"):
            self.label_par_1 = tk.Label(self, text="alfa", font=self.controller.title_font)
            self.label_par_1.grid(row=1, column=1)
            self.entry_par_1 = tk.Entry(self)
            self.entry_par_1.grid(row=2, column=1)

            self.label_par_2 = tk.Label(self, text="valor inicial", font=self.controller.title_font)
            self.label_par_2.grid(row=1, column=2)
            self.entry_par_2 = tk.Entry(self)
            self.entry_par_2.grid(row=2, column=2)

        elif(server_current_arrival_distribution == "T-Student"):
            self.label_tstud = tk.Label(self, text="grados de libertad", font=self.controller.title_font)
            self.label_tstud.grid(row=1, column=1)
            self.entry_tstud = tk.Entry(self)
            self.entry_tstud.grid(row=2, column=1)

        elif(server_current_service_distribution == "Pascal"):
            self.label_pasc_1 = tk.Label(self, text="k", font=self.controller.title_font)
            self.label_pasc_1.grid(row=1, column=1)
            self.entry_pasc_1 = tk.Entry(self)
            self.entry_pasc_1.grid(row=2, column=1)

            self.label_pasc_2 = tk.Label(self, text="m", font=self.controller.title_font)
            self.label_pasc_2.grid(row=1, column=2)
            self.entry_pasc_2 = tk.Entry(self)
            self.entry_pasc_2.grid(row=2, column=2)


        
    def saveDataAndNext(self):
        global server_current_service_distribution
        global server_current_service_time_list
        global SIZE_OF_TIMES
        global server_current_service_distribution_instance
        
        dist = None
        if(server_current_service_distribution == "Exponencial"):
            lamb = float(self.entry_exp.get())
            dist = ExponentialClass(lambdaValue=lamb)
            print("Lamb is", lamb)

        elif(server_current_service_distribution == "Uniforme Discreta"):
            n = float(self.entry_ud.get())
            dist = UniformeDiscretaClass(n=n)
            print("n° de posibilidades is", n)
            print("Uniforme Discreta")
        
        elif(server_current_service_distribution == "Uniforme Continua"):
            a = float(self.entry_uc_1.get())
            b = float(self.entry_uc_2.get())
            dist = UniformeContinuaClass(a=a, b=b)
            print("A is ", a)
            print("B is ", b)
            print("Uniforme Continua")
        
        elif(server_current_service_distribution == "Bernoulli"):
            dist = BernoulliClass()
            print("Bernoulli")

        elif(server_current_service_distribution == "Normal"):
            mu = float(self.entry_nor_1.get())
            ro = float(self.entry_nor_2.get())
            dist = NormalClass(mu=mu, ro=ro)
            print("Mu is ", mu)
            print("Ro is ", ro)
            print("Normal")

        elif(server_current_service_distribution == "Normal Estandar"):
            mu = float(self.entry_nores_1.get())
            ro = float(self.entry_nores_2.get())
            dist = NormalStandardClass(mu=mu, ro=ro)
            print("Mu is ", mu)
            print("Ro is ", ro)
            print("Normal Estandar")

        elif(server_current_service_distribution == "Binomial"):
            n = float(self.entry_bin_1.get())
            m = float(self.entry_bin_2.get())
            dist = BinomialClass(n=n, m=m)
            print("n is ", n)
            print("m is ", m)
            print("Binomial")

        elif(server_current_service_distribution == "Poisson"):
            lamb = float(self.entry_pos_1.get())
            k = float(self.entry_pos_2.get())
            dist = PoissonClass(lamb=lamb, k=k)
            print("lamb is ", lamb)
            print("k is ", k)
            print("Poisson")

        elif(server_current_service_distribution == "Geometrica"):
            k = float(self.entry_geo.get())
            dist = GeometricaClass(k=k)
            print("k", k)
            print("Geometrica")

        elif(server_current_service_distribution == "Erlang"):
            n = float(self.entry_er_1.get())
            lamb = float(self.entry_er_2.get())
            dist = ErlangClass(n=n,lamb=lamb)
            print("Erlang")


        elif(server_current_service_distribution == "Weibull"):
            tasa_fallos = float(self.entry_wei_1.get())
            lamb = float(self.entry_wei_2.get())
            dist = WeibullClass(tasa_fallos=tasa_fallos, lamb=lamb)
            print("tasa_fallos is ", tasa_fallos)
            print("lamb is ", lamb)
            print("Weibull")

        elif(server_current_service_distribution == "Pareto"):
            alpha = float(self.entry_par_1.get())
            xm = float(self.entry_par_2.get())
            dist = ParetoClass(alpha=alpha, xm=xm)
            print("alfa is ", alpha)
            print("initial = xm is ", xm)
            print("Pareto")
        
        elif(server_current_service_distribution == "T-Student"):
            v = float(self.entry_tstud.get())
            dist = TstudentClass(v=v)
            print("v", v)
            print("T-Student")

        elif(server_current_service_distribution == "Pascal"):
            k = float(self.entry_pasc_1.get())
            m = float(self.entry_pasc_2.get())
            dist = PascalClass(k=k, m=m)
            print("k is ", k)
            print("m is ",m)
            print("Pascal")
        


        server_current_service_distribution_instance = dist
        print("server_current_service_distribution_instance is: ")
        print(server_current_service_distribution_instance)

   


        
        self.controller.show_frame("Config_4")



class Config_4(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        global SERVER_DIST_OPTIONS
        global server_list

        label2 = tk.Label(self, text="Elige la distribución de llegada", font=controller.title_font)
        label2.grid(row=2, column=1)
        self.combobox2 = ttk.Combobox(self, values=SERVER_DIST_OPTIONS)
        self.combobox2.grid(row=2, column=2)
        self.combobox2.current(0)

        button2 = tk.Button(self, text="Atras",command=lambda:self.goBack())
        button2.grid(row=3,column=2)

        button = tk.Button(self, text="Siguiente",command=lambda:self.saveDataAndNext())
        button.grid(row=3,column=3)

    def goBack(self):
        self.controller.show_frame("Config_3_A")
        
    def saveDataAndNext(self):
        global server_list
        global SERVER_CONFIG_OPTIONS
        global server_current_arrival_distribution

        server_current_arrival_distribution = self.combobox2.get()
        self.controller.show_frame("Config_5")

class Config_5(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        global SERVER_DIST_OPTIONS
        global server_list

        label2 = tk.Label(self, text="Define los parametros de la distribución de llegada", font=controller.title_font)
        label2.grid(row=0, column=1)

        button2 = tk.Button(self, text="Atras",command=lambda:self.goBack())
        button2.grid(row=3,column=1)

        button1 = tk.Button(self, text="Mostrar",command=lambda:self.show())
        button1.grid(row=3,column=2)

        button = tk.Button(self, text="Siguiente",command=lambda:self.saveDataAndNext())
        button.grid(row=3,column=3)


    def show(self):
        print("Server arrival current sd: ",server_current_arrival_distribution)
        print("comparison is: ",server_current_arrival_distribution == "Exponencial")

        if(server_current_arrival_distribution == "Exponencial"):
            self.label1 = tk.Label(self, text="Lambda", font=self.controller.title_font)
            self.label1.grid(row=1, column=1)
            self.entry1 = tk.Entry(self)
            self.entry1.grid(row=2, column=1)

        elif(server_current_arrival_distribution == "Uniforme Discreta"):
            self.label1 = tk.Label(self, text="n° de posibilidades", font=self.controller.title_font)
            self.label1.grid(row=1, column=1)
            self.entry1 = tk.Entry(self)
            self.entry1.grid(row=2, column=1)

        elif(server_current_arrival_distribution == "Uniforme Continua"):
            self.label1 = tk.Label(self, text="a", font=self.controller.title_font)
            self.label1.grid(row=1, column=1)
            self.entry1 = tk.Entry(self)
            self.entry1.grid(row=2, column=1)

            self.label2 = tk.Label(self, text="b", font=self.controller.title_font)
            self.label2.grid(row=1, column=2)
            self.entry2 = tk.Entry(self)
            self.entry2.grid(row=2, column=2)


        elif(server_current_arrival_distribution == "Bernoulli"):
            self.label1 = tk.Label(self, text="No hay parametros", font=self.controller.title_font)
            self.label1.grid(row=1, column=1)


        elif(server_current_arrival_distribution == "Normal"):
            self.label1 = tk.Label(self, text="mu", font=self.controller.title_font)
            self.label1.grid(row=1, column=1)
            self.entry1 = tk.Entry(self)
            self.entry1.grid(row=2, column=1)

            self.label2 = tk.Label(self, text="ro", font=self.controller.title_font)
            self.label2.grid(row=1, column=2)
            self.entry2 = tk.Entry(self)
            self.entry2.grid(row=2, column=2)

        elif(server_current_arrival_distribution == "Normal Estandar"):
            self.label1 = tk.Label(self, text="mu", font=self.controller.title_font)
            self.label1.grid(row=1, column=1)
            self.entry1 = tk.Entry(self)
            self.entry1.grid(row=2, column=1)

            self.label2 = tk.Label(self, text="ro", font=self.controller.title_font)
            self.label2.grid(row=1, column=2)
            self.entry2 = tk.Entry(self)
            self.entry2.grid(row=2, column=2)
        
        elif(server_current_arrival_distribution == "Binomial"):
            self.label1 = tk.Label(self, text="n", font=self.controller.title_font)
            self.label1.grid(row=1, column=1)
            self.entry1 = tk.Entry(self)
            self.entry1.grid(row=2, column=1)

            self.label2 = tk.Label(self, text="m", font=self.controller.title_font)
            self.label2.grid(row=1, column=2)
            self.entry2 = tk.Entry(self)
            self.entry2.grid(row=2, column=2)

        elif(server_current_arrival_distribution == "Poisson"):
            self.label1 = tk.Label(self, text="lambda", font=self.controller.title_font)
            self.label1.grid(row=1, column=1)
            self.entry1 = tk.Entry(self)
            self.entry1.grid(row=2, column=1)

            self.label2 = tk.Label(self, text="k", font=self.controller.title_font)
            self.label2.grid(row=1, column=2)
            self.entry2 = tk.Entry(self)
            self.entry2.grid(row=2, column=2)

        elif(server_current_arrival_distribution == "Geometrica"):
            self.label1 = tk.Label(self, text="k", font=self.controller.title_font)
            self.label1.grid(row=1, column=1)
            self.entry1 = tk.Entry(self)
            self.entry1.grid(row=2, column=1)

        elif(server_current_arrival_distribution == "Erlang"):
            self.label1 = tk.Label(self, text="n", font=self.controller.title_font)
            self.label1.grid(row=1, column=1)
            self.entry1 = tk.Entry(self)
            self.entry1.grid(row=2, column=1)

            self.label2 = tk.Label(self, text="lambda", font=self.controller.title_font)
            self.label2.grid(row=1, column=2)
            self.entry2 = tk.Entry(self)
            self.entry2.grid(row=2, column=2)

        elif(server_current_arrival_distribution == "Weibull"):
            self.label1 = tk.Label(self, text="tasa de fallos", font=self.controller.title_font)
            self.label1.grid(row=1, column=1)
            self.entry1 = tk.Entry(self)
            self.entry1.grid(row=2, column=1)

            self.label2 = tk.Label(self, text="lambda", font=self.controller.title_font)
            self.label2.grid(row=1, column=2)
            self.entry2 = tk.Entry(self)
            self.entry2.grid(row=2, column=2)

        elif(server_current_arrival_distribution == "Pareto"):
            self.label1 = tk.Label(self, text="alfa", font=self.controller.title_font)
            self.label1.grid(row=1, column=1)
            self.entry1 = tk.Entry(self)
            self.entry1.grid(row=2, column=1)

            self.label2 = tk.Label(self, text="valor inicial", font=self.controller.title_font)
            self.label2.grid(row=1, column=2)
            self.entry2 = tk.Entry(self)
            self.entry2.grid(row=2, column=2)

        elif(server_current_arrival_distribution == "T-Student"):
            self.label1 = tk.Label(self, text="grados de libertad", font=self.controller.title_font)
            self.label1.grid(row=1, column=1)
            self.entry1 = tk.Entry(self)
            self.entry1.grid(row=2, column=1)

        elif(server_current_arrival_distribution == "Pascal"):
            self.label1 = tk.Label(self, text="k", font=self.controller.title_font)
            self.label1.grid(row=1, column=1)
            self.entry1 = tk.Entry(self)
            self.entry1.grid(row=2, column=1)

            self.label2 = tk.Label(self, text="m", font=self.controller.title_font)
            self.label2.grid(row=1, column=1)
            self.entry2 = tk.Entry(self)
            self.entry2.grid(row=2, column=1)

        
        


    def goBack(self):
        self.controller.show_frame("Config_4")
        
    def saveDataAndNext(self):

        global server_current_arrival_distribution
        global server_current_arrival_distribution_instance

        dist = None
        if(server_current_arrival_distribution == "Exponencial"):
            lamb = float(self.entry1.get())
            dist = ExponentialClass(lambdaValue=lamb)
            print("Lamb is", lamb)
        
        elif(server_current_arrival_distribution == "Uniforme Discreta"):
            n = float(self.entry1.get())
            dist = UniformeDiscretaClass(n=n)
            print("n is", n)
            print("Uniforme Discreta")
        
        elif(server_current_arrival_distribution == "Uniforme Continua"):
            a = float(self.entry1.get())
            b = float(self.entry2.get())
            dist = UniformeContinuaClass(a=a, b=b)
            print("A is ", a)
            print("B is ", b)
            print("Uniforme Continua")
        
        elif(server_current_arrival_distribution == "Bernoulli"):
            #lamb = float(self.entryExp.get())
            dist = BernoulliClass()
            print("Bernoulli")

        elif(server_current_arrival_distribution == "Normal"):
            mu = float(self.entry1.get())
            ro = float(self.entry2.get())
            dist = NormalClass(mu=mu, ro=ro)
            print("Mu is ", mu)
            print("Ro is ", ro)
            print("Normal")

        elif(server_current_arrival_distribution == "Normal Estandar"):
            mu = float(self.entry1.get())
            ro = float(self.entry2.get())
            dist = NormalStandardClass(mu=mu, ro=ro)
            print("Mu is ", mu)
            print("Ro is ", ro)
            print("Normal Estandar")

        elif(server_current_arrival_distribution == "Binomial"):
            n = int(self.entry1.get())
            m = int(self.entry2.get())
            dist = BinomialClass(n=n, m=m)
            print("n is ", n)
            print("m is ", m)
            print("Binomial")

        elif(server_current_arrival_distribution == "Poisson"):
            lamb = float(self.entry1.get())
            k = float(self.entry2.get())
            dist = PoissonClass(lamb=lamb, k=k)
            print("lamb is ", lamb)
            print("k is ", k)
            print("Poisson")

        elif(server_current_arrival_distribution == "Geometrica"):
            k = float(self.entry1.get())
            dist = GeometricaClass(k=k)
            print("k is", k)

            print("Geometrica")

        elif(server_current_arrival_distribution == "Erlang"):
            n = float(self.entry1.get())
            lamb = float(self.entry2.get())
            dist = ErlangClass(n=n,lamb=lamb)
            print("Erlang")


        elif(server_current_arrival_distribution == "Weibull"):
            tasa_fallos = float(self.entry1.get())
            lamb = float(self.entry2.get())
            dist = WeibullClass(tasa_fallos=tasa_fallos, lamb=lamb)
            print("tasa_fallos is ", tasa_fallos)
            print("lamb is ", lamb)
            print("Weibull")

        elif(server_current_service_distribution == "Pareto"):
            alpha = float(self.entry1.get())
            xm = float(self.entry2.get())
            dist = ParetoClass(alpha=alpha, xm=xm)
            print("alfa is ", alpha)
            print("initial = xm is ", xm)
            print("Pareto")
        
        elif(server_current_arrival_distribution == "T-Student"):
            v = float(self.entry1.get())
            dist = TstudentClass(v=v)
            print("v", v)
            print("T-Student")

        elif(server_current_arrival_distribution == "Pascal"):
            k = float(self.entry1.get())
            m = float(self.entry2.get())
            dist = PascalClass(k=k, m=m)
            print("k", k)
            print("m", m)
            print("Pacal")
        


        server_current_arrival_distribution_instance = dist
        
        print("server_current_arrival_distribution_instance is: ")
        print(server_current_arrival_distribution_instance)

        self.controller.show_frame("Config_6")

class Config_6(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        
        label3 = tk.Label(self, text="¿Tiene cola de espera asociada?", font=controller.title_font)
        label3.grid(row=3, column=1)

        self.has_queue = tk.StringVar()
        ttk.Radiobutton(self, text="Si", variable=self.has_queue, value="Si").grid(row=3,column=2)
        ttk.Radiobutton(self, text="No", variable=self.has_queue, value="No").grid(row=3,column=3)

        button2 = tk.Button(self, text="Atras",command=lambda:self.goBack())
        button2.grid(row=5,column=2)

        button = tk.Button(self, text="Siguiente",command=lambda:self.saveDataAndNext())
        button.grid(row=5,column=3)


        
    def goBack(self):
        self.controller.show_frame("Config_5")

    def saveDataAndNext(self):
        global server_current_has_queue

        server_current_has_queue = self.has_queue.get()

        if(self.has_queue.get() == "Si"):
            self.controller.show_frame("Config_7")
        else:
            self.controller.show_frame("Config_9")

class Config_7(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller



        label4 = tk.Label(self, text="¿La cola es finita o infinita?", font=controller.title_font)
        label4.grid(row=1, column=1)

        self.queue_is_infinite = tk.StringVar()
        ttk.Radiobutton(self, text="Si", variable=self.queue_is_infinite, value="Si").grid(row=3,column=1)
        ttk.Radiobutton(self, text="No", variable=self.queue_is_infinite, value="No").grid(row=3,column=2)



        button2 = tk.Button(self, text="Atras",command=lambda:self.goBack())
        button2.grid(row=5,column=2)


        button = tk.Button(self, text="Siguiente",command=lambda:self.saveDataAndNext())
        button.grid(row=5,column=3)


    
    def goBack(self):
        self.controller.show_frame("Config_6")
        

    def saveDataAndNext(self):
        
        global server_current_queue_is_infinite 

        if(self.queue_is_infinite == "Si"):
            server_current_queue_is_infinite = True
            self.controller.show_frame("Config_9")
            
        else:
            server_current_queue_is_infinite = False
            self.controller.show_frame("Config_8")
        
        

        

class Config_8(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller



        label4 = tk.Label(self, text="¿Cual es la capacidad de esta cola?", font=controller.title_font)
        label4.grid(row=4, column=1)

        self.queue_capacity = tk.IntVar()
        self.capacity = ttk.Entry(self)
        self.capacity.grid(row=4,column=2)

        button2 = tk.Button(self, text="Atras",command=lambda:self.goBack())
        button2.grid(row=5,column=2)


        button = tk.Button(self, text="Siguiente",command=lambda:self.saveDataAndNext())
        button.grid(row=5,column=3)


    
    def goBack(self):
        self.controller.show_frame("Config_7")
        

    def saveDataAndNext(self):
        
        global server_current_queue_capacity 
        server_current_queue_capacity = int(self.capacity.get())

        self.controller.show_frame("Config_9")



class Config_9(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="¿Desea guardar todos los datos del servidor en el sistema?", font=controller.title_font)
        self.label.grid(row=1, column=1)

        self.btn1 = tk.Button(self, text="Atras",command=lambda: self.goBack())
        self.btn1.grid(row=2, column=1)

        self.btn2 = tk.Button(self, text="Guardar y Seguir",command=lambda: self.saveAndNext())
        self.btn2.grid(row=2, column=2)



    def saveAndNext(self):
        global server_list
        global server_current_index
        global server_current_configuration
        global server_current_service_distribution
        global server_current_arrival_distribution
        global server_current_has_queue
        global server_current_queue_capacity
        global server_current_arrival_time_list
        global server_current_service_time_list
        global server_current_queue_is_infinite

        global server_current_service_distribution_instance
        global server_current_arrival_distribution_instance
        
        print("Server list before: ")
        print(server_list)
        server = None

        if(server_current_configuration == 'Serie'):
            server = ServerSequential.Server_Sequential(
                server_current_index,
                server_current_configuration,
                server_current_service_distribution,
                server_current_arrival_distribution,
                server_current_has_queue,
                server_current_queue_capacity,
                server_current_service_time_list,
                server_current_arrival_time_list,
                None,
                server_current_queue_is_infinite,
                server_current_service_distribution_instance,
                server_current_arrival_distribution_instance
            )
        else:
            server = ServerParallel.Server_Parallel(
                server_current_index,
                server_current_configuration,
                server_current_service_distribution,
                server_current_arrival_distribution,
                server_current_has_queue,
                server_current_queue_capacity,
                server_current_service_time_list,
                server_current_arrival_time_list,
                None,
                None,
                server_current_queue_is_infinite,
                server_current_service_distribution_instance,
                server_current_arrival_distribution_instance
            )
        
        print("This is the new server adding: ", server)

        server_list.append(server)
        print("Server list after adding: ")
        print(server_list)

        self.controller.show_frame("Config_10")
    
    def goBack(self):
        self.controller.show_frame("Config_8")


class Config_10(tk.Frame):

    def __init__ (self, parent, controller):
        global server_list
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="¿Desea agregar un nuevo servidor al sistema o pasar a la simulación?", font=controller.title_font)
        self.label.grid(row=1, column=1)

        self.btn1 = tk.Button(self, text="Agregar nuevo Servidor",command=lambda: self.newServer())
        self.btn1.grid(row=2, column=1)

        self.btn1 = tk.Button(self, text="Simular",command=lambda: self.simulate())
        self.btn1.grid(row=2, column=2)

    def newServer(self):
        global server_current_index
        server_current_index += 1
        self.controller.show_frame("Config_1")


    def simulate(self):
        self.controller.show_frame("Config_11")


class Config_11(tk.Frame):

    def __init__ (self, parent, controller):
        global server_list
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="Primero agregue el tiempo de simulación, se recomienda un valor entre 100 y 300 unidades", font=controller.title_font)
        self.label.grid(row=1, column=1)

        self.clock = ttk.Entry(self)
        self.clock.grid(row=2,column=1)

        self.btn1 = tk.Button(self, text="Simular",command=lambda: self.simulate())
        self.btn1.grid(row=3, column=1)


    def simulate(self):
        global server_list
        global simulation_instance

        #Init indexes
        for s in server_list:
            print(s)
            if(s.configuration == 'Serie'):
                position = s.index +1
                if(position < len(server_list)):
                    s.next_server_index = s.index+1
            
            else:
                position = s.index+1
                #3 casos, hay 1 solo servidor siguiente, hay 2 o no hay ninguno
                n_next = len(server_list) - position
                if(n_next == 1):
                    s.next_server_up_index= s.index+1
                elif(n_next >= 2):
                    s.next_server_up_index= s.index+1
                    s.next_server_down_index= s.index+2
    
        print("SERVER_LIST BEFORE SIMULATION START IS ::::::: ")
        print(server_list)



        simulation_instance = Simulation(server_list=server_list)
        time_duration = int(self.clock.get())

        while simulation_instance.clock <= time_duration :
        #for i in range(1,10):
            simulation_instance.time_advance() 

        self.simulation_report()

    
    def simulation_report(self):
        global simulation_instance
        
        num_arrivals = 0
        number_in_queue = 0
        lost_customers = 0
        user_finished = 0
        num_arrivals = simulation_instance.server_list[0].num_arrivals

        
        
        for s in simulation_instance.server_list:
            number_in_queue += s.num_in_queue
            lost_customers += s.n_lost
            user_finished += s.user_finished
        
        t = []
        final_arr_column = []
        final_arr_result = []

        total_service_time =0
        total_wait_time=0
        for s in simulation_instance.server_list:
            if(s.configuration == 'Serie'):
                op1 = s.num_of_departures/s.dep_sum
                op2 = s.dep_sum / simulation_instance.clock
                
                final_arr_column.append('Average service time server '+str(s.index))
                final_arr_result.append(op1)
                t.append(['Average service time server '+str(s.index),op1])

                final_arr_column.append('Utilization server '+str(s.index))
                final_arr_result.append(op2)
                t.append(['Utilization server '+str(s.index),op2])

                total_service_time+=s.dep_sum


            else:
                op1_t1 = s.num_of_departures1/s.dep_sum1
                op2_t1 = s.dep_sum1 / simulation_instance.clock
                
                final_arr_column.append('Average service time server T1 S')
                final_arr_result.append(op1_t1)
                t.append(['Average service time server T1 S', op1_t1])

                final_arr_column.append('Utilization server T1 S')
                final_arr_result.append(op2_t1)
                t.append(['Utilization server T1 S', op2_t1])

                op1_t2 = s.num_of_departures2/s.dep_sum2
                op2_t2 = s.dep_sum2 / simulation_instance.clock

                final_arr_column.append('Average service time server T2 S')
                final_arr_result.append(op1_t2)
                t.append(['Average service time server T2 S', op1_t2])

                final_arr_column.append('Utilization server T2 S')
                final_arr_result.append(op2_t2)
                t.append(['Utilization server T2 S',op2_t2])

                total_service_time+=s.dep_sum1
                total_service_time+=s.dep_sum2


        final_arr_column.append('Average user in system')
        final_arr_result.append(num_arrivals/total_service_time)

        final_arr_column.append('Average interarrival time')
        final_arr_result.append(simulation_instance.clock/num_arrivals)
        t.append(['Average interarrival time',simulation_instance.clock/num_arrivals])

        final_arr_column.append('People who had to wait in line')
        final_arr_result.append(number_in_queue)
        t.append(['People who had to wait in line', number_in_queue])

        final_arr_column.append('Total average wait time')
        final_arr_result.append(total_wait_time)
        t.append(['Total average wait time', total_wait_time])

        final_arr_column.append('Lost Customers')
        final_arr_result.append(lost_customers)
        t.append(['Lost Customers', lost_customers])

        print("Columns of pandas are: ", final_arr_column)
        print("Values of columns are: ", final_arr_result)
        print("COLUMN LENGTH = ", len(final_arr_column))
        print("VALUES LENGTH = ", len(final_arr_result))

        print("-----------")
        print("This is the final arr merged with data: ")
        print(t)
        print("-----------")

        print("FINAL DATA IS:")
        print("[num_arrivals: %s, number_in_queue: %s, total_wait_time: %s, users_finished: %s, lost_customers: %s"%(num_arrivals, number_in_queue, total_wait_time, user_finished, lost_customers))
        
        df=pd.DataFrame(columns=final_arr_column)

        a=pd.Series(final_arr_result,index=df.columns)
            
        df=df.append(a,ignore_index=True)   
            
        df.to_excel('results_final.xlsx')



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()