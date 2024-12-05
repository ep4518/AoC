#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

vector<string> split(const string& line, const string& delimeter);
vector<int> convertToInt(const vector<string>& stringNumbers);
void reorder_page_list(vector<int>& x, map<int, vector<int> > rules);

// 'in' function: checks if an element exists in a vector
template <typename T>
bool in(const T& element, const std::vector<T>& container) {
    return std::find(container.begin(), container.end(), element) != container.end();
}

// 'any' function: checks if any element in the vector satisfies a condition
template <typename T, typename Func>
bool any(const std::vector<T>& container, Func condition) {
    return std::any_of(container.begin(), container.end(), condition);
}

int main() {
    ifstream f("input.txt");
    if (!f.is_open()) {
        cerr << "Error: Unable to open file." << endl;
        return 1;
    }

    map<int, vector<int> > rules;
    vector<vector<int> > page_lists;
    string line;
    bool flag = true;
    int i;
    vector<string> ptmp;
    while (getline(f, line)) {
        if (line.empty()) {
            flag = false;
            continue;
        }
        if (flag) {
            i = line.find('|');
            rules[stoi(line.substr(0,i))].push_back(stoi(line.substr(i+1,line.size())));
        } else {
            ptmp = split(line,",");  
            page_lists.push_back(convertToInt(ptmp));
        }
        
    }

    int tot1 = 0, tot2 = 0; 

    for (auto& page_list : page_lists) {
        bool flag = true; 
        for (int i = 0; i < page_list.size(); i++) {
            if (any(std::vector<int>(page_list.begin(), page_list.begin() + i), 
                    [&](int p) { return in(p, rules[page_list[i]]); })) {
                flag = false;
                reorder_page_list(page_list, rules);  
                break;
            }
        }

        if (flag) {
            tot1 += page_list[page_list.size() / 2]; 
        } else {
            tot2 += page_list[page_list.size() / 2];  
        }
    }

    // cout << "Rules:" << endl;
    // for (const auto& rule : rules) {
    //     cout << "Key: " << rule.first << " => Values: ";
    //     for (int val : rule.second) {
    //         cout << val << " ";
    //     }
    //     cout << endl;
    // }

    // cout << "Pages:" << endl;
    // for (auto pages: page_lists) {
    //     for (int page: pages) {
    //         cout << page << " ";
    //     }
    //     cout << endl;
    // }

    cout << "Part 1: " << tot1 << endl;
    cout << "Part 2: " << tot2 << endl;
}


vector<string> split(const string& line, const string& delimiter) {
    vector<string> tokens;
    size_t start = 0, end = line.find(delimiter);

    while (end != string::npos) {
        tokens.push_back(line.substr(start, end - start));
        start = end + delimiter.length();
        end = line.find(delimiter, start);
    }

    tokens.push_back(line.substr(start));
    return tokens;
}

vector<int> convertToInt(const vector<string>& stringNumbers) {
    vector<int> intNumbers;
    transform(stringNumbers.begin(), stringNumbers.end(), back_inserter(intNumbers),
              [](const string& str) { return stoi(str); });
    return intNumbers;
}

void reorder_page_list(vector<int>& x, map<int, vector<int> > rules) {
    for (int i = 0; i < x.size(); i++) {
        for (int j = 0; j < i; j++) {
            for (int r = 0; r < rules.at(x[i]).size(); r++) {
                if (x[j] == rules.at(x[i])[r]) {
                    std::swap(x[i], x[j]);
                }
            }
        }
    }
}