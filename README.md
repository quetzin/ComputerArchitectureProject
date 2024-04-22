# Project README.md
Evaluating bubble sort performance across different systems in two different languages: python and C++.

We are presenting as the first group on April 22rd.


## Our Systems
- Quetzin's Mac, Apple M1 Max with 10 cores @ 2.06 Ghz, 16GB
- Quetzin's Mac, Intel i7 9750H with with 6 cores @ 2.6 GHz, 16GB
- Quetzin's Windows, Intel i7 11700K with 8 cores @ 3.6 GHz, 32GB
- Quetzin's Windows, Intel i9 10850K with 10 cores @ 3.6 GHz, 32GB
- Tanner's Windows, Intel i7 4790k with 4 cores @ 4.0 GHz, 16GB
- Tanner's Windows, AMD Ryzen 7 5800H with 8 cores @ 3201 MHz, 16GB
- Suman's Windows, Intel i7-9750H with 6 cores @ 2.60 GHz, 16GB
- Youssef's Windows, 11th Gen Intel i7-11800H @ 2.30GHZ, 2304 Mhz, 8 cores 16 Logical Processors
- (eros linux server, zeus linux server) AMD EPYC 7513 32-Core Processor, Architecture (x86_64)

## How to Run These Programs

### C++
> `g++ insertionSort.cpp -o output`
> `./output`
- I think these gcc commands are only for compiling on linux (TXST's zeus/eros servers). We really should compile and run them on our own computers for performance evaluation. - Tanner

### Python
> `python bubbleSort.py`
