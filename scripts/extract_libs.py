import argparse
import glob
import os
import shutil
import tempfile
import zipfile
from fnmatch import fnmatch

PATTERNS_LIB = "*/lib/*"


def extract_libs(filename: str, output: str) -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        with zipfile.ZipFile(filename) as zf:
            for name in zf.namelist():
                if fnmatch(name, PATTERNS_LIB):
                    zf.extract(name, tmpdir)

        os.makedirs(output, exist_ok=True)

        for file in glob.glob(f"{tmpdir}/*/{PATTERNS_LIB}"):
            shutil.move(file, output)

        for file in glob.glob(f"{tmpdir}/*/{PATTERNS_LIB}/"):
            shutil.move(file, output)


def main():
    parser = argparse.ArgumentParser(
        description="Extract libraries from the SDK zip file",
    )
    parser.add_argument(
        "filename",
        type=str,
        help="The SDK zip file",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="The output directory",
        default="libs",
    )
    args = parser.parse_args()

    extract_libs(args.filename, args.output)


if __name__ == "__main__":
    main()
