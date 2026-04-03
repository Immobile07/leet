// Last updated: 4/4/2026, 12:41:29 AM
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int size_(ListNode*head){
    int count=0;
    ListNode *temp=head;
    while(temp!=NULL){
        count++;
        temp=temp->next;
    }
    return count;
}
    ListNode* middleNode(ListNode* head) {
        ListNode* tmp=head;
        int sz=int(size_(head));
        for (int i=1;i<=sz/2;i++){
            tmp=tmp->next;
        }
        return tmp;
        
    }
};