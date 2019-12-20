// 快排模板
#include "com.h"

int partition(int *arr, int lo, int hi){
	int pivot = arr[hi];
	int end = hi;
	while(lo < hi){
		while(arr[lo]<pivot && lo < hi)lo++;
		while(arr[hi]>=pivot && lo < hi)hi--;
		swap(arr[lo], arr[hi]);
	}
	if(pivot <=arr[lo]){
		swap(arr[lo], arr[end]);
	}else{
		lo++;
	}
	return lo;
}

void qs(int *arr, int lo, int hi){
	if(lo >= hi)return;
	int mid = partition(arr, lo, hi);
	qs(arr, lo, mid-1);
	qs(arr, mid+1, hi);
}


int main(){
	int size;
	int *arr = rd_arr<int>(size);
	qs(arr,0,size-1);
	print(arr, size);
	return 0;	
}