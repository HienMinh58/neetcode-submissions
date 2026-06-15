class KthLargest {
public:
    int K;
    priority_queue<int, vector<int>, greater<int>> minHeap;
    KthLargest(int k, vector<int>& nums) {
        K = k;
        for(int num : nums){
            add(num);
        }
    }
    
    int add(int val) {
        minHeap.push(val);
        if(minHeap.size() > K){
            minHeap.pop();
        }
        return minHeap.top();
    }
};
