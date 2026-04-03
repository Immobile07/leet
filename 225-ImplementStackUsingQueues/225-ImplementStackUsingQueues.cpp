// Last updated: 4/4/2026, 12:41:59 AM
class MyStack {
public:
    queue <int> ek;
    MyStack() {
        
    }
    
    void push(int x) {
        ek.push(x);
    }
    
    int pop() {
        queue <int> dui;
        int z;
        while (ek.empty()!=true){
            z=ek.front();
            ek.pop();
            if (ek.empty()==true){
                
                break;
            }
            else{
                dui.push(z);
            }
        }
        ek=dui;
        return z;
    }
    
    int top() 
    {   int z;
        queue <int> dui;
        while(ek.empty()!=true){
            z=ek.front();
            ek.pop();
            if (ek.empty()==true){
                dui.push(z);
                ;
                break;
            }
            else{
                dui.push(z);
            }
        }
        ek=dui;
        return z;
    }
    
    bool empty() {
        return ek.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */