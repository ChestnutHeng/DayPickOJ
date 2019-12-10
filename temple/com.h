#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>

#include <string.h>

#define P(x) cout << x << endl;

using namespace std;

struct ListNode {
    int val;
    struct ListNode *next;
ListNode(int x){val = x;next=NULL;}
};

template <typename T>
void print(T *arr, int size){
	for(int i =0; i < size; ++i){
		cout << arr[i] << " ";
	}
	cout << endl;
}

void plinklist(ListNode *l){
	while(l){
		cout << l->val << " ";
		l = l->next;
	}
	cout << endl;
}

template <typename T>
void print(T v){
	cout << v << endl;
}

template <typename T>
vector<T> rd_vec(){
	// read a line
	stringstream ss;
	string str;
	getline(cin, str);
	ss << str;
	// set ans
	vector<T> ans;
	T buf;
	while(ss >> buf){
		ans.push_back(buf);
	}
	return ans;
}

ListNode *rd_list(){
	// read a line
	stringstream ss;
	string str;
	getline(cin, str);
	ss << str;
	// set ans
	ListNode *head = new ListNode(0);
	ListNode *t = head;
	int buf;
	while(ss >> buf){
		t->next = new ListNode(buf);
		t = t->next;
	}
	t->next = NULL;
	return head->next;
}

template <typename T>
T rd_val(){
	// read a line
	stringstream ss;
	string str;
	getline(cin, str);
	ss << str;
	// set ans
	vector<T> ans;
	T buf;
	ss >> buf;
	return buf;
}

template <typename T>
T* rd_arr(int &size){
	// read a line
	stringstream ss;
	string str;
	vector<T> ans = rd_vec<T>();
	size = ans.size();
	T arr[ans.size()];
	for(int i = 0; i < ans.size(); ++i){
		arr[i] = ans[i];
	}
	return arr;
}