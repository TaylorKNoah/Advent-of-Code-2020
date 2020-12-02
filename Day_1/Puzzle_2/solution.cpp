#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

int find_nums(int* buffer, int size, int* solutions);


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

    int solutions[3];

    find_nums(int_buf, nums, solutions);

    printf("\nSolutions: %i, %i, %i", solutions[0], solutions[1], solutions[2]);
    printf("\nSolution: %i", (solutions[0] * solutions[1] * solutions[2]));

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


int find_nums(int* buffer, int size, int* solutions)
{
    for(int i=0; i<size; ++i)
    {
        for(int j=i+1; j<size; ++j)
        {
            for(int k=j+1; k<size; ++k)
            {
                if(buffer[i] + buffer[j] + buffer[k] == 2020)
                {
                    solutions[0] = buffer[i];
                    solutions[1] = buffer[j];
                    solutions[2] = buffer[k];
                }
            }
        }
    }


    return 0;
}





