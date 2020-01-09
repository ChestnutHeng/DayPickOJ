// 寻找有序数组中指定的数字
#include "../temple/com.h"


int find_number_index(int *arr, int size, int tar){

}

int main(){
	int size;
	int *arr = rd_arr<int>(&size);
	int tar = rd_val<int>();
	int ind = find_number_index(arr, size, tar);
	cout << ind << endl;
	return 0;	
}