#include <iostream>
#include <math.h>

// function to add the elements of two arrays
// CUDA kernel function
__global__
void add(int n, float *x, float *y) {
    for (int i = 0; i < n; i++)
        y[i] = x[i] + y[i];
}

int main(void) {
    int N = 1<<2; // 1M elements

    float *x, *y;
    cudaMalloc(&x, N*sizeof(float));
    cudaMalloc(&y, N*sizeof(float));

    // initialize x and y arrays on the host
    for (int i = 0; i < N; i++) {
        x[i] = 1.0f;
        y[i] = 2.0f;
    }

    /*
    // Run kernel on 1M elements on the CPU
    add<<<1, 1>>>(N, x, y);

    // Wait for GPU to finish before accessing on host/cpu.
    // Because GPU kernel launches don't block the cpu thread.
    cudaDeviceSynchronize();

    // Check for errors (all values should be 3.0f)
    float maxError = 0.0f;
    for (int i = 0; i < N; i++)
    maxError = fmax(maxError, fabs(y[i]-3.0f));
    std::cout << "Max error: " << maxError << std::endl;

    */
    // Free memory
    //delete [] x;
    //delete [] y;
    cudaFree(x);
    cudaFree(y);

    return 0;
}
