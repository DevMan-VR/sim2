class Server():
    def __init__(self, index, configuration, service_distribution,arrival_distribution, has_wait_queue, queue_capacity, service_time_list, arrival_time_list, server_current_queue_is_infinite, distribution_instance):  
        self.index = index
        self.configuration = configuration
        self.service_distribution = service_distribution
        self.arrival_distribution = arrival_distribution
        self.has_wait_queue = has_wait_queue
        self.queue_capacity = queue_capacity
        self.service_time_list = service_time_list
        self.arrival_time_list = arrival_time_list
        self.server_current_queue_is_infinite = server_current_queue_is_infinite

        #Hay que agregar una instancia de clase de distribucion aca...
        self.distribution_instance = distribution_instance

        #Initial Values
        self.server_state = 0
        self.n_waiting_in_queue = 0
        self.n_lost = 0
        self.service_time_sum = 0
        self.num_of_departures = 0

        if(self.index == 0): #Si es el primer servidor se declara en inf para que el primer evento sea de arrival
            self.t_departure = float('inf')
        else:
            self.t_departure = distribution_instance.random_gen()

    def __str__(self):
        return "\nServer %s:\n\n\nconfiguration: %s,\n\nservice_distribution: %s,\n\narrival_distribution: %s,\n\nhas_wait_queue: %s,\n\nqueue_capacity: %s,\n\nservice_time_list: %s,\n\narrival_time_list: %s\n\n\n END SERVER %s\n"%(self.index,self.configuration, self.service_distribution,self.arrival_distribution,self.has_wait_queue,self.queue_capacity,self.service_time_list,self.arrival_time_list,self.index) 

    def __repr__(self):
        return "\nServer %s:\n\n\nconfiguration: %s,\n\nservice_distribution: %s,\n\narrival_distribution: %s,\n\nhas_wait_queue: %s,\n\nqueue_capacity: %s,\n\nservice_time_list: %s,\n\narrival_time_list: %s\n\n\n END SERVER %s\n"%(self.index,self.configuration, self.service_distribution,self.arrival_distribution,self.has_wait_queue,self.queue_capacity,self.service_time_list,self.arrival_time_list,self.index) 

    def arriveOne(self):
        if(self.server_state == 0): #Si está desocupado
            self.scheduleDep()
        else:
            if(self.has_wait_queue): #Si tiene cola de espera
                if(self.server_current_queue_is_infinite): #Si la cola de espera es infinita entonces agregar a la cola
                    self.addOneToQueue()
                else:
                    if(self.n_waiting_in_queue <= self.queue_capacity): #Si aun queda cupo en la cola de espera
                        self.addOneToQueue()
                    else:
                        return


    def addOneToQueue(self):
        self.n_waiting_in_queue +=1         

    def scheduleDep(self):
        return

    def oneIsLost(self):
        self.n_lost +=1