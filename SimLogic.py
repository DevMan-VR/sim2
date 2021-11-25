# Esta clase requiere como argumento:
# La lista de servidores conectados por indice
# Una instancia de clase de distribución de llegada con sus parametros cargados


class Simulation ():
    def __init__(self, server_list, arrival_distribution_instance):
        self.server_list = server_list #List of CLASS SERVER SEQUENTIAL AND PARALLEL

        self.num_arrivals=0 #total number of arrivals
        self.total_wait_time=0.0
        self.number_in_queue=0 #customers who had to wait in line(counter)
        self.lost_customers=0 #customers who left without service
        self.customers_in_system =0
        self.clock=0.0 # Clock
        self.arrival_distribution_instance = arrival_distribution_instance             
        self.t_arrival=self.arrival_distribution_instance.gen_random() #Genera un numero aleatorio apartir de su distribución y con los parametros que ya tiene cargado

    
    def time_advance(self):

        dep_array = [self.t_arrival]
        current_total_waiting_q = 0

        for s in self.server_list:
            dep_array.append(s.t_departure)
            current_total_waiting_q += s.n_waiting_in_queue
        
        index_min = min(range(len(dep_array)), key=dep_array.__getitem__)

        t_next_event = self.server_list[index_min].t_departure 
        self.total_wait_time += (current_total_waiting_q*(t_next_event-self.clock))
        self.clock = t_next_event


        if(index_min == 0): # Event is arrival
            self.arriveToFirst()
        else: 
            # Cada servidor se hace cargo de hacer departure de si mismo segun su configuracion y luego de propagar ese evento si es necesario
            # El evento de departure en un servidor puede provocar el evento de arriveOne en su siguiente servidor conectado
            self.server_list[index_min].departure()
        
        

    def evaluateAndManageNextEvent(self):
        return


    def arriveToFirst(self):
        self.server_list[0].arriveOne()
    
    

    def pushToNext(self, index):
        self.server_list[index].arriveOne()

    

        