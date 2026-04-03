// Last updated: 4/4/2026, 12:42:22 AM
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        bool flag=false;
        ListNode *har=head;
        ListNode *tort=head;
        while(har!=NULL && har->next!=NULL){
            har=har->next->next;
            tort=tort->next;
            if (har == tort){
               flag=true;
               break;
            }
        }
        if (flag==true){
            return true;
        }
        else{
            return false;
        }
    }
};