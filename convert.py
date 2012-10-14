import collections
import json
import os
import sys
from resumebabel.resumebabel import ResumeBabel


if __name__ == '__main__':
    print ResumeBabel.get_supported_formats()
    sys.exit()
    input_json = sys.argv[1]
    output_file = sys.argv[2]

    # TODO: make sure output_format is not empty
    output_format = (os.path.splitext(output_file)[1])[1:]


    resume = open(input_json).read()
    r = ResumeBabel(resume)

    out_fd = open(output_file, 'wb')
    r.export_resume(out_fd, output_format)
    out_fd.close()
