#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main() {
  vector< vector<int> > data;
  for (string line; getline(cin, line); ) {
    istringstream iss(line);
    vector<int> row;
    int x;
    while (iss >> x) {
      row.push_back(x);
    }
    data.push_back(row);
  }

  int checksum = 0;
  for (auto row : data) {
    int min = 10000;
    int max = -10000;
    for (auto x : row) {
      if (x < min) {
        min = x;
      }
      if (x > max) {
        max = x;
      }
    }
    checksum += max - min;
  }

  cout << "A " << checksum << endl;

  checksum = 0;
  for (auto row : data) {
    int count = 0;
    for (auto i = 0; i < row.size(); i++) {
      for (auto j = 0; j < row.size(); j++) {
        if (i == j || row[i] > row[j]) {
          continue;
        }
        if (row[j] % row[i] == 0) {
          count++;
          checksum += (row[j] / row[i]);
        }
      }
    }
    assert(count == 1);
  }
  cout << "B " << checksum << endl;
}
