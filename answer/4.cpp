#include "../temple/com.h"

// 1 5 8 2 4 | 3
// patition下标赋值正确
// 找的是第k小的数字
// 只有一个数字时两个返回值都要操作
// 最终返回的是找到的数字

int partition(int *arr, int lo, int hi, int *kth){
	if (lo == hi){*kth = 0;return arr[lo];}
	int pivot = arr[hi];
	int store = lo;
	for(int i = lo; i <= hi - 1; i++){
		if(arr[i] < pivot){
			swap(arr[i], arr[store]);
			store++;
		}
	}
	swap(arr[hi], arr[store]);
	*kth = store;
	return pivot;
}

int find_kth_little(int *arr, int size, int k){
	int kth;
	int pivot;
	int lo = 0, hi = size - 1;
	while(lo <= hi){
		pivot = partition(arr, lo, hi, &kth);
		if(kth > k - 1){
			hi = kth - 1;
		}else if(kth < k - 1){
			lo = kth + 1;
		}else{
			return pivot;
		}
		//print(lo, hi, kth);
	}
	return -1;
}

int main(){
	int size;
	int *arr = rd_arr<int>(&size);
	int k = rd_val<int>();
	int ind = find_kth_little(arr,size,k);
	cout << ind << endl;
	return 0;	
}