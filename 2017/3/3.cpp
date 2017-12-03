#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stdlib.h>
#include <map>

using namespace std;

int solve(int target) {
  if (target == 1) {
    return 0;
  }
  int x = 1;
  int y = 0;
  int delta = 3;
  
  for (int n = 2; n < target; ) {
    for (int i = 0; i < delta - 2 && n < target; i++, n++)
      y++;
    for (int i = 0; i < delta - 1 && n < target; i++, n++)
      x--;
    for (int i = 0; i < delta - 1 && n < target; i++, n++)
      y--;
    for (int i = 0; i < delta && n < target; i++, n++)
      x++;
    delta += 2;
  }
    
  return abs(x) + abs(y);
}

map< pair<int, int>, int > square;

int computeSquare(int x, int y) {
  int sum = 0;
  for (int i = -1; i < 2; i++) {
    for (int j = -1; j < 2; j++) {
      if (i == 0 && j == 0) {
        continue;
      }
      pair<int, int> p(x + i, y + j);
      sum += square[p];
    }
  }
  pair<int, int> p(x, y);
  square[p] = sum;
  return sum;
}

int solveB(int target) {
  square.clear();
  if (target == 1) {
    return 0;
  }
  pair<int, int> p(0, 0);
  square[p] = 1;
  int x = 1;
  int y = 0;
  int delta = 3;
  
  for (; computeSquare(x, y) <= target; ) {
    for (int i = 0; i < delta - 2 && computeSquare(x, y) <= target; i++)
      y++;
    for (int i = 0; i < delta - 1 && computeSquare(x, y) <= target; i++)
      x--;
    for (int i = 0; i < delta - 1 && computeSquare(x, y) <= target; i++)
      y--;
    for (int i = 0; i < delta && computeSquare(x, y) <= target; i++)
      x++;
    delta += 2;
  }
    
  return computeSquare(x, y);
}

int main() {
  cout << solve(1)    << ' ' << 0 << endl;
  cout << solve(12)   << ' ' << 3 << endl;
  cout << solve(23)   << ' ' << 2 << endl;
  cout << solve(1024) << ' ' << 31 << endl << endl;
  cout << "A " << solve(312051) << endl;

  cout << "B " << solveB(312051) << endl;
}
