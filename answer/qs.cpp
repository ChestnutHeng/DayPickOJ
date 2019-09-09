// 快排，第k位，二分模板

#include <iostream>
#include <vector>
#include "com.h"

using namespace std;

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

int middle(int *arr, int lo, int hi, int k){
	if(lo >= hi && hi != k)return -1;
	int pivot = arr[hi];
	int end = hi;
	int start = lo;
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
	if(lo == k){
		return arr[lo];
	}else if(lo > k){
		return middle(arr, start, lo-1, k);
	}else{
		return middle(arr, lo+1, hi, k);
	}
}

int bs(int *arr, int size, int num){
	int lo = 0, hi = size-1;
	int mid;
	while(lo <= hi){
		mid = (lo + hi)/2;
		if (arr[mid] == num) return mid;
		if(arr[mid] < num)lo=mid+1;
		if(arr[mid] > num)hi=mid-1;
		//cout << lo << hi << endl;
	}
	return -1;
}

int main(){
	int size;
	int *arr = rd_arr<int>(size);
	qs(arr,0,size-1);
	print(arr, size);
	return 0;	
}