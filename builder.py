# -*- coding: utf-8 -*-

import os
import sys

def file2list(filepath):
    ret = []
    with open(filepath, encoding='utf8', mode='r') as f:
        ret = [line.rstrip('\n') for line in f.readlines()]
    return ret

def list2file(filepath, ls):
    with open(filepath, encoding='utf8', mode='w') as f:
        f.writelines(['{:}\n'.format(line) for line in ls] )

def strbool2bool(bytestr):
    l = bytestr.lower()
    if l in ['n', 'no', 'false']:
        return False
    if l in ['y', 'yes', 'true']:
        return True
    raise RuntimeError('Invalid boolean value "{0}".'.format(bytestr))

def raise_option_error(msg, lineno, line):
    raise RuntimeError('{0} at line {1}, "{2}".'.format(msg, lineno, line))

def append_to_out(appendee_list, appender, use_ignore=False):
    if use_ignore:
        return
    appendee_list.append(appender)

def parse_arguments():
    import argparse

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='100q generator.'
    )
    parser.add_argument('-i', '--input', default=None, required=True,
        help='A input filename.')
    parser.add_argument('-o', '--output', default=None, required=True,
        help='A output filename.')

    parser.add_argument('-l', '--limit', default=-1, type=int,
        help='The limit of the number of output. No limit if minus given.')

    parser.add_argument('--opt-category-format', default='## (@)', type=str,
        help='A format of Category Line: You can use `@` for the current line excluded a category mark.')

    parser.add_argument('--opt-question-format', default='## @@ @', type=str,
        help='A format of Question Line: You can use `@@` for the numbering format and `@` for the current line.')

    parser.add_argument('--opt-numbering-format', default='d', type=str,
        help='A format of how to display of Question Line\'s number: Based on python format() function grammer.')

    parser.add_argument('--opt-category-mark', default='##', type=str,
        help='A string to be parsed as a Category Line')

    parser.add_argument('--opt-ignore-blank', default=False, action='store_true',
        help=' if given, ignore blank lines in parsing.')

    args = parser.parse_args()
    return args

args = parse_arguments()

MYDIR = os.path.abspath(os.path.dirname(__file__))
infile = os.path.join(MYDIR, args.input)
outfile = os.path.join(MYDIR, args.output)
limitcount = args.limit

opt_fmt_cate         = args.opt_category_format
opt_fmt_q            = args.opt_question_format
opt_catemark         = args.opt_category_mark
opt_numbering_format = args.opt_numbering_format
opt_ignore_blank     = args.opt_ignore_blank

is_limit_over        = False

lines = file2list(infile)
outlines = []
curno = 1
for i,line in enumerate(lines):
    if limitcount>=0 and curno>limitcount and is_limit_over==False:
        is_limit_over = True
        continue

    # blank line
    if len(line)==0:
        if not opt_ignore_blank:
            append_to_out(outlines, '', is_limit_over)
        continue

    # comment line
    #   ; comment
    #   <!-- comment -->
    #   // comment
    if line[0]==';' or line[0]=='<' or line[0]=='/':
        continue

    # header/footer line
    if line[0]==' ':
        append_to_out(outlines, line[1:])
        continue

    # content line
    #   '-' and '*' is a list grapper in GFM.
    if line[0]=='-' or line[0]=='*':
        # - A question
        # ^^
        # Cut here.
        line = line[1:].strip()

        if line.find(opt_catemark)!=-1:
            appendee = line.replace(opt_catemark, '').strip()
            newline = opt_fmt_cate.replace('@', appendee)
        else:
            numbering_format = '{0:'+opt_numbering_format+'}'
            numbered_format = opt_fmt_q.replace(
                '@@',
                numbering_format.format(curno)
            )
            appendee = line.strip()
            newline = numbered_format.replace('@', appendee)
            curno += 1
        append_to_out(outlines, newline, is_limit_over)
        continue

list2file(outfile, outlines)
