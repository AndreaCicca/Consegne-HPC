//gcc -fopenmp  sections.c  -o sections

#include <stdio.h>
#include <omp.h>

int main(int argc, char* argv[])
{
 int i;

 omp_set_nested(1);

 #pragma omp parallel private(i) num_threads(2)
 {

  #pragma omp sections
    {
       #pragma omp section 
         {
          printf("Master %d/%d \n",omp_get_thread_num(),omp_get_num_threads() );
         }

       #pragma omp section 
         {
         #pragma omp parallel for num_threads(8)
         for(i = 0; i < 8; i++)
         printf("Thr %d/%d : %d \n",omp_get_thread_num(),omp_get_num_threads(),i);
         }

    } // end sections 


  } // end parallel 
}


