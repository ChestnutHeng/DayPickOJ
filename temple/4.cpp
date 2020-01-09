// 寻找第k个小的数字
// 寻找中位数、partition
// 寻找数字是第几小

#include "../temple/com.h"


int find_kth_little(int *arr, int size, int k){
    
}

int main(){
	int size;
	int *arr = rd_arr<int>(&size);
	int k = rd_val<int>();
	int ind = find_kth_little(arr,size,k);
	cout << ind << endl;
	return 0;	
}