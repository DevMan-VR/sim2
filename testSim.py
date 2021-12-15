
import Server
from ServerParallel import Server_Parallel
from ServerSequential import Server_Sequential
#import ServerParallel
from Exponential import ExponentialClass
import numpy as np
import random
import pandas as pd
from SimLogic import Simulation

class Test():

    def __init__(self):

        s1 = Server_Sequential(
            0,
            "Serie",
            "Exponencial",
            "Exponencial",
            "Si",
            70,
            [],
            [],
            1,
            False,
            ExponentialClass(lambdaValue=0.7),
            ExponentialClass(lambdaValue=1)
        )

        s2 = Server_Sequential(
            1,
            "Serie",
            "Exponencial",
            "Exponencial",
            "Si",
            70,
            [],
            [],
            2,
            False,
            ExponentialClass(lambdaValue=0.8),
            ExponentialClass(lambdaValue=1)
        )

        s3 = Server_Sequential(
            2,
            "Serie",
            "Exponencial",
            "Exponencial",
            "Si",
            70,
            [],
            [],
            None,
            False,
            ExponentialClass(lambdaValue=0.5),
            ExponentialClass(lambdaValue=1)
        )


        server_list = [s1,s2,s3]
        sim = Simulation(server_list=server_list)
        
        while sim.server_list[0].num_arrivals < 300:
        #while sim.server_list[2].user_finished < 1 :
        #for i in range(1,30):
            sim.time_advance() 


        num_arrivals = 0
        number_in_queue = 0
        lost_customers = 0
        user_finished = 0
        num_arrivals = sim.server_list[0].num_arrivals
        for s in sim.server_list:
            number_in_queue += s.num_in_queue
            lost_customers += s.n_lost
            user_finished += s.user_finished
        
        
        t = []
        final_arr_column = []
        final_arr_result = []

        total_wait_time=0
        for s in sim.server_list:
            if(s.configuration == 'Serie'):

                if(s.dep_sum > 0):
                    op1 = s.num_of_departures/s.dep_sum
                else:
                    op1 = s.num_of_departures
                op2 = s.dep_sum / sim.clock
                
                final_arr_column.append('Average service time server '+str(s.index))
                final_arr_result.append(op1)
                t.append(['Average service time server '+str(s.index),op1])

                final_arr_column.append('Utilization server '+str(s.index))
                final_arr_result.append(op2)
                t.append(['Utilization server '+str(s.index),op2])

                #total_wait_time+=s.dep_sum


            else:
                if(s.dep_sum1 > 0):
                    op1_t1 = s.num_of_departures1/s.dep_sum1
                else:
                    op1_t1 = s.num_of_departures1
                op2_t1 = s.dep_sum1 / sim.clock
                
                final_arr_column.append('Average service time server T1 S')
                final_arr_result.append(op1_t1)
                t.append(['Average service time server T1 S', op1_t1])

                final_arr_column.append('Utilization server T1 S')
                final_arr_result.append(op2_t1)
                t.append(['Utilization server T1 S', op2_t1])

                op1_t2 = s.num_of_departures2/s.dep_sum2
                op2_t2 = s.dep_sum2 / sim.clock

                final_arr_column.append('Average service time server T2 S')
                final_arr_result.append(op1_t2)
                t.append(['Average service time server T2 S', op1_t2])

                final_arr_column.append('Utilization server T2 S')
                final_arr_result.append(op2_t2)
                t.append(['Utilization server T2 S',op2_t2])

                #total_wait_time+=s.dep_sum1
                #total_wait_time+=s.dep_sum2

        final_arr_column.append('Average interarrival time')
        final_arr_result.append(sim.clock/num_arrivals)
        t.append(['Average interarrival time',sim.clock/num_arrivals])

        final_arr_column.append('People who had to wait in line')
        final_arr_result.append(number_in_queue)
        t.append(['People who had to wait in line', number_in_queue])


        total_wait_time = sim.total_wait_time
        final_arr_column.append('Total average wait time')
        final_arr_result.append(total_wait_time)
        t.append(['Total average wait time', total_wait_time/num_arrivals])

        final_arr_column.append('Lost Customers')
        final_arr_result.append(lost_customers)
        t.append(['Lost Customers', lost_customers])

        final_arr_column.append('Users Finished')
        final_arr_result.append(user_finished)

        print("Columns of pandas are: ", final_arr_column)
        print("Values of columns are: ", final_arr_result)
        print("COLUMN LENGTH = ", len(final_arr_column))
        print("VALUES LENGTH = ", len(final_arr_result))

        print("-----------")
        print("This is the final arr merged with data: ")
        print(t)
        print("-----------")

        print("FINAL DATA IS:")
        print("[num_arrivals: %s, total_wait_time: %s, users_finished: %s, lost_customers: %s"%(num_arrivals, total_wait_time, user_finished, lost_customers))
        print("Average wait time: ", total_wait_time/num_arrivals)
        print("Total en cola de espera: ", number_in_queue)
        
        print("Estado servidor 1: ", sim.server_list[0].server_state)
        print("Estado servidor 2: ", sim.server_list[1].server_state)
        print("Estado servidor 3: ", sim.server_list[2].server_state)

       # print("En arrivo en servidor 1: ", sim.server_list[0].t_arrival)
       # print("En arrivo en servidor 2: ", sim.server_list[1].t_arrival)
       # print("En arrivo en servidor 3: ", sim.server_list[2].t_arrival)

        print("Por llegar a servidor 2", sim.server_list[1].t_almost_arriving )
        print("Por llegar a servidor 3", sim.server_list[2].t_almost_arriving )



        print("lost costumer in 1,2,3", sim.server_list[0].n_lost,sim.server_list[1].n_lost,sim.server_list[2].n_lost)
        df=pd.DataFrame(columns=final_arr_column)
        a=pd.Series(final_arr_result,index=df.columns)
        df=df.append(a,ignore_index=True)    
        df.to_excel('results4.xlsx')
    

test = Test()