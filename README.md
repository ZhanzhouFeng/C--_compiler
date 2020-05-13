# 编译原理大作业

#### Description
使用python实现的对C--语言的词法分析、语法分析

#### Software Architecture
+ **词法分析器**的输入为字符串（带进行词法分析的源程序），分析器从 左到右扫描每行源程序的符号，按照 C—的语法进行分析，并将其转化 为 TOKEN 字（单词种别码，自身值），输出到文件中，为进一步语法分析 程序做基础。

+ **语法分析器**的输入为字符串（带进行词法分析的源程序），处理过程 分为词法分析和语法分析，词法分析使用上述的词法分析器， 语法分析部分使用 ll（1）语法进行分析，输出为 ll（1）文法下的产生 语法树所用的产生式的推导，并将字符表示翻译成汉字和单词，便于阅 读。 

#### Algorithm

+ **词法分析器**：分析器从左到右扫描每行源程序的符号，按照 C—的 语法进行分析，并将其转化为 TOKEN 字，送入文件中等待语法分析进一 步处理。 
+ **语法分析器**：分析器分别构建符号栈和输入串两个栈，分别依次从 左到右和从右到左读取，按照 ll（1）的语法进行分析，对其进行输入 和规约，输出 ll（1）文法下的产生语法树所用的产生式的推导。 
