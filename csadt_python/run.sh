#!/bin/bash


echo "##### Running: /usr/bin/python 1_ExcelToText.py 0_RecordLinkageInput100Lines.xlsx A1 T101 100Lines.txt"
/usr/bin/python 1_ExcelToText.py 0_RecordLinkageInput100Lines.xlsx A1 T101 100Lines.txt
echo "##### Running: python 2_TextToDataPreprocessedText.py 100Lines.txt 100LinesPreProcessed.txt"
python 2_TextToPreprocessedText.py 100Lines.txt 100LinesPreProcessed.txt

echo "##### Running: python 3_PreprocessedTextToTree.py 100LinesPreProcessed.txt conditions.txt Tree.txt"
python 3_PreprocessedTextToTree.py 100LinesPreProcessed.txt conditions.txt Tree.txt
###echo "##### Running: python 4_TestingDataToTree.py 200TestingData.txt Tree.txt"
###python 4_TestingDataToTree.py 200TestingData.txt Tree.txt
