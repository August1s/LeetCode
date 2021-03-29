
// 首先按照身高进行排序
// 优先插入身高最高的，因为插入身高低的元素不会影响高身高元素的正确顺序

vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
    auto cmp = [](vector<int>& v1, vector<int>& v2){ return (v1[0]==v2[0])? v1[1]<v2[1] : v1[0]>v2[0]; };
    sort(people.begin(), people.end(), cmp);
    
    vector<vector<int>> res;
    for(auto p : people)
    {
        res.insert(res.begin() + p[1], p);
    }
    return res;
}