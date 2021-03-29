// 首先对两个数组排序
// 根据贪心算法，我们尽量使用最小的饼干满足各种胃口孩子

int findContentChildren(vector<int>& g, vector<int>& s) {
    sort(g.begin(), g.end());
    sort(s.begin(), s.end());
    int i = 0,j = 0;
    int count = 0;
    while(i<g.size() && j<s.size())
    {
        if(g[i]<=s[j])
            count++,i++,j++;
        else
            j++;
    }
    return count;
}