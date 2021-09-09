"""
    twelfe is a simple python utiliy to print ELF file headers, including ELF, section and program headers

"""

import argparse
from typing import Any
from elf import *
from util import read_bytes


def main():
    """
        Main Entry. Validates the passed arguments.

    """

    args = read_args()
    file = args["file"]

    if file == "":
        print("[!]: No file specified")
        exit(-1)

    elf = ELF.from_file(file)

    if args["all"]:
        elf.print_elf_header()
        elf.print_program_headers()
        elf.print_section_headers()
        exit(0)

    if args["elf"]:
        elf.print_elf_header()

    if args["program"]:
        elf.print_program_headers()

    if args["section"]:
        elf.print_section_headers()

    first_addr = int(elf.elf_header.prog_entry, 16)
    #rat = elf.read_at_address(first_addr, 8)
    rat = elf.read_opcodes(first_addr+2, 3)
    print(
        f"Expecting First instruction at: {elf.elf_header.prog_entry} / {rat}")

    executable_section = elf.get_section_by_flag("X")
    for es in executable_section:
        print(es.name)
        print(es.addr.lstrip('0'))
        first_instruction = read_bytes(elf.bytes, int(es.offset, 16), count=8)
        print(f"First instruction: {first_instruction}")


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
