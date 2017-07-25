#!/bin/bash

trap "exit" INT

working_dir=$PWD
engine=$1
n_times=$2
prefix=$3
tmptex_dir=$4

cd ${tmptex_dir}
for i in `seq 1 ${n_times}`
do
    ${engine} output
done
mv output.pdf ${working_dir}/${prefix}.pdf


