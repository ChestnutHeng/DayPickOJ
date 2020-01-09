// 链表相加模板（leetcode 1）

#include "../temple/com.h"


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
       struct ListNode* l3 = (ListNode*)malloc(sizeof(struct ListNode));
	l3->val = 0;
	struct ListNode *tra = l3;
	int c = 0;
	while(c || l1 || l2){
	    c += (l1 ? l1->val : 0) + (l2 ? l2->val : 0);
	    tra->next = (ListNode*)malloc(sizeof(struct ListNode));
	    tra->next->val = c%10;
	    tra = tra->next;
	    c /= 10;
	    if(l1) l1 = l1->next;
	    if(l2) l2 = l2->next;
	}
	tra->next = NULL;
	return l3->next;
}

int main(){
	ListNode* l1 = rd_list();
	ListNode* l2 = rd_list();
	ListNode* l3 = addTwoNumbers(l1, l2);
	plinklist(l3);
	return 0;	
}