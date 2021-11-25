import numpy as np
import pandas as pd
from main import Server_Sequential, Server_Parallel, Server

class Bank_Simulation:
    def __init__(self): 
        self.clock=0.0                      #simulation clock
        self.num_arrivals=0                 #total number of arrivals
        self.t_arrival=self.gen_int_arr()   #time of next arrival
        self.t_departure1=float('inf')      #departure time from server 1
        self.t_departure2=float('inf')      #departure time from server 2
        self.dep_sum1=0                     #Sum of service times by teller 1
        self.dep_sum2=0                     #Sum of service times by teller 2
        self.state_T1=0                     #current state of server1 (binary)
        self.state_T2=0                     #current state of server2 (binary)
        self.total_wait_time=0.0            #total wait time
        self.num_in_q=0                     #current number in queue
        self.number_in_queue=0              #customers who had to wait in line(counter)
        self.num_of_departures1=0           #number of customers served by teller 1  
        self.num_of_departures2=0           #number of customers served by teller 2 
        self.lost_customers=0               #customers who left without service
        self.num_in_system =0

        s1 = Server_Sequential(
            0,
            "Serie",
            "Exponencial",
            "Exponencial",
            "Si",
            12,
            [0.42517370703259294, 0.09726336864039875, 0.23955661130338748, 0.3360671398138247, 0.43208777839163753, 0.5374303390858318, 0.655690310815838, 0.7991153737088363, 0.9638570167369047, 1.1808860355858306, 1.4509442759425188, 1.8569303015070016, 2.66107207964126, 0.02245230585891572, 0.09262092049076234, 0.1574317455400764, 0.2290238760467772, 0.30934184648142216, 0.4004253587974034, 0.4991665700972886, 0.6141251017955583, 0.7442947808164402, 0.8950908323274944, 1.079338834542725, 1.321637578281982, 1.6466517552307296, 2.2826053430988216, 0.002569909445346255, 0.059783762461934856, 0.12303708882532848, 0.19276190627766726, 0.26731023340702476, 0.34985327442908015, 0.439676623613196, 0.5424879432787199, 0.6582966962122425, 0.8096574854364706, 0.9743242705027041, 1.1754869671838832, 1.443561708640214, 1.8525014004053661, 2.682427438102107, 0.023361752090408562, 0.08468257716183517, 0.14723436085059546, 0.2210495355351889, 0.29472948025392337, 0.3861192289532167, 0.4848849892178841, 0.5867468135471263, 0.7100174178646611, 0.8550151715548697, 1.0329194830853967, 1.26154164964056, 1.545524175778657, 2.0105203935762006, 3.180032087728349, 0.0393218231123653, 0.10169715132070481, 0.18060145625375126, 0.25455176807260144, 0.33590438122293975, 0.4378951105635477, 0.6197793383348881, 0.846179517587548, 1.459481562654753, 2.4072865291284775, 0.04849853722248575, 0.15418694880374215, 0.23066800480730237, 0.42144496825417177, 0.5621578792954229, 0.7036151207949806, 1.0871232232841739, 1.4973417530803805, 0.0716063277677363, 0.1520381684211708, 0.22629111786924733, 0.3316664094044164, 0.4799687844330706, 0.667127983610303, 0.9207634686533961, 1.2550319755273058, 1.5750652617534888, 2.055351858554964, 3.4394588050432393, 0.0439049604691819, 0.10858185314563211, 0.18118077738544427, 0.26848997058260876, 0.415825820357439, 0.5839600041089043, 0.8069419575386998, 1.1419868015454948, 1.7002809111604322, 3.6112500614000442, 0.16344726291422726, 0.26611550384769084, 0.41537296373104654],
            [1.548605591516429, 0.27810896340840435, 0.3480313868703567, 0.40563262472085115, 0.4594440619488181, 0.5154689955977658, 0.574719809759953, 0.6400273620122111, 0.7077115453455984, 0.7927485055804825, 0.8817659349120341, 1.0286097896779032, 1.2484442707853685, 1.6120066617089963, 2.2323539735849276, 0.0027792971728855575, 0.03537141200156045, 0.06655334482853272, 0.09572060587624892, 0.12618474816897693, 0.15661482376506203, 0.1899142922096002, 0.2241902994037247, 0.2606098762250818, 0.2991672767863743, 0.34089228189758775, 0.38945312081968797, 0.43867015520941144, 0.4899601084084944, 0.5459887981126125, 0.6065525765237211, 0.6727722289325591, 0.7457590708310438, 0.8289050573653807, 0.9245656233267514, 1.036289726873072, 1.1818830594222518, 1.3552253396086753, 1.5817174158380252, 1.9288813118232735, 2.723937664973704, 0.014475151163919038, 0.04110603384041101, 0.06916919496833401, 0.09668399326062566, 0.1271553291681622, 0.1581597231004328, 0.19133677380842862, 0.2264862355833459, 0.26422045364960356, 0.30323186238325883, 0.3443713460211076, 0.3886752959460114, 0.43526182004339375, 0.4853500291318145, 0.5377303636182208, 0.5974373580331478, 0.6591547234942047, 0.7313491771388768, 0.9243533146943979, 1.0453093983889215, 1.175305994350912, 1.3438815951714815, 1.5680277547072947, 1.9146076483588355, 2.651592230550503, 0.01292973324448024, 0.039586291055939894, 0.06753222475157328, 0.09645983338497702, 0.12626458757340053, 0.15760982539109714, 0.18883062171122783, 0.2286356939213943, 0.26593524893184955, 0.303255142996662, 0.3450348924684555, 0.3890102919144567, 0.436333497660955, 0.48774051006254904, 0.5434806198913559, 0.6036773071712531, 0.6696259000101269, 0.7442701943653978, 0.8285553229782157, 0.9229942880481306, 1.0264772725349651, 1.1559653529188036, 1.3169689331145908, 1.530293504462927, 1.8314042420017649, 2.395490241827876, 0.007192295087955767, 0.033676203472868455, 0.06076417535345444, 0.08910094575723282, 0.11882678458940577, 0.1500055095654636, 0.18313987736967954],
            
            )

        


    def time_adv(self):                                                       
        t_next_event=min(self.t_arrival,self.t_departure1,self.t_departure2)  
        self.total_wait_time += (self.num_in_q*(t_next_event-self.clock))
        self.clock=t_next_event
                
        if self.t_arrival<self.t_departure1 and self.t_arrival<self.t_departure2:
            self.arrival()
        elif self.t_departure1<self.t_arrival and self.t_departure1<self.t_departure2:
            self.teller1()
        else:
            self.teller2()

    def arrival(self):              
        self.num_arrivals += 1
        self.num_in_system += 1

        if self.num_in_q == 0:                                 #schedule next departure or arrival depending on state of servers
            if self.state_T1==1 and self.state_T2==1:
                self.num_in_q+=1
                self.number_in_queue+=1
                self.t_arrival=self.clock+self.gen_int_arr()
                
                
            elif self.state_T1==0 and self.state_T2==0:
                
                if np.random.choice([0,1])==1:
                    self.state_T1=1
                    self.dep1= self.gen_service_time_teller1()
                    self.dep_sum1 += self.dep1
                    self.t_departure1=self.clock + self.dep1
                    self.t_arrival=self.clock+self.gen_int_arr()

                else:
                    self.state_T2=1
                    self.dep2= self.gen_service_time_teller2()
                    self.dep_sum2 += self.dep2
                    self.t_departure2=self.clock + self.dep2
                    self.t_arrival=self.clock+self.gen_int_arr()

                    
            elif self.state_T1==0 and self.state_T2 ==1:       #if server 2 is busy customer goes to server 1
                self.dep1= self.gen_service_time_teller1()
                self.dep_sum1 += self.dep1
                self.t_departure1=self.clock + self.dep1
                self.t_arrival=self.clock+self.gen_int_arr()
                self.state_T1=1
            else:                                              #otherwise customer goes to server 2
                self.dep2= self.gen_service_time_teller2()
                self.dep_sum2 += self.dep2
                self.t_departure2=self.clock + self.dep2
                self.t_arrival=self.clock+self.gen_int_arr()
                self.state_T2=1
        
        elif self.num_in_q < 4 and self.num_in_q >= 1:       #if queue length is less than 4 generate next arrival and make customer join queue
            self.num_in_q+=1
            self.number_in_queue+=1                             
            self.t_arrival=self.clock + self.gen_int_arr()
            
        elif self.num_in_q == 4:                             #if queue length is 4 equal prob to leave or stay
            if np.random.choice([0,1])==0: 
                self.num_in_q+=1 
                self.number_in_queue+=1                 
                self.t_arrival=self.clock + self.gen_int_arr()
            else:
                self.lost_customers+=1
                
                
        elif self.num_in_q >= 5:                            #if queue length is more than 5 60% chance of leaving
            if np.random.choice([0,1],p=[0.4,0.6])==0:
                self.t_arrival=self.clock+self.gen_int_arr()
                self.num_in_q+=1 
                self.number_in_queue+=1 
            else:
                self.lost_customers+=1

    def teller1(self):                #departure from server 2
        self.num_of_departures1 += 1
        if self.num_in_q>0:
            self.dep1= self.gen_service_time_teller1()
            self.dep_sum1 += self.dep1
            self.t_departure1=self.clock + self.dep1
            self.num_in_q-=1
        else:
            self.t_departure1=float('inf') 
            self.state_T1=0                  
    
    def teller2(self):                #departure from server 1
        self.num_of_departures2 += 1
        if self.num_in_q>0:
            self.dep2= self.gen_service_time_teller2()
            self.dep_sum2 += self.dep2
            self.t_departure2=self.clock + self.dep2
            self.num_in_q-=1
        else:
            self.t_departure2=float('inf')
            self.state_T2=0

    def gen_int_arr(self):                                             #function to generate arrival times using inverse trnasform
        return (-np.log(1-(np.random.uniform(low=0.0,high=1.0))) * 3)
    
    def gen_service_time_teller1(self):                                #function to generate service time for teller 1 using inverse trnasform
        return (-np.log(1-(np.random.uniform(low=0.0,high=1.0))) * 1.2)
    
    def gen_service_time_teller2(self):                                #function to generate service time for teller 1 using inverse trnasform
        return (-np.log(1-(np.random.uniform(low=0.0,high=1.0))) * 1.5)
        





s=Bank_Simulation()
df=pd.DataFrame(columns=['Average interarrival time','Average service time teller1','Average service time teller 2','Utilization teller 1','Utilization teller 2','People who had to wait in line','Total average wait time','Lost Customers'])


for i in range(100):
    np.random.seed(i)
    s.__init__()
    while s.clock <= 240 :
        s.time_adv() 
    a=pd.Series([s.clock/s.num_arrivals,s.dep_sum1/s.num_of_departures1,s.dep_sum2/s.num_of_departures2,s.dep_sum1/s.clock,s.dep_sum2/s.clock,s.number_in_queue,s.total_wait_time,s.lost_customers],index=df.columns)
    df=df.append(a,ignore_index=True)   
    
df.to_excel('results.xlsx')