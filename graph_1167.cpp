#include <iostream>
#include <stdio.h>
	
typedef struct vertex{
	int ID;
	int* adjacency_vertex;
	int* edge_weight;
}vertex;

int main() {
	vertex* metrix;
	int size;
	
	scanf("%d", &size);
	metrix = new vertex[size];
	
	printf("%d",1);
	return 0;
}
