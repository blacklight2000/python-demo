import benchmark
from fibonacci1 import *

class Benchmark_Sqrt(benchmark.Benchmark):
    each = 100 # allows for differing number of runs
    def test_case1(self):
        Case1.fibonacci(20)
    def test_case2(self):
        Case2.fibonacci(20)

if __name__ == '__main__':
    benchmark.main(format="markdown", numberFormat="%.4g")
