# CMPS 2200 Reciation 6
## Answers

**Name:**_____________Dachen (Owen) Ni____________


Place all written answers from `recitation-06.md` here for easier grading.


- **1b.**

Based on the empirical output. When using random permutations of input sizes, the fixed pivot quick sort has the same asymptotic bound as random pivot quick sort O(logn). When, using already sorted permutations, the quick sort using fixed pivot has time of O(n^2), which has the same asymptotic bound as selection sort's, while the random pivot still has runtime of O(nlogn).

runtime using sorted list:

| n    |  ssort |   qsort-fixed-pivot |   qsort-random-pivot |
|------|--------|---------------------|----------------------|
|   10 |  0.006 |               0.008 |                0.008 |     
|  100 |  0.190 |               0.292 |                0.089 |      
|  200 |  0.672 |               1.102 |                0.197 |      
|  500 |  4.165 |               5.967 |                0.468 |     
|  800 | 10.128 |              14.341 |                0.806 |      
| 1000 | 15.511 |              23.795 |                0.970 |      
| 1200 | 22.145 |              31.054 |                1.150 |      
| 1500 | 34.554 |              52.373 |                1.612 |     
| 1800 | 50.196 |              69.492 |                1.931 |      
| 2000 | 61.966 |              86.424 |                2.068 | 

runtime using shuffled list:
|    n |   qsort-fixed-pivot |     ss |   qsort-random-pivot |
|------|---------------------|--------|----------------------|
|   10 |               0.007 |  0.006 |                0.008 |      
|  100 |               0.084 |  0.218 |                0.100 |     
|  200 |               0.189 |  0.777 |                0.210 |    
|  500 |               0.491 |  4.467 |                0.490 |     
|  800 |               0.765 | 10.813 |                0.842 |     
| 1000 |               0.921 | 15.993 |                1.039 |     
| 1200 |               1.095 | 22.705 |                1.250 |     
| 1500 |               1.599 | 34.937 |                1.571 |     
| 1800 |               1.781 | 50.434 |                1.820 |     
| 2000 |               1.900 | 62.313 |                2.037 | 

- **1c.**
The runtime of tim sort is way faster than qsort, no matter input list is sorted or not. Although the qsort random pivot is our quickest algorithm, it is nearly 100 times slower than tim sort.

runtime using sorted list:
|    n |   qsort-fixed-pivot |     ss |   qsort-random-pivot |   tim_sort |
|------|---------------------|--------|----------------------|------------|
|   10 |               0.006 |  0.006 |                0.008 |      0.000 |
|  100 |               0.079 |  0.196 |                0.091 |      0.001 |
|  200 |               0.153 |  0.692 |                0.183 |      0.002 |
|  500 |               0.462 |  4.263 |                0.490 |      0.006 |
|  800 |               0.711 | 10.154 |                0.768 |      0.008 |
| 1000 |               0.922 | 15.709 |                0.980 |      0.009 |
| 1200 |               1.109 | 22.422 |                1.232 |      0.011 |
| 1500 |               1.444 | 35.013 |                1.518 |      0.015 |
| 1800 |               1.732 | 50.257 |                1.941 |      0.017 |
| 2000 |               1.907 | 62.215 |                2.019 |      0.019 |

sorted input:
|    n |   qsort-fixed-pivot |     ss |   qsort-random-pivot |   tim_sort |
|------|---------------------|--------|----------------------|------------|
|   10 |               0.009 |  0.006 |                0.009 |      0.001 |
|  100 |               0.319 |  0.207 |                0.099 |      0.001 |
|  200 |               1.187 |  0.741 |                0.203 |      0.002 |
|  500 |               6.329 |  4.179 |                0.496 |      0.005 |
|  800 |              14.903 | 10.136 |                0.817 |      0.009 |
| 1000 |              23.620 | 15.421 |                0.998 |      0.011 |
| 1200 |              30.486 | 22.234 |                1.249 |      0.011 |
| 1500 |              51.203 | 34.593 |                1.543 |      0.015 |
| 1800 |              70.033 | 49.894 |                1.862 |      0.018 |
| 2000 |              85.328 | 61.702 |                2.069 |      0.021 |