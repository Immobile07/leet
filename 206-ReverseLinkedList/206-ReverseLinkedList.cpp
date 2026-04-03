// Last updated: 4/4/2026, 12:42:05 AM
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
        void reversible(ListNode *&head, ListNode*porer){
            if (porer->next==NULL){
                head=porer;
                return;
            }
            else{
                reversible(head,porer->next);
                porer->next->next=porer;
                porer->next=NULL;
            }
        }







    ListNode* reverseList(ListNode* head) {
        if (head==NULL){
            return head;
        }
        else{
            reversible(head,head);
            return head;
        }
    }
};