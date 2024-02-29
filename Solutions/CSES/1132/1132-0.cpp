#include <iostream>
#include <vector>
using namespace std;


const int MAX_N = 2e5 + 5;
int N;
vector<int> G[MAX_N];
vector<int> child(MAX_N, 0);
vector<int> ans(MAX_N, 0);
int build_child(int x, int pre=-1) {
    int result = 0;
    for(int i: G[x]) {
        if(i == pre) continue;
        result = max(build_child(i, x), result);
    }
    return child[x] = result+1;
}
void solve(int x, int pre=-1, int cnt=0) {
    ans[x] = max(child[x]-1, cnt);
    for(int i:G[x]) {
        if(i==pre) continue;
        solve(i, x, cnt+1);
    }
}
int main() {
    cin >> N;
    for(int i=2;i<=N;++i) {
        int a, b;
        cin >> a >> b;
        G[a].push_back(b);
        G[b].push_back(a);
    }
    int end_of_tree = -1;
    for(int i=1;i<=N;++i) {
        if(G[i].size() > 1) continue;
        end_of_tree = i;
        break;
    }
    build_child(end_of_tree);
    solve(end_of_tree);
    for(int i=1;i<=N;++i) cout << ans[i] << ' ';
    cout << '\n';
    return 0;
}