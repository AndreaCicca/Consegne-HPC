/*
  mpi_DataMining.c
- il Task 0 invia a tutti l'intero x tra 0 e 10 (esempio 7)
- Tutti i  processi generano ogni secondo un intero random tra 0 e 10
- chi trova il numero x  invia un messaggio agli altri con il numero trovato e termina
- tutti gli altri processi ricevono e stampano il valore ricevuto e il mittente, quindi  terminano

module load intel impi
mpicc mpi_DataMining.c -o mpi_DataMining
mpirun  mpi_DataMining
*/

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <mpi.h>

int main (int argc, char *argv[]) {
 MPI_Status status;
 MPI_Request request;
 int  MPIrank, MPIsize;
 int r, i, x, flag,  received;


 MPI_Init(&argc, &argv);
 MPI_Comm_rank(MPI_COMM_WORLD, &MPIrank);
 MPI_Comm_size(MPI_COMM_WORLD, &MPIsize);

 srand48((unsigned)time(NULL)*MPIrank); // inizializzazione del seme
 flag=0;


 if (MPIrank==0)   x=7; 

// invio di x da rank 0 a tutti gli altri 

 if (MPIrank == 0) 
 {  
    printf("SEND: Task %d/%d - x: %d\n", MPIrank, MPIsize, x); 
    for (i = 1; i < MPIsize; i++) 
    { 
      MPI_Send(&x, 1, MPI_INT, i, 666, MPI_COMM_WORLD); 
    } 
  } 
 else 
 { 
    MPI_Recv(&x, 1, MPI_INT, 0, 666, MPI_COMM_WORLD, &status);
    printf("RECV: Task %d/%d - x: %d\n", MPIrank, MPIsize, x);
 }

// attiva la ricezione asincrona non bloccante di x
MPI_Irecv(&received, 1, MPI_INT, MPI_ANY_SOURCE, 666, MPI_COMM_WORLD, &request);

 while(!flag)
 {
  sleep(1);
  MPI_Test( &request, &flag, &status);

  r=drand48()*10;    // intero random tra 0 e 10
  
  if(flag != 1)  
  {
    printf ("Task %d/%d - x:%d  r:%d \n", MPIrank, MPIsize,x, r);
  }

  if (r == x) 
   { 
  // invio a tutti di r 
    for (i = 0; i < MPIsize; i++) 
    { 
      MPI_Send(&r, 1, MPI_INT, i, 666, MPI_COMM_WORLD); 
    }
   }
}


 if(MPIrank != status.MPI_SOURCE)  
 {
   printf ("Task %d/%d - RECEIVED %d from %d, exiting ...\n", MPIrank, MPIsize, received,  status.MPI_SOURCE);
 }
 MPI_Finalize();
 return 0;
}