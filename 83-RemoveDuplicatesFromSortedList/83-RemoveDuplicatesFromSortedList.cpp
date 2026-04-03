// Last updated: 4/4/2026, 12:42:37 AM
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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* tmp=head;
        while (tmp!=NULL){
            if(tmp->next==NULL){
                break;
            }
            else if (tmp->val == tmp->next->val){
                ListNode *delet=tmp->next;
                tmp->next=tmp->next->next;
                delete delet;
            }
            else{
                tmp=tmp->next;
            }
        }
         return head;
    }
   
};