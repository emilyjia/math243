#!/bin/bash
# $1 = keyword $2 = source $3 = url_file $4 = text_file $5 = pages $6 = count_file

keyword=$1
source=$2
url_file=$3
text_file=$4
pages=$5
count_file=$6
# takes a text file and parses it
python url.py $keyword $source $url_file $pages
python3 news_text.py $url_file $text_file $keyword
/Users/Emily/Documents/stanford-parser/lexparser.sh $text_file > $count_file
