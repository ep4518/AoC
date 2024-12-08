#include <iostream>
#include <set>
#include <vector>
#include <fstream>
#include <string>


using namespace std;

int fn(const vector<vector<char> > &G, const vector<int> &start);

int main() {

	ifstream f("input.txt");
	if (!f.is_open()) {
		cerr << "Error: Unable to open file." << endl;
		return 1;
	}
	vector<vector<char> > G;
	string line;

	while (getline(f, line)) {
		vector<char> v(line.begin(), line.end());
		G.push_back(v);
	}
	
	vector<int> start;
	for (int i = 0; i < G.size(); i++) {
		for (int j = 0; j < G[0].size(); j++) {
			if (G[i][j] == '^') start={i, j};
		}
	}

  cout << "Part 1: " << fn(G, start) << endl;

  int count = 0;
	for (int i = 0; i < G.size(); i++) {
		for (int j = 0; j < G[0].size(); j++) {
      if (G[i][j] == '#') continue;
      auto mG = G;
      
     mG[i][j] = '#';
      if (fn(mG, start) == -1) {count++;}
    }
  }

  cout << "Part 2: " << count << endl;

}

int fn(const vector<vector<char> > &G, const vector<int> &start) {
	int i = start[0], j = start[1];
	set<vector<int> > SEENWDIR;
	set<vector<int> > SEEN;
	int d = 0;
	int di, dj;
	vector<vector< int > > directions={{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
	while ((0 <= i) && (i < G.size()) && (0 <= j) && (j < G[0].size())) {
    if (SEENWDIR.count({i, j, d})) {return -1;}
		SEEN.insert({i, j});  
		SEENWDIR.insert({i, j, d});

		di = directions[d][0];
		dj = directions[d][1];
		if ((0 <= i + di) && (i + di < G.size()) && (0 <= j + dj) && (j + dj < G[0].size())) {
			if (G[i+di][j+dj] == '#') {
				d++;
				d%=4;
				di = directions[d][0];
				dj = directions[d][1];
			}
		}
		i = i + di;
		j = j + dj;
	}	
  return SEEN.size();
}
