// Last updated: 4/4/2026, 12:42:06 AM
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
public:int size_(ListNode*&head){
    int count=0;
    ListNode *temp=head;
    while(temp!=NULL){
        count+=1;
        temp=temp->next;

    }
    return count;
}

int how_mch(ListNode*head,int val){
    ListNode * temp=head;
    int cnt=0;
    while(temp!=NULL){
        if (temp->val==val){
            cnt+=1;
            temp=temp->next;
        }
        else{
            temp=temp->next;
        }
    }
    return cnt; 
}

void rmv(ListNode*&head, int val){
    ListNode *temp=head;
        while(temp!=NULL && temp->next!=NULL){
            if (head->val==val){
                ListNode *z=head;
                head=head->next;
                delete z;
                temp=head;
            }
        else if(temp->next->val==val){
            ListNode *dlt=temp->next;
            temp->next=temp->next->next;
        }
        else{
            temp=temp->next;
        }
        }
}
void clear_all(ListNode *&head){
    head=NULL;
}
    ListNode* removeElements(ListNode*&head, int val) {
        if (how_mch(head,val)==size_(head)){
            clear_all(head);
            return head;
        }
        rmv(head,val);
        return head;
    }
};