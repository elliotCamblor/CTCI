#include <iostream>
#include <stack>

char* reverse(char *str) {
    std::stack<char> charStackTemp;

    for(; *str != '\0'; str++) {
        charStackTemp.push(*str);
    }

    char *returnStr = new char[charStackTemp.size()];
    int i = 0;
    while(!charStackTemp.empty()){
        returnStr[i++] = charStackTemp.top();
        charStackTemp.pop();
    }
    return returnStr;
}

int main(int argc, char* argv[]) {
    for(int i = 1; i < argc; i++){
        std::cout<<reverse(argv[i]) <<std::endl;
    }
}
