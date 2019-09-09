#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;

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