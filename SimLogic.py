# Esta clase requiere como argumento:
# La lista de servidores conectados por indice
# Una instancia de clase de distribución de llegada con sus parametros cargados


class Simulation ():
    def __init__(self, server_list):
        self.server_list = server_list #List of CLASS SERVER SEQUENTIAL AND PARALLEL

        self.num_arrivals=0 #total number of arrivals
        self.total_wait_time=0.0
        self.number_in_queue=0 #customers who had to wait in line(counter)
        self.lost_customers=0 #customers who left without service
        self.customers_in_system =0
        self.clock=0.0 # Clock


        self.initialize_first_server()
        self.show_init_data()

        for s in self.server_list:
            s.setSimulationInstance(instance=self)
    
    def initialize_first_server(self):
        #Inicializar el primer servidor con tiempo de llegada de modo que sea este quien reciba el evento
        self.server_list[0].t_arrival = self.server_list[0].arrival_distribution_instance.random_gen()

    def show_init_data(self):
        #print("t_arrival is: ", self.t_arrival)
        if(self.server_list[0].configuration == 'Serie'):
            print("t_departure is: ",self.server_list[0].t_departure )
        elif(self.server_list[0].configuration == 'Paralelo'):
            print("t_departure_up is: ", self.server_list[0].t_departure_up)
            print("t_departure_down is: ", self.server_list[0].t_departure_down)


    def time_advance(self): #Las llegadas solo pueden ocurrir al primer servidor
        # Hay 2 casos, que el primer servidor sea secuencial o sea paralelo

        t_next_event = None
        users_total_waiting = 0
        arr = []

        for s in self.server_list:
            arr.append(s.getAndSetMinTimeEvent())
            users_total_waiting += s.num_in_queue


        print("SERVERS DATA ARE: " )
        for r in self.server_list:
            print(r)

        print("SERVER_LIST EVENTS ARE: ", arr)
        print("CLOCK IS: ", self.clock)

        

        t_next_event = min(arr)
        self.total_wait_time += users_total_waiting * (t_next_event-self.clock)
        self.clock = t_next_event
        
        
        index_min = min(range(len(arr)), key=arr.__getitem__)
        print("min index is: ", index_min)

        actingServer = self.server_list[index_min]
        print("Current acting server is: ", actingServer) 
        print("Acting Server attr_name event is: ",actingServer.min_attr_name )
        print("t_next_event IS: ", t_next_event)

        
        if(actingServer.min_attr_name == 'arrival'):
            actingServer.arrival()
        
        elif(actingServer.min_attr_name == 'min_almost_arriving'):
            actingServer.almostToArrived()
        else:
            actingServer.departure()
    

    

    def arriveToFirst(self):
        self.server_list[0].arriveOne()
    
    
    def pushToNext(self, index):
        self.server_list[index].arriveOneAtTime(new_t_arrival=(self.clock + self.server_list[index].arrival_distribution_instance.random_gen()))
        
    
    

        