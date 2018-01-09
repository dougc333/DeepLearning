// -*- c++ -*-
#include <stdio.h>
#include <cuda.h>
#include <iostream>
#include <stdlib.h>
#include <ctime>

//http://www.nvidia.com/docs/IO/116711/sc11-cuda-c-basics.pdf is wrong

__global__ void add(int *a, int*b, int count){
  int id = blockIdx.x + blockDim.x + threadIdx.x;
  if(id < count){
    a[id] += b[id];
  }
}

using namespace std;

int main(int argc, char** argv){
  srand(time(NULL));
  int count = 100;
  int *h_a = new int[count];
  int *h_b = new int[count];

  for(int i=0;i<count;i++){
    h_a[i] = rand() % 1000;
    h_b[i] = rand() % 1000;
  }
  
  int *d_a, *d_b;
  
  cudaMalloc(&d_a, sizeof(int)*count);
  cudaMalloc(&d_b, sizeof(int)*count);


  cudaMemcpy(d_a, h_a, sizeof(int)*count,cudaMemcpyHostToDevice);
  cudaMemcpy(d_b, h_b, sizeof(int)*count,cudaMemcpyHostToDevice);

  add<<<count/256+1,256>>>(d_a, d_b,count);
  
  cudaMemcpy(h_a, d_a, sizeof(int)*count, cudaMemcpyDeviceToHost);

  for(int i=0;i<count;i++){
    cout<<h_a[i]<<","<<endl;
  }
  cudaFree(d_a);
  cudaFree(d_b);
  
  delete[] h_a;
  delete[] h_b;


  return 0;
}

