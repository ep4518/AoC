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

    const vector<vector<int> > directions = {{-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}};
    const vector<vector<int> > directions2 = {{-1, 1}, {1, 1}, {1, -1}, {-1, -1}};
    int h = rows.size(), w = (h > 0) ? rows[0].size() : 0; 
    const vector< char > chars1 = {'M', 'A', 'S'};
    const vector<vector< char > > matches2 =  {{'M', 'M', 'S', 'S'}, {'S', 'M', 'M', 'S'}, {'S', 'S', 'M', 'M'}, {'M', 'S', 'S', 'M'}};

    int tot1 = 0, tot2 = 0;
    int di, dj, ii, jj;
    bool flag;
    vector < char > tmp = {};
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            if (rows[i][j] == 'X') {
                for (int k = 0; k < directions.size(); k++) {
                    di = directions[k][0],
                    dj = directions[k][1];
                    flag = true;
                    ii = i + di;
                    jj = j + dj;
                    for (int l = 0; l < chars1.size(); l++) {
                        if ((0 <= ii) && (ii < h) && (0 <= jj) && (jj <= w) && rows[ii][jj] == chars1[l]) {
                            ii += di;
                            jj += dj;
                            continue;
                        } else {
                            flag = false;
                            break;
                        }
                    }
                    if (flag) tot1++;
                }
            }
            if (rows[i][j] == 'A') {
                tmp = {};
                for (int k = 0; k < directions2.size(); k++) {
                    di = directions2[k][1];
                    dj = directions2[k][0];
                    ii = i + di;
                    jj = j + dj;
                    if ((0 <= ii) && (ii < h) && (0 <= jj) && (jj < w)) {
                        tmp.push_back(rows[ii][jj]);
                    }
                }
                for (int k = 0; k < matches2.size(); k++) {
                    if (matches2[k] == tmp) {
                        tot2++;
                    }
                }
            }
        }
    }

    cout << "Part 1: " << tot1 << endl;
    cout << "Part 2: " << tot2 << endl;
}