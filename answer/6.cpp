// 最大不同子序列（leetcode 3）

#include "temple/com.h"
#include <map>

int lengthOfLongestSubstring(string s) {
    map<int, int> lastp;
    int p1 = 0, maxl = 0;
    int p2 = 0;
    while(s[p2] != '\0'){
        if(lastp.find(s[p2]) != lastp.end()){
            if (maxl < p2 - p1){
                maxl = p2 - p1;
            }
            p1 = lastp[s[p2]] + 1;
            p2 = p1;
            lastp.clear();
        }
        //cout << p1 << p2 << maxl << endl;
        lastp[s[p2]] = p2;
        p2++;
    }
    if (maxl < p2 - p1){
        maxl = p2 - p1;
    }
    return maxl;
}

int main(){
	string inp;
    cin >> inp;
    int ans = lengthOfLongestSubstring((char *)inp.c_str());
	P(ans)
	return 0;	
}