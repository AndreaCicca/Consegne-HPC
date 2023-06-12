# compilare tutti i file nella cartella corrente .c e .cpp
# nel caso dei file cpp bisogna usare g++-12 con il flag -fopenmp
# nel caso dei file c bisogna usare gcc-12 con il flag -fopenmp


# compilazione dei file .c

for file in *.c
do
    gcc -fopenmp -o ${file%.*} $file
done

# compilazione dei file .cpp

for file in *.cpp
do
    g++ -fopenmp -o ${file%.*} $file
done
