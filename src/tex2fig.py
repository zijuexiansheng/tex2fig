#!/usr/bin/env python

import os
import sys
import argparse

#script_dir=os.path.dirname( os.path.abspath(os.path.realpath(__file__)) )
script_dir = os.path.join( os.environ['LOONCONFIG'], "tex2fig")

def main(args):
    working_dir="/tmp/tex2fig-{}/".format( os.getpid() )
    os.system("mkdir -p %s" % working_dir)
    img_path = ""
    if args.img:
        img_path = "\\graphicspath{{%s/}}" % os.path.abspath(os.path.realpath( args.img ))
    with open(os.path.join(script_dir, "tex2fig.tmpl"), "r") as fin:
        tmpl = fin.read()
    with open(args.infile, "r") as fin:
        infile_data = fin.read()
    with open(os.path.join(working_dir, "output.tex"), "w") as fout:
        fout.write(tmpl % (args.width, img_path, infile_data))
    os.system("%s %s %s %s %s" % (os.path.join(script_dir, "tex2fig.sh"), args.engine, args.n, args.prefix, working_dir))
    os.system("rm -rf %s" % working_dir)

def parse_argument():
    parser = argparse.ArgumentParser(description = "Convert tex to standalone pdf file")
    parser.add_argument('-p', dest='prefix', type=str, metavar='prefix', default='output', help='Prefix of the output file name (default "output")')
    parser.add_argument('-w', dest='width', type=float, metavar='width', default='21', help='Set maximum page width (cm)')
    parser.add_argument('-E', dest='engine', type=str, metavar='engine', default='lualatex', choices=['pdflatex', 'xelatex', 'lualatex'], help='Set compiling engines (default lualatex)')
    parser.add_argument('-n', dest='n', type=int, metavar='n', default=1, help='Set compiling times (default 1)')
    parser.add_argument('-i', dest='img', type=str, metavar='img', help='Image folder (default: None)')
    parser.add_argument(dest='infile', type=str, metavar='infile', help='Tex file name')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_argument()
    main(args)
