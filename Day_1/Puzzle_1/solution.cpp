#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

int find_nums(int* buffer, int size);


int main(int argc, char* argv[])
{
    /////////////////////////////////////////////////////////////////////////////////////////
    //                                      Error Check
    /////////////////////////////////////////////////////////////////////////////////////////

    if(argc != 2)
    {
        fprintf(stderr, "\nTo use: ./solution <.txt>\n");
        exit(-1);
    }

    ifstream in;
    in.open(argv[1], ios::in);

    if(!in.is_open())
    {
        fprintf(stderr, "\nERROR: file %s not found\n", argv[1]);
        exit(-1);
    }


    /////////////////////////////////////////////////////////////////////////////////////////
    //                                      Read in file to int[]
    /////////////////////////////////////////////////////////////////////////////////////////
    
    string temp;
    int nums = 0;
    while(in.is_open() && !in.eof())
    {
        getline(in, temp);
        ++nums;
    }

    printf("\nLines in file: %i", nums);


    in.clear();
    in.seekg(0, ios::beg);

    char** buffer = new char* [nums];

    for(int i=0; i<nums; ++i)
    {
        getline(in, temp);
        buffer[i] = new char[(sizeof(temp.data())+1)];
        strcpy(buffer[i], temp.data());
        //printf("\nBuffer[%i]: %s", i, buffer[i]);
    }


    /////////////////////////////////////////////////////////////////////////////////////////
    //                               convert to ints       
    /////////////////////////////////////////////////////////////////////////////////////////

    int int_buf[nums];

    printf("\n\n");

    for(int i=0; i<nums; ++i)
    {
        int_buf[i] = stoi(buffer[i]);
        //printf("\nBuffer[%i]: %s", i, buffer[i]);
        //printf("\nInt_Buffer[%i]: %i", i, int_buf[i]);
    }


    /////////////////////////////////////////////////////////////////////////////////////////
    //                               solve       
    /////////////////////////////////////////////////////////////////////////////////////////


    int x = find_nums(int_buf, nums);
    int y = 2020 - x;
    
    int solution = x*y;

    printf("\nSolution: %i, X: %i, Y: %i, X+Y: %i", solution, x, y, x+y);

    //cleanup
    for(int i=0; i<nums; ++i)
    {
        delete[] buffer[i];
        buffer[i] = NULL;
    }


    delete [] buffer;
    buffer = NULL;

    in.close();


    printf("\n\n");

    return 0;
}


int find_nums(int* buffer, int size)
{

    for(int i=0; i<size; ++i)
    {
        for(int j=i+1; j<size; ++j)
        {
            if((buffer[i] + buffer[j]) == 2020)
                return buffer[i];
        }
    }

    return 0;
}





