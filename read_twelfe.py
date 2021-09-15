"""
    read_twelfe is a simple python utiliy to print ELF file headers, including ELF, section and program headers

"""

import argparse
from twelfe.elf import ELF
from typing import Any
# from twelfe import elf.ELF


def main():
    """
        Main Entry. Validates the passed arguments.

    """

    args = read_args()
    file = args["file"]

    if file == "":
        print("[!]: No file specified")
        exit(-1)

    elffile = ELF.from_file(file)

    if args["all"]:
        elffile.print_elf_header()
        elffile.print_program_headers()
        elffile.print_section_headers()
        exit(0)

    if args["elf"]:
        elffile.print_elf_header()

    if args["program"]:
        elffile.print_program_headers()

    if args["section"]:
        elffile.print_section_headers()


def read_args() -> dict[str, Any]:
    """
        Creates the argparse argument parser

        Returns:
            dict[str, Any]
                The dictionary of read command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file",
                        help="Path to ELF file", required=True, default="")
    parser.add_argument("-e", "--elf",
                        help="Print ELF Header", action="store_true")
    parser.add_argument("-s", "--section",
                        help="Print Section Headers", action="store_true")
    parser.add_argument("-p", "--program",
                        help="Print Program Headers", action="store_true")
    parser.add_argument("-a", "--all",
                        help="Print All Headers", action="store_true")
    return vars(parser.parse_args())


if __name__ == "__main__":
    main()
