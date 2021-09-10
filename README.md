# twelfe
A python script for parsing Linux ELF files.

### Prerequisites:
Uses just one third party library:

* argparse : For parsing command line arguments

*Argparse* should be installed on running the installer for *twelfe*. 
Otherwise run `pip install argparse`.



### Installation

```console
$ git clone https://github.com/G-Nils/twelfe.git

$ cd twelfe

$ pip install -e .
```


# Example:

Print the ELF header:
```console
$ python3 twelfe.py -f test --elf

ELF Header:
Magic:                                ELF
Class:                                64-Bit
Data:                                 Little Endian
Header Version:                       01
OS ABI:                               SYSTEM V
Padding:                              00000000000000
Type:                                 EXEC (executable)
Inst Set:                             x86_64
ELF Version:                          000001
Entry Point:                          0x401040
Start Program Headers:                0x40 bytes into file
Start Section Headers:                0x3920 bytes into file
Flags:                                000000
Header Size:                          0x40 bytes 
Size Program Headers:                 0x38 bytes
Program Header Entries:               0xb
Size Section Headers:                 0x40
Section Header Entries:               0x1d
Section Header String Table Index:    0x1c
```

Print the program headers:
```console
$ python3 twelfe.py -f test --program

Program Headers:
Type               Address(virt)          Address(phy)          Offset        Size(file)       Size(mem)     Flags     Align
PHDR            0x0000000000400040      0x0000000000400040      0x40            0x268           0x268           R--     0x8       
INTERP          0x00000000004002a8      0x00000000004002a8      0x2a8           0x1c            0x1c            R--     0x1       
LOAD            0x0000000000400000      0x0000000000400000      0x              0x438           0x438           R--     0x1000    
LOAD            0x0000000000401000      0x0000000000401000      0x1000          0x1ed           0x1ed           R-E     0x1000    
LOAD            0x0000000000402000      0x0000000000402000      0x2000          0x1a8           0x1a8           R--     0x1000    
LOAD            0x0000000000403e10      0x0000000000403e10      0x2e10          0x220           0x228           RW-     0x1000    
DYNAMIC         0x0000000000403e20      0x0000000000403e20      0x2e20          0x1d0           0x1d0           RW-     0x8       
NOTE            0x00000000004002c4      0x00000000004002c4      0x2c4           0x44            0x44            R--     0x4       
GNU_EH_FRAME    0x0000000000402018      0x0000000000402018      0x2018          0x4c            0x4c            R--     0x4       
GNU_STACK       0x0000000000000000      0x0000000000000000      0x              0x              0x              RW-     0x10      
GNU_RELRO       0x0000000000403e10      0x0000000000403e10      0x2e10          0x1f0           0x1f0           R--     0x1       

R = Read, W = Write, E = Executable
```

Print the section headers:
```console
$ python3 twelfe.py -f test --section

Section Headers: 
ID     Name               Type               Address          Offset     Size     Flags        Info        Link       Align     Entr. Size     
0                        NULL           0x0000000000000000    0x          0x                    0x          0x          0x          0x          
1    .interp             PROGBITS       0x00000000004002a8    0x2a8       0x1c        A         0x          0x          0x1         0x          
2    .note.gnu.build-id  NOTE           0x00000000004002c4    0x2c4       0x24        A         0x          0x          0x4         0x          
3    .note.ABI-tag       NOTE           0x00000000004002e8    0x2e8       0x20        A         0x          0x          0x4         0x          
4    .gnu.hash           GNU_HASH       0x0000000000400308    0x308       0x1c        A         0x          0x5         0x8         0x          
5    .dynsym             DYNSYM         0x0000000000400328    0x328       0x60        A         0x1         0x6         0x8         0x18        
6    .dynstr             STRTAB         0x0000000000400388    0x388       0x3d        A         0x          0x          0x1         0x          
7    .gnu.version        VERSYM         0x00000000004003c6    0x3c6       0x8         A         0x          0x5         0x2         0x2         
8    .gnu.version_r      VERNEED        0x00000000004003d0    0x3d0       0x20        A         0x1         0x6         0x8         0x          
9    .rela.dyn           RELA           0x00000000004003f0    0x3f0       0x30        A         0x          0x5         0x8         0x18        
10   .rela.plt           RELA           0x0000000000400420    0x420       0x18        AI        0x16        0x5         0x8         0x18        
11   .init               PROGBITS       0x0000000000401000    0x1000      0x17        AX        0x          0x          0x4         0x          
12   .plt                PROGBITS       0x0000000000401020    0x1020      0x20        AX        0x          0x          0x10        0x10        
13   .text               PROGBITS       0x0000000000401040    0x1040      0x1a1       AX        0x          0x          0x10        0x          
14   .fini               PROGBITS       0x00000000004011e4    0x11e4      0x9         AX        0x          0x          0x4         0x          
15   .rodata             PROGBITS       0x0000000000402000    0x2000      0x18        A         0x          0x          0x4         0x          
16   .eh_frame_hdr       PROGBITS       0x0000000000402018    0x2018      0x4c        A         0x          0x          0x4         0x          
17   .eh_frame           PROGBITS       0x0000000000402068    0x2068      0x140       A         0x          0x          0x8         0x          
18   .init_array         INIT_ARRAY     0x0000000000403e10    0x2e10      0x8         WA        0x          0x          0x8         0x8         
19   .fini_array         FINI_ARRAY     0x0000000000403e18    0x2e18      0x8         WA        0x          0x          0x8         0x8         
20   .dynamic            DYNAMIC        0x0000000000403e20    0x2e20      0x1d0       WA        0x          0x6         0x8         0x10        
21   .got                PROGBITS       0x0000000000403ff0    0x2ff0      0x10        WA        0x          0x          0x8         0x8         
22   .got.plt            PROGBITS       0x0000000000404000    0x3000      0x20        WA        0x          0x          0x8         0x8         
23   .data               PROGBITS       0x0000000000404020    0x3020      0x10        WA        0x          0x          0x8         0x          
24   .bss                NOBITS         0x0000000000404030    0x3030      0x8         WA        0x          0x          0x1         0x          
25   .comment            PROGBITS       0x0000000000000000    0x3030      0x27        MS        0x          0x          0x1         0x1         
26   .symtab             SMTAB          0x0000000000000000    0x3058      0x5e8                 0x2b        0x1b        0x8         0x18        
27   .strtab             STRTAB         0x0000000000000000    0x3640      0x1d7                 0x          0x          0x1         0x          
28   .shstrtab           STRTAB         0x0000000000000000    0x3817      0x103                 0x          0x          0x1         0x          

W = Write, A = Alloc, X = Executabe, M = Merge, S = Strings, I = Info, O = Link Order, N = OS Nonconforming, G = Group, T = TLS

```

### Developer Information:

Currently all field are **strings**. This results from simply parsing the hex bytes of the file. When integers are needed (for example for calculating), you can use `int(value, 16)` to simply parse the fields.

