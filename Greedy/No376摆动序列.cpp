// 将数列想象为一个折线，可以看出我们要找的就是折线中的转折点
// 同时我们需要一个while，处理一下相同的元素

int wiggleMaxLength(vector<int>& nums){
    int count = 1;
    int i = 0;
    while (i < nums.size() - 1)
    {
        int pre = i>0? nums[i - 1] : nums[i], j = i + 1;
        while (nums[j] == nums[i] && j < nums.size() - 1) j++;
        if (j == nums.size() - 1)
        {
            if ((nums[i]>pre && nums[i]>nums[j]) || nums[i]<pre && nums[i]<nums[j])
            {
                count += 2;
                break;
            }
            else if(pre!=nums[i])
            {
                count++;
                break;
            }
            else
                break;
        }
        if ((nums[i] > pre && nums[i] > nums[j]) || (nums[i] < pre && nums[i] < nums[j]))
        {
            count++; i=j;
        }
        else
            i=j;
    }
    return count;
}
