# Puzzle #2 Solution
### Taylor Noah

To Run:  
1) > make  
2) > ./solution puzzle1_input.txt  

Notes:
- To solve this second puzzle I modified the prevoius solutions solve function to accomodate three integer solutions.
- For an added challenge I wrote this assuming the program would have no prior knowledge of the file size.    
- It's not entirely efficient with the nested loops, but since the file is so small I figured it wouldn't hurt.  
- For a bigger file I would have:  
  - used pthreads
  - sorted the input
  - used threads to quickly find solutions
  - consider writing in C  
