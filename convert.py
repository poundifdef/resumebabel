import collections
import json
import os
import sys
from resumebabel.resumebabel import ResumeBabel


if __name__ == '__main__':
    input_json = sys.argv[1]
    output_file = sys.argv[2]

    # TODO: make sure output_format is not empty
    output_format = (os.path.splitext(output_file)[1])[1:]


    resume = open(input_json).read()
    r = ResumeBabel(resume)

    out_fd = open(output_file, 'wb')
    out_fd.write(r.export_resume(output_format))
    out_fd.close()
