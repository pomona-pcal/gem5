#include <iostream>
#include <thread>
#include <chrono>

static bool events_done = false;
// simulate an event queue with an array of events
int events[100];

void producer_func()
{
    std::cout << "Producer is beginning simulation..." << std::endl;
    while (!events_done){
        std::cout << "producer is waiting for consumer to finish..." << std::endl;
        std::this_thread::sleep_for(std::chrono::milliseconds(750));
    }
}

void consumer_func()
{
    std::cout << "Consumer is beginning work..." << std::endl;
    // do work on events until the producer signals that events are done

    for (int event: events){
        std::cout << "Consumer is working on event: " << event << std::endl;
        std::this_thread::sleep_for(std::chrono::milliseconds(250));
    }

    events_done = true;
}

int main()
{
    for (int i = 0; i < 100; i++){
        events[i] = i + 1;
    }
    std::cout << "Program beginning" << std::endl;

    std::thread producer(producer_func);
    std::thread consumer(consumer_func);

    consumer.join();
    std::cout << "Consumer finished work" << std::endl;

    producer.join();
    std::cout << "Producer ending simulation" << std::endl;

}
