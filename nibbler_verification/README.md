RISC-V ILA for Nibbler
---------------

User Level ISA : RV32I

* 8 branch/jump instructions
* 5 load instructions
* 3 store instructions
* 10 ALU instructions
* 9 ALU-immediate instructions
* 2 immediate instructions

**For verification**
1. ```mkdir build && mkdir verification && cd build```
2. ```cmake .. && build && ./RiscV_RV32IExe```
3. ```cd ../verification/ADD && bash run.sh```
