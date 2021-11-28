from SimLogic import Simulation
import numpy as np

class Server_Parallel():
    def __init__(self, index, configuration, service_distribution,arrival_distribution, has_wait_queue, queue_capacity, service_time_list, arrival_time_list, next_server_up_index,next_server_down_index, server_current_queue_is_infinite,service_distribution_instance,arrival_distribution_instance):  
        
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
        self.next_server_up_index = next_server_up_index
        self.next_server_down_index = next_server_down_index
        
        self.state_T1 = 0
        self.state_T2 = 0
        self.dep_sum1 = 0
        self.dep_sum2 = 0

        self.n_lost = 0
        self.service_time_sum = 0
        self.num_of_departures1 = 0
        self.num_of_departures2 = 0

        self.t_arrival = float("inf")
        self.t_departure1 = float("inf")
        self.t_departure2 = float("inf")

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


        if(
            self.t_departure2 < self.t_arrival and 
            self.t_departure2 < self.t_departure1
        ):
            self.min_attr_name = "departure2"
            return self.t_departure2

        elif(
            self.t_departure1 < self.t_arrival and 
            self.t_departure1 < self.t_departure2
        ):
            self.min_attr_name = "departure1"
            return self.t_departure1

        else:
            self.min_attr_name = "arrival"
            return self.t_arrival

    def arriveOneAtTime(self,new_t_arrival):
        self.t_arrival = new_t_arrival



    def addOneToQueue(self):
        self.num_in_queue +=1         


    def oneIsLost(self):
        self.n_lost +=1
    

    def arrival(self):              
        self.num_arrivals += 1
        print("Server Doing is Server n° ",self.index)
        print("Entering to Arrival event on Parallel Server...")
        if (self.state_T1==1 and self.state_T2==1):
            print("Entering to case when both are busy")
            if(self.has_wait_queue == 'Si'):
                if(self.server_current_queue_is_infinite == False):
                    if(self.num_in_queue < self.queue_capacity):
                        #Todavia hay cupo
                        self.num_in_queue +=1
                        self.t_arrival=self.simulation_instance.clock+self.arrival_distribution_instance.random_gen()
                    else:
                        self.oneIsLost()
                else:
                    self.num_in_queue += 1
                    self.t_arrival=self.simulation_instance.clock+self.arrival_distribution_instance.random_gen()
            else:
                self.oneIsLost()
        
        elif(self.state_T1==0 and self.state_T2==0):
            print("Entering in case when two servers are available")
            if np.random.choice([0,1])==1:
                print("Case that chooses T1")
                self.state_T1=1
                dep1= self.service_distribution_instance.random_gen()
                self.dep_sum1 += dep1
                self.t_departure1=self.simulation_instance.clock + dep1
                self.t_arrival=self.simulation_instance.clock+self.arrival_distribution_instance.random_gen()
                print("NEW DEPARTURE SCHEDULED ::: t_departure1 is: ", self.t_departure1)

            else:
                print("Case that chooses T2")
                self.state_T2=1
                self.dep2= self.service_distribution_instance.random_gen()
                self.dep_sum2 += self.dep2
                self.t_departure2=self.simulation_instance.clock + self.dep2
                self.t_arrival=self.simulation_instance.clock+self.arrival_distribution_instance.random_gen()
                print("NEW DEPARTURE SCHEDULED ::: t_departure2 is: ", self.t_departure2)
        
        elif(self.state_T1==0 and self.state_T2==1):
            print("Case t1 is avaible and t2 is busy")
            self.state_T1=1
            dep1= self.service_distribution_instance.random_gen()
            self.dep_sum1 += dep1
            self.t_departure1=self.simulation_instance.clock + dep1
            self.t_arrival=self.simulation_instance.clock+self.arrival_distribution_instance.random_gen()
            print("NEW DEPARTURE SCHEDULED ::: t_departure1 is: ", self.t_departure1)
        
        elif(self.state_T1==1 and self.state_T2==0):
            print("Case t1 is busy and t2 is available")
            self.state_T2=1
            self.dep2= self.service_distribution_instance.random_gen()
            self.dep_sum2 += self.dep2
            self.t_departure2=self.simulation_instance.clock + self.dep2
            self.t_arrival=self.simulation_instance.clock+self.arrival_distribution_instance.random_gen()
            print("NEW DEPARTURE SCHEDULED ::: t_departure2 is: ", self.t_departure2)
        else:
            print("Entering in an error state")

        
        print("SERVER PARALLEL N°"+str(self.index)+" ARRIVAL ::: NEW t_arrival IS: ", self.t_arrival)


    def departure(self):#Agregar caso de si es infinita, o de si no tiene queue
        print("SERVER PARALLEL N°"+str(self.index)+" DEPARTURE ::: CURRENT t_departure1 IS: ", self.t_departure1)
        print("SERVER PARALLEL N°"+str(self.index)+" DEPARTURE ::: CURRENT t_departure2 IS: ", self.t_departure2)

        if(self.min_attr_name == 'departure1'):
            if(self.num_in_queue == 0):
                self.t_departure1 = float("inf")
                self.state_T1 = 0
                self.userToNextServerUp()
                self.num_of_departures1 +=1
            else:
                dep = self.service_distribution_instance.random_gen()
                self.dep_sum1 += dep
                self.t_departure1 = self.simulation_instance.clock + dep
                self.num_in_queue -= 1
                self.userToNextServerUp()
                self.num_of_departures1 +=1

        elif(self.min_attr_name == 'departure2'):
            if(self.num_in_queue == 0):
                self.t_departure2 = float("inf")
                self.state_T2 = 0
                self.userToNextServerDown()
                self.num_of_departures2 +=1
            else:
                dep = self.service_distribution_instance.random_gen()
                self.dep_sum2 += dep
                self.t_departure2 = self.simulation_instance.clock + dep
                self.num_in_queue -= 1
                self.userToNextServerDown()
                self.num_of_departures2 +=1
    
        print("SERVER PARALLEL N°"+str(self.index)+" DEPARTURE ::: CURRENT t_departure1 IS: ", self.t_departure1)
        print("SERVER PARALLEL N°"+str(self.index)+" DEPARTURE ::: CURRENT t_departure2 IS: ", self.t_departure2)

            

    def userToNextServerUp(self):
        if(self.next_server_up_index == None):
            self.user_finished +=1
        else:
            self.simulation_instance.pushToNext(index=self.next_server_up_index)
    
    def userToNextServerDown(self):
        if(self.next_server_down_index == None):
            self.user_finished +=1
        else:
            self.simulation_instance.pushToNext(index=self.next_server_down_index)
    
    def getMinDepartureTime(self):
        return min(self.t_departure1, self.t_departure2)

    def __str__(self):
        return "\nServer Parallel %s:\n\n\nconfiguration: %s,\n\nself.server_state_1: %s,\n\nself.server_state_2: %s,\n\nself.num_in_queue: %s,\n\nhas_wait_queue: %s,\n\nqueue_capacity: %s,\n\nself.t_departure1: %s,\n\nself.t_departure2: %s\n\nself.t_arrival: %s\n\n\n END SERVER %s\n"%(self.index,self.configuration, self.state_T1,self.state_T2,self.num_in_queue,self.has_wait_queue,self.queue_capacity,self.t_departure1,self.t_departure2,self.t_arrival,self.index) 

    def __repr__(self):
        return "\nServer Parallel %s:\n\n\nconfiguration: %s,\n\nself.server_state_1: %s,\n\nself.server_state_2: %s,\n\nself.num_in_queue: %s,\n\nhas_wait_queue: %s,\n\nqueue_capacity: %s,\n\nself.t_departure1: %s,\n\nself.t_departure2: %s\n\nself.t_arrival: %s\n\n\n END SERVER %s\n"%(self.index,self.configuration, self.state_T1,self.state_T2,self.num_in_queue,self.has_wait_queue,self.queue_capacity,self.t_departure1,self.t_departure2,self.t_arrival,self.index) 


