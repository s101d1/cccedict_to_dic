# CC-CEDICT to Google Pinyin DIC Converter

A python script to convert [CC-CEDICT](https://cc-cedict.org/wiki/) file into [Google Pinyin IME](https://www.google.com/intl/zh-CN/ime/pinyin/)'s DIC file.

## Software Requirements
* Python v2.7.x

## Usage

1. Download [CC-CEDICT file](https://www.mdbg.net/chinese/dictionary?page=cc-cedict).

2. Extract and put the CC-CEDICT file in same directory as the script.

3. Run `python cccedict_to_dic.py [cc_cedict_filename] [output_dic_filename]` in console to perform the conversion.

   Example: `python cccedict_to_dic.py cedict_ts.u8 output.dic`
   
   If you use the binary EXE file, run `cccedict_to_dic.exe [cc_cedict_filename] [output_dic_filename]` in console.


## Binary Release

The binary EXE file is provided for Windows user who don't want to use python to run the script.

[Download cccedict_to_dic.exe](https://github.com/s101d1/cccedict_to_dic/releases/download/0.1/cccedict_to_dic.exe)
