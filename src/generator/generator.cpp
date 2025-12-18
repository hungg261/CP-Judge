#include <bits/stdc++.h>
#define int long long
using namespace std;

#include "../RandLib/randlib.h"
using namespace RandLib;

void generate(){
    NumberGen NumGen;
    int n = NumGen.Rand<int>(1, 1e9);

    cout << n << '\n';
}

signed main(){
    ios_base::sync_with_stdio(0); cin.tie(0);

    generate();

    return 0;
}