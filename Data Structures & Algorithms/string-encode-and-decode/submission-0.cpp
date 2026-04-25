class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded;

        for (string bob : strs){
            encoded += to_string(bob.length());
            encoded += '#';
            encoded += bob;
        }

        return encoded;
    }

    vector<string> decode(string s) {
        vector<string> decoded;
        int n = s.length();
        int i = 0;


        while(i!=n){
            int j = i;
            while (s[j]!='#'){
                j++;
                //find the # for encoding
            }

            int length = std::stoi(s.substr(i, j-i));
            string word = s.substr(j+1, length);
            //j+1 bc j is index of #
            decoded.push_back(word);
            i =j+1+length;
        }

        return decoded;
    }
};
