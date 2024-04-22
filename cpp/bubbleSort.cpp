#include <bits/stdc++.h>
#include <chrono>
using namespace std;
using namespace chrono;

// A function to implement insertion sort
void insertionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;

        // Move elements of arr[0..i-1], that are greater than key,
        // to one position ahead of their current position
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

// Function to print an array to a file
void printArrayToFile(const vector<int>& arr, const string& filename) {
    ofstream outFile(filename);
    for (int num : arr) {
        outFile << num << endl;
    }
    outFile.close();
}

// Function to read an array from a file
vector<int> readArrayFromFile(const string& filename) {
    ifstream inFile(filename);
    vector<int> arr;
    int temp;
    while (inFile >> temp) {
        arr.push_back(temp);
    }
    inFile.close();
    return arr;
}

// Driver code
int main() {
    string inputFilename = "unsorted_numbers.txt";
    string outputFilename = "sorted_numbers.txt";

    auto start = high_resolution_clock::now();

    vector<int> arr = readArrayFromFile(inputFilename);
    insertionSort(arr);
    printArrayToFile(arr, outputFilename);

    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop - start);

    cout << "Total time taken: " << duration.count() << " milliseconds\n";
    return 0;
}
