	//gcc -fopenmp master-slave.c

#include <stdio.h>
#include <omp.h>

int request, response;

omp_lock_t master;
omp_lock_t slave;

int request_new_work(int t)
{
   request=t;
   omp_unset_lock(&master); // request is ready
   omp_set_lock(&slave);    // waiting fo answer
   omp_test_lock(&master);   // block master
   return (response);
}

int main(int argc, char* argv[])
{
 int i;

 omp_init_lock(&master);
 omp_init_lock(&slave);

 omp_set_lock(&master);
 omp_set_lock(&slave);

 omp_set_nested(1);

 srand48((unsigned)time(NULL));

 #pragma omp parallel private(i) num_threads(2)
 {

  #pragma omp sections
    {
       #pragma omp section // master 
           while(1)
           { 
             omp_set_lock(&master);
             printf("Master: received request from %d  resp: %d \n", request, ++response);
             omp_unset_lock(&slave);
             omp_test_lock(&master);
         }

       #pragma omp section //slave
         {
         #pragma omp parallel  num_threads(4)
           {
            int block_num=0;
            float x; 
            int t=omp_get_thread_num();
           
            while(1) 
            {
//              printf ("Slave %d: calling request of work.. \n",t);  
              #pragma omp critical
              block_num=request_new_work(t);

              printf ("Slave  %d: working on %d \n",t,block_num);  
              usleep(1000000);

            } // end while

           } // end parallel
         
       } // end section 

    } // end sections 
  } // end parallel 

omp_destroy_lock(&master);
omp_destroy_lock(&slave);
}
