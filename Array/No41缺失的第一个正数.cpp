// 1.排序后直接找数组中的元素
// 2.哈希表记录每个元素是否在数组中
// 3.首先进行交换，将每个元素交换到正确的位置上（有点类似于哈希表的记录方法），
//   然后再遍历找到不在正确的位置上的元素。时间为O(n)，空间为O(1)


int firstMissingPositive(vector<int>& nums) {
    for (int i = 0; i < nums.size(); i++)
    {
        int temp = i;
        while (nums[temp] > 0 && nums[temp] <= nums.size() && nums[temp] != i + 1 && nums[temp]!= nums[nums[temp] - 1])
        {
            swap(nums[temp], nums[nums[temp] - 1]);
        }
    }
    for(int i=0;i<nums.size();i++)
    {
        if(nums[i]!=i+1)
            return i+1;
    }
    return nums.size()+1;
}