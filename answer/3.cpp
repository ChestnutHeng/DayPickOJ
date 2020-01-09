#include "../temple/com.h"


int find_number_index(int *arr, int size, int tar){
	int hi = size - 1, lo = 0;
	int mid;
	while (lo <= hi)
	{
		mid = (hi + lo)/2;
		if(arr[mid] < tar){
			lo = mid + 1;
		}else if(arr[mid] > tar){
			hi = mid - 1;
		}else{
			return mid;
		}
	}
	return -1;
}

int main(){
	int size;
	int *arr = rd_arr<int>(&size);
	int tar = rd_val<int>();
	int ind = find_number_index(arr, size, tar);
	cout << ind << endl;
	return 0;	
}