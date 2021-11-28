from SimLogic import Simulation

class Server_Sequential():
    def __init__(self, index, configuration, service_distribution,arrival_distribution, has_wait_queue, queue_capacity, service_time_list, arrival_time_list, next_server_index, server_current_queue_is_infinite,service_distribution_instance,arrival_distribution_instance):  
        #super().__init__(index,configuration,service_distribution,arrival_distribution,has_wait_queue,queue_capacity,server_time_list, arrival_time_list, server_current_queue_is_infinite,distribution_instance)
        
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
        self.service_distribution_instance = service_distribution_instance
        self.arrival_distribution_instance = arrival_distribution_instance

        #Initial Values
        self.next_server_index = next_server_index
        
        self.server_state = 0
        self.n_lost = 0
        self.dep_sum = 0
        self.num_of_departures = 0

        self.t_departure = float("inf")
        self.t_arrival = float("inf")

        self.min_attr_name = None

        self.num_arrivals = 0

        self.num_in_queue = 0
        self.simulation_instance = None

        self.user_finished = 0

        self.t_almost_arriving = []
        self.index_current_almost_arriving = None

    
    def setSimulationInstance(self,instance):
        self.simulation_instance = instance

    def getAndSetMinTimeEvent(self):

        if(self.t_departure < self.t_arrival):
            self.min_attr_name = "departure"
            return self.t_departure

        else:
            self.min_attr_name = "arrival"
            return self.t_arrival


    def arriveOneAtTime(self,new_t_arrival):
        print("new arrival is in: ", new_t_arrival)
        self.t_arrival = new_t_arrival


    def addOneToQueue(self):
        self.num_in_queue +=1         


    def oneIsLost(self):
        self.n_lost +=1
    

    def arrival(self):

        self.num_arrivals += 1
        print("ARRIVAL ::: CURRENT t_arrival IS: ", self.t_arrival)

        if(self.server_state == 1):
            if(self.has_wait_queue == 'Si'):
                if(self.server_current_queue_is_infinite == False):
                    if(self.num_in_queue < self.queue_capacity):
                        self.num_in_queue += 1
                        self.t_arrival = self.simulation_instance.clock + self.arrival_distribution_instance.random_gen()
                    else:
                        self.oneIsLost()
                        print("ONE IS LOST BABY DON'T HURT ME DON'T HURT ME NO MORE")
                        self.t_arrival = self.simulation_instance.clock + self.arrival_distribution_instance.random_gen()
                else:
                    self.num_in_queue += 1
                    self.t_arrival = self.simulation_instance.clock + self.arrival_distribution_instance.random_gen()
            else:
                self.oneIsLost()
                print("ONE IS LOST BABY DON'T HURT ME DON'T HURT ME NO MORE")
                self.t_arrival = self.simulation_instance.clock + self.arrival_distribution_instance.random_gen()
        else:
            #Server disponible
            self.server_state = 1
            dep = self.service_distribution_instance.random_gen()
            self.dep_sum += dep
            self.t_departure = self.simulation_instance.clock + dep
            self.t_arrival = self.simulation_instance.clock + self.arrival_distribution_instance.random_gen()

        
        print("ARRIVAL ::: NEW t_arrival IS: ", self.t_arrival)


    def departure(self):#Agregar caso de si es infinita, o de si no tiene queue
        print("ARRIVAL ::: CURRENT t_departure IS: ", self.t_arrival)
        if(self.num_in_queue == 0):
            self.t_departure = float("inf")
            self.server_state = 0
            self.userToNextServer()
            self.num_of_departures +=1
        else:
            dep = self.service_distribution_instance.random_gen()
            self.dep_sum += dep
            self.t_departure = self.simulation_instance.clock + dep
            self.num_in_queue -= 1
            self.userToNextServer()
            self.num_of_departures +=1
        
        print("DEPARTURE ::: NEW t_departure IS: ", self.t_departure)

    def userToNextServer(self):
        if(self.next_server_index == None):
            self.user_finished +=1
        else:
            self.simulation_instance.pushToNext(index=self.next_server_index)
    
    def getMinDepartureTime(self):
        return self.t_departure

    def __str__(self):
        return "\nServer Sequential %s:\nconfiguration: %s,\nService distribution instance: %s\nArrival distribution instance:%s \nself.server_state: %s,\n\nself.num_in_queue: %s,\n\nhas_wait_queue: %s,\n\nqueue_capacity: %s,\n\nself.t_departure: %s,\n\nself.t_arrival: %s\n\nserver_almost_arriving: %s\n\nEND SERVER %s\n"%(self.index,self.configuration,self.service_distribution_instance,self.arrival_distribution_instance, self.server_state,self.num_in_queue,self.has_wait_queue,self.queue_capacity,self.t_departure,self.t_arrival,self.t_almost_arriving,self.index) 

    def __repr__(self):
        return "\nServer Sequential %s:\nconfiguration: %s,\nService distribution instance: %s\nArrival distribution instance:%s \nself.server_state: %s,\n\nself.num_in_queue: %s,\n\nhas_wait_queue: %s,\n\nqueue_capacity: %s,\n\nself.t_departure: %s,\n\nself.t_arrival: %s\n\nserver_almost_arriving: %s\n\nEND SERVER %s\n"%(self.index,self.configuration,self.service_distribution_instance,self.arrival_distribution_instance, self.server_state,self.num_in_queue,self.has_wait_queue,self.queue_capacity,self.t_departure,self.t_arrival,self.t_almost_arriving,self.index) 

