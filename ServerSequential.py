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
        #print("##############")
        #print("Server index "+str(self.index)+" has a t_almost_arriving of: ")
        #print(self.t_almost_arriving)
        #print("##############")

        next_arrival = float("inf")
        if(self.index == 0):
            next_arrival = self.t_arrival
        else:
            if(len(self.t_almost_arriving) == 0):
                next_arrival = float("inf")
            else:
                index_min = min(range(len(self.t_almost_arriving)), key=self.t_almost_arriving.__getitem__)
                next_arrival = self.t_almost_arriving[index_min]
                self.index_current_almost_arriving = index_min
    


        if(self.t_departure < next_arrival):
            self.min_attr_name = "departure"
            return self.t_departure

        else:
            self.min_attr_name = "arrival"
            return next_arrival

        


    def arriveOneAtTime(self,new_t_arrival):
        print("new arrival is in: ", new_t_arrival)

        if(self.index == 0):
            self.t_arrival = new_t_arrival
        else:
            self.t_almost_arriving.append(new_t_arrival)


    def addOneToQueue(self):
        self.num_in_queue +=1         


    def oneIsLost(self):
        self.n_lost +=1
    

    def manageNewArrival(self):
        if(self.index == 0): #Si es el primer servidor, se debe generar un nuevo time, sino se pregunta si tiene por un usuario por llegar
            self.t_arrival = self.simulation_instance.clock + abs(self.arrival_distribution_instance.random_gen())
            #self.num_arrivals += 1
        else:
            if(len(self.t_almost_arriving) > 0):
                #Si hay usuarios por llegar se asigna el nuevo t como el time del menor
                index_min = min(range(len(self.t_almost_arriving)), key=self.t_almost_arriving.__getitem__)
                self.t_arrival = self.t_almost_arriving[index_min]
                del self.t_almost_arriving[index_min] ##remove element from array
            else:
                #Si no hay usuarios por llegar se define el t_arrival como inf hasta que llegue un nuevo usuario
                self.t_arrival = float("inf")

    def arrival(self):

        self.num_arrivals += 1
        print("ARRIVAL ::: CURRENT t_arrival IS: ", self.t_arrival)

        if(self.server_state == 1):
            if(self.has_wait_queue == 'Si'):
                if(self.server_current_queue_is_infinite == False):
                    if(self.num_in_queue < self.queue_capacity):
                        self.num_in_queue += 1
                        self.manageNewArrival()
                                
                    else:
                        self.oneIsLost()
                        print("ONE IS LOST BABY DON'T HURT ME DON'T HURT ME NO MORE")
                        self.manageNewArrival()
                else:
                    self.num_in_queue += 1
                    self.manageNewArrival()
            else:
                self.oneIsLost()
                print("ONE IS LOST BABY DON'T HURT ME DON'T HURT ME NO MORE")
                self.manageNewArrival()
        else:
            #Server disponible
            self.server_state = 1
            dep = abs(self.service_distribution_instance.random_gen())
            self.dep_sum += dep
            self.t_departure = self.simulation_instance.clock + dep
            self.manageNewArrival()

        
        print("ARRIVAL ::: NEW t_arrival IS: ", self.t_arrival)


    def departure(self):#Agregar caso de si es infinita, o de si no tiene queue
        print("ARRIVAL ::: CURRENT t_departure IS: ", self.t_arrival)
        if(self.num_in_queue == 0):
            self.t_departure = float("inf")
            self.server_state = 0
            self.userToNextServer()
            self.num_of_departures +=1
        else:
            dep = abs(self.service_distribution_instance.random_gen())
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
        return "\nServer Sequential %s: [self.server_state: %s, self.num_in_queue: %s,self.t_departure: %s,self.t_arrival: %s,server_almost_arriving: %s END SERVER] %s\n"%(self.index, self.server_state,self.num_in_queue,self.t_departure,self.t_arrival,self.t_almost_arriving,self.index) 

    def __repr__(self):
        return "\nServer Sequential %s: [self.server_state: %s, self.num_in_queue: %s,self.t_departure: %s,self.t_arrival: %s,server_almost_arriving: %s END SERVER] %s\n"%(self.index, self.server_state,self.num_in_queue,self.t_departure,self.t_arrival,self.t_almost_arriving,self.index) 

