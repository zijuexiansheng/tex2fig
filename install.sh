#!/usr/bin/env bash

mkdir bin/
mkdir script_dir/
cp src/tex2fig.py bin/tex2fig
cp src/tex2fig.sh script_dir/tex2fig.sh
cp src/tex2fig.tmpl script_dir/tex2fig.tmpl

echo "Done"
echo "Add the following command in your .bashrc or .zshrc file before using tex2fig"
echo "  export PATH=$PWD/bin:\$PATH"
echo "  export LOONCONFIG=$PWD/script_dir"

