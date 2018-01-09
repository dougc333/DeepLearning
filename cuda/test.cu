// -*- c++ -*-
#include <stdio.h>
#include <cuda.h>
#include <iostream.h>
#include <stdlib.h>
#include <ctime>

//http://www.nvidia.com/docs/IO/116711/sc11-cuda-c-basics.pdf is wrong

__global__ void add(int *a, int*b, int*c){
  *c = *b + *a;
}

int main(int argc, char** argv){
  int a,b,c;
  int *d_a, *d_b, *d_c;

  cudaMalloc((void **)&d_a, sizeof(void**));
  cudaMalloc((void **)&d_b, sizeof(void**));
  cudaMalloc((void **)&d_c, sizeof(void**));
  a = 2;
  b = 7;

  cudaMemcpy(d_a, &a, sizeof(d_a),cudaMemcpyHostToDevice);
  cudaMemcpy(d_b, &b, sizeof(d_b),cudaMemcpyHostToDevice);

  add<<<1,1>>>(d_a, d_b, d_c);
  cudaMemcpy(&c, d_c, sizeof(d_c), cudaMemcpyDeviceToHost);
  cudaFree(d_a);
  cudaFree(d_b);
  cudaFree(d_c);
  printf("%d", c);
  printf("asdfasdfasdf\n");
  return 0;
}

