#!/usr/bin/env python
import sys
from os.path import basename
import getopt
import cchardet
import codecs
from itertools import izip_longest
import pysrt
import re
from texts import ssa_header, ssa_line, help_text


def show_help():
    print help_text
    sys.exit(2)


class Error(Exception):
    pass


class MergeSubs(object):
    _TAGS_MAP = {'<i>': '{\\i1}', '</i>': '{\\i0}',  # Italic
                 '<b>': '{\\b1}', '</b>': '{\\b0}',  # Bold
                 '<u>': '{\\u1}', '</u>': '{\\u0}',  # Underline
                 '\n': '\N'  # New line
                 }

    def __init__(self, top_file, sub_file, join=False):
        self.top_file = top_file
        self.sub_file = sub_file
        self.join = join

    def __repr__(self):
        return 'MergeSubs(%s, %s)' % (self.top_file, self.sub_file)

    def _replace_tags(self, text):
        for tag in self._TAGS_MAP:
            text = re.sub(tag, self._TAGS_MAP[tag], text)
        return text

    @staticmethod
    def _file_encoding(file_name):
        try:
            with open(file_name, 'rb') as f:
                encoding = cchardet.detect(f.read()).get('encoding')
        except IOError as e:
            raise Error(e)

        return encoding

    def _open_srt(self, file_name):
        return pysrt.open(file_name,
                          encoding=self._file_encoding(file_name))

    def _generate_new_line(self, data, style):
        def _generate_time(time):
            return '%d:%d:%d.%s' % (time.hours, time.minutes,
                                    time.seconds, str(time.minutes)[:2])

        # Replace newlines for SubStation Alpha
        # SubStation Alpha ignores \n, it uses \N
        return (ssa_line % (_generate_time(data.start),
                            _generate_time(data.end),
                            style,
                            self._replace_tags(data.text)))

    def _generate_new_data(self, merged_lines):
        new_header = ssa_header % ((basename(self.top_file)
                                    + ', ' +
                                    basename(self.sub_file)))

        new_lines = '\n'.join(merged_lines)

        return new_header + new_lines

    @staticmethod
    def _write_new_file(new_file, new_data):
        try:
            f = codecs.open(new_file, 'w', 'utf-8')
            f.write(new_data)
            f.close()
        except:
            raise Error('Unable to write file: %s' % new_file)
        else:
            print ('New file created as name: %s'
                   '\n\nHave a good time!') % new_file

    def do(self):
        top_subs = self._open_srt(self.top_file)
        sub_subs = self._open_srt(self.sub_file)

        merged_lines = list()

        for top, sub in izip_longest(top_subs, sub_subs):
            if top:
                position = 'sub_' if self.join else 'top'
                merged_lines.append(self._generate_new_line(top, position))
            if sub:
                merged_lines.append(self._generate_new_line(sub, 'sub'))

        return self._generate_new_data(merged_lines)


def main():
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, 'hjt:s:n:', ['top=', 'sub=', 'join'])
    except getopt.GetoptError:
        show_help()

    top_file = sub_file = new_file = join = None

    for opt, arg in opts:
        if opt == '-h':
            show_help()
        elif opt in ('-t', '--top'):
            top_file = arg
        elif opt in ('-s', '--sub'):
            sub_file = arg
        elif opt in ('-n', '--new'):
            new_file = arg
        elif opt in ('-j', '--join'):
            join = True

    if not all((top_file, sub_file, new_file)):
        show_help()

    merge_subs = MergeSubs(top_file, sub_file, join)
    new_data = merge_subs.do()
    merge_subs._write_new_file(new_file, new_data)

if __name__ == '__main__':
    main()
