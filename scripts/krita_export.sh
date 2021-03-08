#!/bin/bash

# Requires krita and imagemagick

INFILE=$1
FORMAT=${2:-png}
PIXELS=${3:-9216}

if [[ ! $INFILE ]]; then
    exit 1
fi

prefix=`echo $INFILE | cut -d "." -f 1`;
convert_file="${prefix}.${FORMAT}";
pixel_sqrt=`echo $PIXELS | awk '{print sqrt($0)}'`;
resize_file="${prefix}_${pixel_sqrt}px.${FORMAT}";

echo -e "Exporting $INFILE to:"
echo -e "\t${convert_file}"
echo -e "\t${resize_file}"

echo "/mnt/c/Program\ Files/Krita\ \(x64\)/bin/krita.exe --export --export-filename ${convert_file} ${INFILE}";
/mnt/c/Program\ Files/Krita\ \(x64\)/bin/krita.exe --export --export-filename ${convert_file} ${INFILE};
#/c/Program\ Files/Krita\ \(x64\)/bin/krita.exe --export --export-filename ${convert_file} ${INFILE};
echo "convert ${convert_file} -filter point -resize ${PIXELS}@  ${resize_file}";
convert ${convert_file} -filter point -resize ${PIXELS}@  ${resize_file}