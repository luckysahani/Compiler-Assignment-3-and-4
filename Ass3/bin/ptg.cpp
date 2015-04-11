#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <fstream>
using namespace std;

int main(){
	// FILE * plog;
	// plog = fopen("parselog.txt","r");
	ifstream plog;
	plog.open("parselog.txt", ifstream::in);
	ofstream outp;
	outp.open("output.txt", ofstream::out);
	int linecount = 0;
	string str;
	while(getline (plog, str)){
		int i=0;
		for(i=11; str[i]!=':' ;i++){
		}
		if(str[i+1]=='A'){
			i++;
			for(; str[i]!=':' ;i++){
			}
			if(str[i+2]=='R'){
				linecount++;
				while(str[i]!='[') i++;
				i++;
				while(str[i]!=']') {
					outp << str[i];
					i++;
				}
				outp << " # ";
				while(str[i]!='[') i++;
				i++;
				while(1) {
					if(str[i]==']' && str[i+1]== ' ' && str[i+2] == 'a' && str[i+3] == 'n' && str.length() < i+21){
						// outp<<" "<<i << " " << str.length()<< " ";
						break;
					}
					outp << str[i];
					i++;
				}
				outp << endl;
			}
		}
	}
}
