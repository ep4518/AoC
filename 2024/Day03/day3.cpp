#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <string>
#include <regex>
// g++ --std=c++20 day3.cpp -o day3

using namespace std;

int main() {
    ifstream f("input.txt");
    if (!f.is_open()) {
        cerr << "Error: Unable to open file." << endl;
        return 1;
    }
    vector< string > rows;
    string line;
    while (getline(f, line)) {
        rows.push_back(line);
    }

    std::regex mul_pattern(R"(mul\((\d+),\s*(-?\d+)\)|do\(\)|don't\(\))");

    bool flag = true;

    int tot1 = 0, tot2 = 0;

    for (auto line: rows) {

        std::sregex_iterator it(line.begin(), line.end(), mul_pattern);
        std::sregex_iterator end;

        while(it != end) {
            std::smatch match = *it;

            if (match[0].compare("do()") == 0) flag = true;
            else if (match[0].compare("don't()") == 0) flag = false;
            else {
                tot1 += stoi(match[1]) * stoi(match[2]);
                tot2 += flag * stoi(match[1]) * stoi(match[2]);
            }

            it++;
        }
    }
    cout << "Part 1: " << tot1 << endl;
    cout << "Part 2: " << tot2 << endl;
}