#include <iostream>
#include <vector>

using namespace std;

//input the puzzle numbers
int inputNumbers(vector<int> &puzzle);
//print the puzzle
void printPuzzle(const vector<int> &puzzle, int n);
//solve the puzzle
bool puzzleSolve(vector<int> &,int,int);
//check puzzle to right side to solve it
bool puzzlePermutation1(vector<int> &puzzle, int elements, int selectedElement);
//check puzzle left side to solve it
bool puzzlePermutation2(vector<int> &puzzle, int elements, int selectedElement);

int main(){
   //input the puzzle elements
    vector<int> puzzle;
    int elements= inputNumbers(puzzle);
    if(puzzleSolve(puzzle, elements, 0)){
        cout<<"Puzzle solved!"<<endl;
    }
    else{
        cout<<"Puzzle can not be solved!"<<endl;
    }
    return 0;
}

//function to input the elements for the puzzle
int inputNumbers(vector<int> &puzzle){

    //puzzle elements
    int puzzleElements;
    int count=0;

    //Ask user to input elements to puzzle
    cout<<"Please enter the positive elements for the puzzle (Enter 0 to finish the puzzle elements) ): "<<endl;
    cin >> puzzleElements;

    //Check if the number is positive or not
    while(puzzleElements < 0){
        cout<<"Wrong number! Please input again: "<<endl;
        cin >> puzzleElements;
    }

    //add all elements to the puzzle
    while(puzzleElements != 0){
        puzzle.push_back(puzzleElements);
        count++;
        cin >> puzzleElements;
        while(puzzleElements < 0){
            cout<<"Please enter correct elements: "<<endl;
            cin >> puzzleElements;
        }
    }
    puzzle.push_back(0);
    count++;

    //Select the first number to start jumping
    int fir;
    cout<<"Please select elements to start solve puzzle (from 1 to "<<count<<" ):"<<endl;
    cin>>fir;


    //add all elements to the puzzle
    while(fir<=0||fir>count){
        cout<<"Please enter correct elements: "<<endl;
        cin>>fir;
    }

    puzzle.insert(puzzle.begin(),fir);
    count++;
    printPuzzle(puzzle, count);
    return count;
}

//function to print the puzzle elements
void printPuzzle(const vector<int> &puzzle, int n){
    cout<<"Your puzzle is: "<<endl;
    for(int i=0;i<n;i++){
        cout<<puzzle[i]<<" ";
    }
    cout<<endl;
}

//function to solve the puzzle
bool puzzleSolve(vector<int> &puzzle, int elements, int m){
    vector<int> temp;

    if(m == elements - 1){
        return true;
    }

    else{
        if(puzzlePermutation1(puzzle, elements, m)){
            int o=m+puzzle[m];
            temp=puzzle;
            puzzle[m]=-1;
            if(puzzleSolve(puzzle, elements, o)){
                return true;
            }
        }
        puzzle=temp;

        if(puzzlePermutation2(puzzle, elements, m)){
            int o=m-puzzle[m];
            temp=puzzle;
            puzzle[m]=-1;
            if(puzzleSolve(puzzle, elements, o)){
                return true;
            }
        }
        puzzle=temp;

        return false;
    }
}

bool puzzlePermutation1(vector<int> &puzzle, int elements, int selectedElement){
    selectedElement+=puzzle[selectedElement];
    if(puzzle[selectedElement] == -1){
        return false;
    }
    if(selectedElement <= 0 || selectedElement >= elements){
        return false;
    }
    return true;
}

bool puzzlePermutation2(vector<int> &puzzle, int elements, int selectedElement){
    selectedElement-=puzzle[selectedElement];
    if(puzzle[selectedElement] == -1){
        return false;
    }
    if(selectedElement <= 0 || selectedElement >= elements){
        return false;
    }
    return true;
}

