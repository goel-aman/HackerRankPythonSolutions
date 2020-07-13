#include <bits/stdc++.h>

using namespace std;

// Complete the formingMagicSquare function below.
int formingMagicSquare(vector<vector<int>> s) {
    int magic[][9] = {
            {8,1,6,3,5,7,4,9,2},
            {6,1,8,7,5,3,2,9,4},
            {4,9,2,3,5,7,8,1,6},
            {2,9,4,7,5,3,6,1,8}, 
            {8,3,4,1,5,9,6,7,2},
            {4,3,8,9,5,1,2,7,6}, 
            {6,7,2,1,5,9,8,3,4}, 
            {2,7,6,9,5,1,4,3,8}};
    int ss[9];
    int k = 0;
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            ss[k] = s[i][j];
            k++;
        }
    }

    int ans = INT_MAX;
    for(int i=0;i<8;i++){
        int difference = 0;
        int* arr = magic[i];
        for(int j=0;j<9;j++){
            difference += abs(arr[j] - ss[j]);
        }
        if(difference < ans){
            ans = difference;
        }
    }
    return ans;


}
int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    vector<vector<int>> s(3);
    for (int i = 0; i < 3; i++) {
        s[i].resize(3);

        for (int j = 0; j < 3; j++) {
            cin >> s[i][j]; 
        }


    }

    int result = formingMagicSquare(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
