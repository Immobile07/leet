// Last updated: 4/4/2026, 12:42:55 AM
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
        ListNode *temp=head;
        int cnt=0;
        while (temp!=NULL){
            cnt++;
            temp=temp->next;
        }
        return cnt;
    }
    void rmv_nth(ListNode *&head,int n){
        ListNode *temp=head;
        if (n==size_(head)){
            if (head->next==NULL){
                head=NULL;
            
            }
            else{
                ListNode *dlt=head;
                head=head->next;
                delete dlt;
            }
        }
        else if(n==1){
            for (int i=1;i<=(size_(head))-n-1;i++){
            temp=temp->next;
        }
         ListNode *dlt=temp->next;
                temp->next=NULL;
                delete dlt;
        }
        else{
        for (int i=1;i<=(size_(head))-n-1;i++){
            temp=temp->next;
        }
        ListNode *dlt=temp->next;
                temp->next=temp->next->next;
                delete dlt;
        }
    }

    
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        rmv_nth(head,n);
        return head;
    }
};