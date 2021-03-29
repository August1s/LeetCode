// 贪心算法，我们首先根据nums[i]找到当前可跳跃的范围
// 然后我们再这个范围中，选择跳的最远的方案作为跳跃次数最小的方案

int jump(vector<int>& nums) {
    int i = 0, count = 0;
    while(i<nums.size()-1)
    {
        if(i+nums[i]>=nums.size()-1)
        {
            count++;
            break;
        }
        int maxstep = i, maxdis = i;
        for(int j=i+1;j<=nums[i]+i && j<nums.size();j++)
        {
            if(j + nums[j] > maxdis)
            {
                maxstep = j;
                maxdis = j+nums[j];
            }
        }
        i = maxstep;
        count++;
    }
    return count;
}

// 这题还可以使用动态规划
// F(i) = min( F(k) ) + 1  如果F(k)可以跳到F(i) 
int jump(vector<int>& nums) {
    vector<int> dp(nums.size(), 99999999);
    dp[0] = 0;
    for(int i=1;i<dp.size();i++)
    {
        for(int j=i-1;j>=0;j--)
        {
            if(j+nums[j]>=i)
                dp[i] = min(dp[i], dp[j]+1);
        }
    }
    return dp[dp.size()-1];
}