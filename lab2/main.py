import argparse
import re

from console import console_utility

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="console utility")
    parser.add_argument("-source_filename", dest="source_filename", type=str)
    parser.add_argument("-output_filename", dest="output_filename", type=str)
    parser.add_argument("-source_type", dest="source_type", type=str)
    parser.add_argument("-output_type", dest="output_type", type=str)
    parser.add_argument("-config_file", dest="config_file_name", type=str)

    args = parser.parse_args()

    source_filename = None
    output_filename = None
    source_type = None
    output_type = None

    if args.config_file_name is not None:
        config_file_name = re.search(r"(.+)\.py$", args.config_file_name).group(1)
        module = __import__(config_file_name)

        source_filename = module.source_filename
        output_filename = module.output_filename
        source_type = module.source_type
        output_type = module.output_type

    else:
        source_filename = args.source_filename
        output_filename = args.output_filename
        source_type = args.source_type
        output_type = args.output_type

    console_utility(source_filename, output_filename, source_type, output_type)
