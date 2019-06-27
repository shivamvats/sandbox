#include <iostream>
#include <chrono>

constexpr long long unsigned int factorial_fast( long long unsigned int n ){
    return (n <= 1)? 1 : ( n*factorial_fast( n-1 ) );
}

long long unsigned int factorial( long long unsigned int n ){
    return (n <= 1)? 1 : ( n*factorial( n-1 ) );
}

void run_constexpr_factorial(){
    std::cout<<"\nFactorial using compile-time computation:\n";
    std::cout<<"=========================================\n";
    auto start_time = std::chrono::high_resolution_clock::now();
    constexpr int n = 20;
    for( int i=0; i<100000; i++ )
        static constexpr long long int f = factorial_fast(n);
    static constexpr long long int f = factorial_fast(n);
    std::cout<<"factorial("<<n<<"):\t"<<f<<"\n";
    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed_time = end_time - start_time;
    std::cout<<"Time taken: "<<elapsed_time.count()<<"s\n";

}

void run_normal_factorial(){
    std::cout<<"\nFactorial using run-time computation:\n:";
    std::cout<<"========================================\n";
    auto start_time = std::chrono::high_resolution_clock::now();
    int n = 20;
    for( int i=0; i<100000; i++ )
        static long long int f = factorial(n);
    static long long int f = factorial(n);
    std::cout<<"factorial("<<n<<"):\t"<<f<<"\n";
    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed_time = end_time - start_time;
    std::cout<<"Time taken: "<<elapsed_time.count()<<"s\n";


}

int main(){
    run_normal_factorial();
    run_constexpr_factorial();
}
