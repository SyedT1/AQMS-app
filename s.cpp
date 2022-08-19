#include <bits/stdc++.h>
using namespace std;
using ll = long long int;
void setup()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
}
void solve()
{
    ll a, b, c, d;
    cin >> a >> b >> c >> d;
    cout << (b > a) + (c > a) + (d > a) << endl;
}
int main()
{
    ll q;
    cin >> q;
    while (q--)
    {
        solve();
    }
}
