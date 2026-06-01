#include <iostream>
#include <pthread.h>

typedef struct {
    int thread_id;
} thread_data_t;

void* thread_fn(void *arg){
    int tid = ((thread_data_t*) arg) -> thread_id;
    std::cout << "Hello from thread " << tid << "!" << std::endl;
    return nullptr;
}

int main(int argc, char **argv){
    int num_threads = 5;
    pthread_t tid[num_threads];
    thread_data_t args[num_threads];
    for (int i = 0; i < num_threads; i++){
        args[i].thread_id = i;
        pthread_create(&tid[i], nullptr, thread_fn, &args[i]);
    }
    for (int i = 0; i < num_threads; i++){
        pthread_join(tid[i], nullptr);
    }
    return 0;
}
