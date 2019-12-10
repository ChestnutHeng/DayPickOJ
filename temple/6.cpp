// 最大不同子序列（leetcode 3）

#include "com.h"


int lengthOfLongestSubstring(char * s){
    char *p1 = s, *p2 = s;
    int maxlen = 0;
    int nowlen = 0;
    short mp[26];
    memset(mp, 0, sizeof(short)*26);
    while (*p2 != '\0')
    {
        if (mp[*p2 - 'a'] == 0) {
            mp[*p2 - 'a'] = 1;
            nowlen++;
            p2++;
        }else{
            p1 = p2;
            if(nowlen > maxlen){
                maxlen = nowlen;
            }
            nowlen = 0;
            memset(mp, 0, sizeof(short)*26);
        }
        print(mp, 26);
        P(nowlen << *p2)
    }
    return maxlen;
}

int main(){
	string inp;
    cin >> inp;
    int ans = lengthOfLongestSubstring((char *)inp.c_str());
	P(ans)
	return 0;	
}