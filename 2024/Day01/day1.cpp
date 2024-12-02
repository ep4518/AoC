#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <math.h>
#include<map>
// g++ day1.cpp -o day1

using namespace std;

int main() {
    ifstream f("input.txt");
    string line, l, r;
    vector<int> left, right;
    while (getline(f, line)) {
        l = line.substr(0,line.find(' '));
        r = line.substr(line.find(' '), line.size());
        left.push_back(stoi(l));
        right.push_back(stoi(r));
    }
    f.close();

    int tot1, tot2 = 0;

    map<int,int> count;

    sort(left.begin(), left.end());
    sort(right.begin(), right.end());

    for (int i = 0; i < left.size(); i++) {
        // Part 1
        tot1 += abs(left[i] - right[i]);

    }

    for (int num: right) {
        count[num]++;
    }
    for (int num: left) {
        tot2 += count[num] * num;
    }

    cout << "Part 1: " << tot1 << endl;
    cout << "Part 2: " << tot2 << endl;

    return 0;
}