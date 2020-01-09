
#include "../temple/com.h"

void search(vector<vector<int>> &ans, vector<int> stack, vector<int> left){
    if(stack.empty()){
        ans.push_back(left);
        return;
    }
    for(int i =0; i < stack.size(); ++i){
        vector<int> tstack = stack;
        vector<int> tleft = left;
        tleft.push_back(stack[i]);
        tstack.erase(tstack.begin() + i);
        search(ans, tstack, tleft);
    }
}

vector<vector<int>> permute(vector<int>& nums) {
    vector<vector<int>> ans;
    vector<int> left;
    search(ans, nums, left);
    return ans;
}

int main(){
    vector<int> v1 = rd_vec<int>();
    vector<vector<int>> ans = permute(v1);
    print(ans);
    return 0;
}