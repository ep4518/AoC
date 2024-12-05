#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <string>

using namespace std;

int main() {
    ifstream f("input.txt");
    if (!f.is_open()) {
        cerr << "Error: Unable to open file." << endl;
        return 1;
    }
    vector< vector < char > > rows;
    vector< char > row;
    string line;
    while (getline(f, line)) {
        row.assign(line.begin(),line.end());
        rows.push_back(row);
    }

    const vector< vector <int> > directions{{-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}};
    int h = rows.size(), w = rows[0].size();

    int tot1 = h, tot2 = w;

    cout << "Part 1: " << tot1 << endl;
    cout << "Part 2: " << tot2 << endl;
}