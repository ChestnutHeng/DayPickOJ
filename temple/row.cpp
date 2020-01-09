
#include "../temple/com.h"

string function1(string num1, string num2) {
    string sum;
    
    return sum;
}

int main(){
    string a, b;
    cin >> a >> b;
    // 读一个值
    float f = rd_val<float>();
    // 读一个数组
    vector<string> v1 = rd_vec<string>();
    // 读一个c数组
    int final_size;
    int *iarr = rd_arr<int>(&final_size);
    // 读一个链表
    ListNode *head = rd_list();

    // 打印一个值
    P(function1(a, b));
    // 打印一个值
    print(f);
    // 打印一个c数组
    print(iarr, final_size);
    // 打印一个数组
    print(v1);
    // 打印一个链表
    plinklist(head);
    return 0;
}