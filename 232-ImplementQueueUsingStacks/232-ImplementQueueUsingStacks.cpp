// Last updated: 4/4/2026, 12:41:58 AM
class MyQueue {
public:
    stack<int>ek;
    MyQueue() {
        
    }
    
    void push(int x) {
        ek.push(x);
    }
    
    int pop() {
        stack<int>dui;
        int z;
        while(ek.empty()!= true){
            z=ek.top();
            ek.pop();
            if(ek.empty()==true){
                
                
                break;
            }
            else{
                dui.push(z);
            }
        }
        while(!dui.empty()){
            ek.push(dui.top());
            dui.pop();
        }
        return z;
    }

    
    int peek() {
        stack<int>dui;
        int z;
        while(!ek.empty()){
             z=ek.top();
            ek.pop();
            if(ek.empty()==true){
                dui.push(z);
                
                break;
            }
            else{
                dui.push(z);
            }
        }
         while(!dui.empty()){
            ek.push(dui.top());
            dui.pop();
        }
        return z;
    }
    
    bool empty() {
        return ek.empty();
    }
};


/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */