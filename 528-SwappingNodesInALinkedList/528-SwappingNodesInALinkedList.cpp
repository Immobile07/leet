// Last updated: 4/4/2026, 12:41:39 AM
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

int size_(ListNode *head){
    ListNode* temp=head;
    int cnt=0;
    while (temp!=NULL){
        cnt++;
        temp=temp->next;
    }
    return cnt;
}

    void swap_nd(ListNode *&head, int value){
        ListNode *shamner=head;
        ListNode *picher=head;
        int y=value-1;
        for (int i=1;i<=y;i++){
            shamner=shamner->next;
        }
        int x=size_(head)-value;
        for (int i=1;i<=x;i++){
            picher=picher->next;
        }
        if (shamner->next!=picher->next){
           int z=shamner->val;
            shamner->val=picher->val;
            picher->val=z;
                    }
    }



    ListNode* swapNodes(ListNode* head, int k) {
            
            swap_nd(head,k);
            return head;            
            
            
            
            }
};