// 首先我们对区间，依照右端点，进行排序
// 这里贪心的思想体现在，我们总是在最小的右端点出射出气球，这样可以保证在最小的右端点射中尽量多的气球
// 也就是说，一定存在一种最优（射出的箭数最小）的方法，使得每一支箭的射出位置都恰好对应着某一个气球的右边界。


int findMinArrowShots(vector<vector<int>>& points) {
    auto cmp = [](vector<int>& v1, vector<int>& v2){return v1[1]<v2[1];};
    sort(points.begin(), points.end(), cmp);
    int count = 0;
    long right = LONG_MIN;
    for(auto& p : points)
    {
        if(p[0]>right)
        {
            right = p[1];
            count++;
        }
    }
    return count;
}