#!/usr/bin/env python3
'''
/************************/
/*     enc_dec.py       */
/*     Version 1.0      */
/*     2024/03/14       */
/************************/
'''
import argparse
from mod_enc_dec import decode, encode
import sys


def main():
    parser = argparse.ArgumentParser(
        description='encode decode HP48GX functions')
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument(
        '-d', '--decode', action='store_true', help='perform decoding')
    group.add_argument(
        '-e', '--encode', action='store_true', default=True,
        help='perform encoding')
    parser.add_argument(
        '-i', '--input-file', help='input file', default='')
    parser.add_argument(
        '-o', '--output-file', help='output file', default='')
    parser.add_argument(
        '-t', '--enc_type', type=int, default=3, help='encoded type')

    args, unknown = parser.parse_known_args()
    if not args.input_file and len(unknown) == 1:
        args.input_string = unknown[0]
    elif not args.input_file:
        parser.error("If no input file is provided, a string must "
                     "be given as the last argument.")

    if args.decode:
        result = decode(
            args.input_file or args.input_string, isFile=bool(args.input_file))
    else:
        result = encode(
            args.input_file or args.input_string, isFile=bool(args.input_file),
            enc_type=args.enc_type)

    if args.output_file:
        with open(args.output_file, 'w') as f:
            f.write(result)
    else:
        print(result)


if __name__ == '__main__':
    if sys.version_info[0] < 3:
        raise 'Must be using Python 3'
    main()
