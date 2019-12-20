// 二分模板

#include "com.h"


int bs(int *arr, int size, int tar){
	int lo = 0, hi = size - 1;
	int mid;
	while(lo <= hi){
		mid = (lo + hi)/2;
		if (arr[mid] == tar){
			return mid;
		}else if(arr[mid] > tar){
			hi = mid - 1;
		}else{
			lo = mid + 1;
		}
	}
	return -1;
}

int main(){
	int size;
	int *arr = rd_arr<int>(size);
	int tar = rd_val<int>();
	int ind = bs(arr,size, tar);
	cout << ind << endl;
	return 0;	
}