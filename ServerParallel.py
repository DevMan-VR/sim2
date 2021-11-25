import Server
from SimLogic import Simulation
class Server_Parallel(Server):
    def __init__(self, index, configuration, service_distribution, arrival_distribution, has_wait_queue, queue_capacity,server_time_list, arrival_time_list, next_server_up_index,next_server_down_index,server_current_queue_is_infinite,distribution_instance):
        super().__init__(index, configuration,service_distribution, arrival_distribution, has_wait_queue, queue_capacity,server_time_list, arrival_time_list,server_current_queue_is_infinite,distribution_instance)
        self.next_server_up_index = next_server_up_index
        self.next_server_down_index = next_server_down_index

        # Parent Values Inherited:
        # self.server_state = 0
        # self.n_waiting_in_queue = 0
        # self.n_lost = 0
        # self.service_time_sum = 0
        # self.num_of_departures = 0
        # self.t_departures = []
        # self.distribution_instance (Instance of Class distribution)


    def pushToNextUp(self):
        Simulation.pushToNext(self.next_server_up_index)

    def pushToNextDown(self):
        Simulation.pushToNext(self.next_server_down_index)

    def departure(self):
        if(self.n_waiting_in_queue >= 1): #Si queda solo 1 en la cola de espera, se resta ese 1, se deja el servidor disponible y se llama al pushToNext
            self.n_waiting_in_queue -= 1
            self.server_state = 0
            #self.pushToNext()

        elif(self.n_waiting_in_queue == 0): #Si no hay espera, el server queda disponible y se llama el pushToNext
            self.server_state = 0
            #self.pushToNext()

#Falta implementar la logica para determinar si el push se hace hacia arriba o hacia abajo