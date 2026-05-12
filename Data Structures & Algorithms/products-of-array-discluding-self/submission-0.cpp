class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int siz = nums.size();
        vector<int> asc(siz);
        vector<int> desc(siz);

        for (int i =0; i<siz; i++){
            if (i==0){
                asc[0]=nums[0];
                desc[siz-1]=nums[siz-1];
                continue;
            }
            asc[i]=nums[i]*asc[i-1];
            desc[siz-1-i]=nums[siz-1-i]*desc[siz-i];
        }

        vector<int> ans(siz);

        for (int i=0; i<siz; i++){
            if (i==0){
                ans[i]= desc[i+1];
                continue;
            }
            if (i==(siz-1)){
                ans[i]=asc[siz-2];
                continue;
            }
            ans[i] = asc[i-1]*desc[i+1];

        }
        return ans;
        //return desc;

    }
};
