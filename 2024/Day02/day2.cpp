#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <string>
#include <cmath>
#include <boost/range/iterator_range.hpp>


using namespace std;
//using namespace boost;

std::vector<std::vector<int>> prn(const std::vector<int>& r);
int fn(const vector<int> &r);


int main() {

    ifstream f("input.txt");
    vector<vector<int> > rows;
    string line;
    while (getline(f, line)) {

        if (line.empty()) continue;

        stringstream ss(line);
        vector<int> row;
        int number;

        while (ss >> number) {
            row.push_back(number);
        }

        rows.push_back(row);

    }

    int cnt = 0;
    for (const auto& r : rows) {
        cnt += fn(r);
    }

    cout << "Part 1: " << cnt << endl;

    cnt = 0;
    prn(rows[0]);
    int s;
    for (const auto& r : rows) {
        s = fn(r);
        cnt += s;
        if (s == 0) {
            for (const auto& nr: prn(r)) {
                if (fn(nr) == 1) {cnt++; break;}
            }
        }
    }
    cout << "Part 2: " << cnt << endl;

}

std::vector<std::vector<int>> prn(const std::vector<int>& r) {
    std::vector<std::vector<int>> combinations;

    for (size_t i = 0; i < r.size(); ++i) {
        auto range1 = boost::make_iterator_range(r.begin(), r.begin() + i);
        auto range2 = boost::make_iterator_range(r.begin() + i + 1, r.end());

        std::vector<int> combination;
        combination.insert(combination.end(), range1.begin(), range1.end());
        combination.insert(combination.end(), range2.begin(), range2.end());
        combinations.push_back(combination);

//        for (const auto& num : combination) {
//            cout << num << " ";
//        }
//        cout << endl;
    }

    return combinations;
}

int fn(const vector<int> &r) {
    bool flag = true;
    int prev, diff, prev_diff = 0;
    for (int i = 0; i < r.size(); i++) {

        diff = r[i] - prev;

        if (i == 0) {prev = r[i]; continue;}

        if ((1 > abs(prev - r[i])) || (3 < abs(prev - r[i])) || (prev_diff * diff < 0)) {flag = false; break;}

        prev = r[i];
        prev_diff = diff;

    }
    if (flag) {
        return 1;
    }

    return 0;
}