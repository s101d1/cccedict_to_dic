#!/usr/bin/python

import sys
import io
import re

arguments = sys.argv[1:]

if len(arguments) < 2:
    print 'Usage: ' + sys.argv[0] + ' [input_cccedit_file] [output_dic_file]'
    sys.exit()

inputFN = arguments[0]
outputFN = arguments[1]

# Input file should be a CC-CEDICT file with UTF-8 encoding.
# Output file would be a google pinyin input dic file with GBK encoding.
with io.open(inputFN, 'r', encoding = 'utf8') as inFile, io.open(outputFN, 'w+', encoding = 'gbk') as outFile:
    writeCount = 0

    # Each line represents the CC-CEDICT entry: Traditional Simplified [pin1 yin1] /English equivalent 1/equivalent 2/
    # See https://cc-cedict.org/wiki/format:syntax for more details.
    # We would only care for the "Traditional Simplified [pin1 yin1]" part.
    for line in inFile:
        # Skip comment line
        if line.startswith('#'):
            continue

        # Locate the pinyin's brackets position
        firstBracketIndex = line.find('[')
        lastBracketIndex = line.find(']')

        # If the brackets are not found, the entry is invalid so skip it
        if firstBracketIndex == -1 or lastBracketIndex == -1:
            continue

        # Fetch the "Traditional Simplified" part into list
        chineseWords = re.split(r'\s+', line[:firstBracketIndex].strip())

        # We only need the traditional chinese word for the dic entry
        tradChineseWord = chineseWords[0]

        # Skip chinese word entry that contains non-chinese characters
        if bool(re.search(ur'[^\u4e00-\u9fff]', tradChineseWord)):
            continue

        # Fetch the "pin1 yin1" part (not including the brackets) and remove the number characters.
        # So for example, "pin1 yin1" will become "pin yin".
        pinyin = re.sub('[\d]', '', line[firstBracketIndex+1:lastBracketIndex].strip()).lower()

        # Convert certain pinyin so they are compatible with google pinyin's dic format
        pinyin = pinyin.replace('u:', 'v').replace('ve', 'ue')

        # Skip entry with pinyin that are not compatible with google pinyin
        if pinyin == 'xx':
            continue

        # Skip chinese word entry that have unequal pinyins which is unacceptable in google pinyin dic
        pinyins = re.split(r'\s+', pinyin)
        if len(tradChineseWord) != len(pinyins):
            continue

        # Write the result dic entry to output file.
        # Result entry format: <chinese_word><TAB>1<TAB><pinyin>
        outFile.write(tradChineseWord + '\t1\t' + pinyin + '\n')

        writeCount += 1

    if writeCount > 0:
        print 'Successfully created dic file'
