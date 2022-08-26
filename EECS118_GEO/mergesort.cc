/**
 *  \file mergesort.cc
 *
 *  \brief Implement your mergesort in this file.
 */

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "sort.hh"




void mergehalf(keytype* a,int min, int max, int mid){
	int *temp = new int[max-min+1];
	int f = min;
	int g = mid+1;
	int index = 0;
	
	
	while(f <= mid && g <= max){
		if(a[f] < a[g]){
			temp[index] = &a[f];
			f = f+1;
		}
		else{
			temp[index] = &a[g];
			g = g+1;
		}
		index = index+1;
	}
	printf("\n f \n");
	while(f <= mid){
		printf("MID");
		temp[index] = &a[f]; 
		index = index+1;
		f = f+1;
	}
	printf("\n g \n");
	while(g <= max){
		printf("MAX");
		temp[index] = &a[g];
		index++;
		g++;
	}
	printf("ok 2");
	//please work; 
	for(int n = 0;min<=max;n++){
		printf("A:%d  ->  T: %d", a[min],temp[n]);
		a[min] = temp[n];
		min++;
		
	}
	
	//free(temp);
	//delete[] temp;
	//free(a);
	//delete[] a;
	
}


void mergesort(keytype* a, int min, int max){
	printf("\n made merge sort \n");
	if(min >= max){ //End recursion, size 1 arrays
		return;
		printf("size1 good");
	}
	else{
		int mid = (min + max)/2;
	
		
		mergesort(a, min,mid); //min to mid
		mergesort(a, mid+1,max); //mid+1 to max
		printf("\n merge sort done \n");
		mergehalf(a, min,max,mid);
		printf("\n merge half done \n");
	}
	
}

void mySort (int N, keytype* A)
{
	printf("\n \n MY sort \n \n");
	mergesort(A,0,N);
} 



/* eof */
