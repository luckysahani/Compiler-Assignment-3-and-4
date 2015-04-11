#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <string>
#include <vector>
#include <map>
using namespace std;

vector<string> explode(const string& str, const char& ch) {
    string next;
    vector<string> result;

    // For each character in the string
    for (string::const_iterator it = str.begin(); it != str.end(); it++) {
        // If we've hit the terminal character
        if (*it == ch) {
            // If we have some characters accumulated
            if (!next.empty()) {
                // Add them to the result vector
                result.push_back(next);
                next.clear();
            }
        } else {
            // Accumulate the next character into the sequence
            next += *it;
        }
    }
    if (!next.empty())
         result.push_back(next);
    return result;
}

int main(){
	vector< vector<int> > stack (2000);
	int stack_count[1000];
	int printnum[1000],printnumcnt=0;
	ifstream inp;
	inp.open("output1.txt", ifstream::in);
	cout << "digraph ParseTree{"<< endl;
	map <string, int> mymap;
	int map_count=1;
	string str;
	string rule ="";
	while(getline(inp, str)){
		int i=0,j=0,flag=0;
		printnumcnt=0;
		vector<string> linelm = explode(str,'#');
		std::vector<string> prod = explode(linelm[0],' ');
		map<string, int> :: iterator it = mymap.find(prod[0]);
		//cout << (it!=mymap.end());
		if(it!=mymap.end()==0){
			mymap[prod[0]] = map_count;
			stack_count[map_count] = 1;
			cout << prod[0] << "_1" << " [ label = \""<< prod[0] <<"\" ]";
			printnum[printnumcnt] = 1;
			printnumcnt++;
			map_count++;
		}
		else{
			int temp = it->second;
			int ttemp = stack[temp][stack[temp].size()-1];
			stack[temp].pop_back();
			cout << prod[0] << "_" << ttemp << " [ label = \""<< prod[0] <<"\" ]";
			printnum[printnumcnt] = ttemp;
			printnumcnt++;
		}
		cout << endl;
		it = mymap.find(prod[2]);
		if(it!=mymap.end()==0){
			mymap[prod[2]] = map_count;
			stack_count[map_count] = 1;
			stack[map_count].push_back(1);
			cout << prod[2] << "_1" << " [ label = \""<< prod[2] <<"\" ]";
			printnum[printnumcnt] = 1;
			printnumcnt++;
			map_count++;
		}
		else{
			int temp = it->second;
			stack_count[temp]++;
			stack[temp].push_back(stack_count[temp]);
			cout << prod[2] << "_" << stack_count[temp] << " [ label =\" "<< prod[2] <<"\" ]";
			printnum[printnumcnt] = stack_count[temp];
			// cout << stack_count[temp];
			printnumcnt++;
		}
		cout << endl;
		for(i=3; i< prod.size(); i++){
			it = mymap.find(prod[i]);
			if(it!=mymap.end()==0){
				mymap[prod[i]] = map_count;
				stack_count[map_count] = 1;
				stack[map_count].push_back(1);
				cout << prod[i] << "_1" << " [ label = \""<< prod[i] <<"\" ]";
				printnum[printnumcnt] = 1;
				printnumcnt++;
				map_count++;
			}
			else{
				int temp = it->second;
				stack_count[temp]++;
				stack[temp].push_back(stack_count[temp]);
				cout << prod[i] << "_" << stack_count[temp] << " [ label =\" "<< prod[i] <<"\" ]";
				printnum[printnumcnt] = stack_count[temp];
				printnumcnt++;
			}
			cout << endl;
		}

		cout << prod[0] << "_" << printnum[0] << " " << prod[1] << " " << prod[2] << "_" << printnum[1]<<" ";
		for(i=3; i< prod.size(); i++){
			cout << " , " << prod[i]<<"_"<<printnum[i-1] ;
		}
		cout << endl;
	} 
	cout << "}" << endl;
	return 0;
}