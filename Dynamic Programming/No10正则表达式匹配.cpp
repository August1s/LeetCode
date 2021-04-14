
// 状态转移方程：
// 当p[j] == * 的时候, F(i, j) = F(i-1, j-1) && (s[i] == p[j] || p[j] == '.')
// 当p[j] != * 的时候：1. F(i, j) = F(i, j-2)，表示舍弃*号组成的部分
//                    2. F(i, j) = F(i-1, j) && (s[i] == p[j - 1] || p[j - 1] == '.')，判断是否和*号前的那个字符匹配

bool isMatch(string s, string p) 
{
    s = ' ' + s;
    p = ' ' + p;
    vector<vector<bool>> dp(s.size(), vector<bool>(p.size(), false));
    dp[0][0] = true;
    for (int i = 0; i < s.size(); i++)
    {
        for (int j = 0; j < p.size(); j++)
        {
            if (!i && !j)  continue;
            if (j + 1 <= p.size() && p[j + 1] == '*') continue;
            if (p[j] != '*')
            {
                if (s[i] == p[j] || p[j] == '.')
                    if (i > 0 && j > 0)
                        dp[i][j] = dp[i - 1][j - 1];
            }
            else
            {
                if (i > 0)
                    dp[i][j] = dp[i][j - 2] || ((s[i] == p[j - 1] || p[j - 1] == '.') && dp[i - 1][j]);
                else
                    dp[i][j] = dp[i][j - 2];
            }
        }
    }
    return dp[s.size() - 1][p.size() - 1];
}