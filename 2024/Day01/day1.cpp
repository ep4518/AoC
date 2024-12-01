#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <math.h>
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

    int tot1, tot2, cnt = 0;

    for (int i = 0; i < left.size(); i++) {
        //  Part 2
        cnt = 0;

        for (int j = 0; j < right.size(); j++) {

            if (left[i] == right[j]) cnt ++;

        }

        tot2 += cnt * left[i];

    }

    sort(left.begin(), left.end());
    sort(right.begin(), right.end());

    for (int i = 0; i < left.size(); i++) {
        // Part 1
        tot1 += abs(left[i] - right[i]);

    }

    cout << "Part 1: " << tot1 << endl;
    cout << "Part 2: " << tot2 << endl;

    return 0;
}