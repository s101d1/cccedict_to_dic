# CC-CEDICT to Google Pinyin DIC Converter

A python script to convert [CC-CEDICT](https://cc-cedict.org/wiki/) file into [Google Pinyin IME](https://www.google.com/intl/zh-CN/ime/pinyin/)'s DIC file.

## Software Requirements
* Python v2.7.x

## Usage

1. Download [CC-CEDICT file](https://www.mdbg.net/chinese/dictionary?page=cc-cedict).

2. Extract and put the CC-CEDICT file in same directory as the script.

3. Run `python cccedict_to_dic.py [cc_cedict_filename] [output_dic_filename]` in console to perform the conversion.

   Example: `python cccedict_to_dic.py cedict_ts.u8 output.dic`

4. The output DIC file can be imported into Google Pinyin IME.
