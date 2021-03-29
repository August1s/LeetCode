// 面值为5，10，20，价格为5，显然20块钱是没有用的
// 对于20块找零15的情况，我们尽量先找零10块，再找零5块，这里使用贪心

bool lemonadeChange(vector<int>& bills) {
        int five = 0, ten = 0;
        for(auto b : bills)
        {
            if(b==5)
                five++;
            else if(b==10)
            {
                ten++;
                if(five>0)  
                    five--;
                else    
                    return false;
            }
            else
            {
                int temp = 15;
                if(ten>0)
                {
                    ten--;
                    temp -= 10;
                }
                while(temp>0 && five>0)
                {
                    five--;
                    temp -= 5;
                }
                if(temp>0)
                    return false;
            }
        }
        return true;
    }