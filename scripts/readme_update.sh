#!/bin/bash

README=$1
IMAGE=$2
BASE="https://raw.githubusercontent.com/ktmeaton/pixilart/master"

new_readme=`cat $README | head -n -2`

filename=`basename $IMAGE`;
dirname=`dirname $IMAGE`;

year=`echo $dirname | cut -d "/" -f 2`;
month=`echo $dirname | cut -d "/" -f 3`;
day=`echo $filename | cut -d "_" -f 1`;

tag=`echo $filename | cut -d "_" -f 2`;
title=`echo $filename | cut -d "_" -f 3 | cut -d "." -f 1 | sed 's/-/ /g'`;
src=$BASE/$IMAGE

new_element="    <td align='center'>
        <a href='$src'>
            <img src='$src' width='100px;' alt=''/>
            <br />
            <sub>
                <b>$title</b>
            </sub>
        </a>
        <br />
        <small>${year}-${month}-${day}</small>
        <br />
        <a href='https://www.pixilart.com/search?term=$tag'>#$tag</a>
    </td>"

mv $README $README.bak

echo -e "$new_readme" > $README
echo -e "$new_element" >> $README
echo -e "  </tr>" >> $README
echo -e "</table>" >> $README


