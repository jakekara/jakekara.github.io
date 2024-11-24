from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
import os
import subprocess
import sys
from typing import Literal, Optional

DESTINATION_ROOT = "assets/images"


@dataclass
class OutputFormat:
    folder_path: str
    new_ext: Literal["avif", "jpg", "webp"]
    width: int
    height: Optional[int] = None
S

def run_command(command):

    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"command failed: {command}", file=sys.stderr)

def convert_width(
    *,
    in_file: str,
    output_subdirectory: str,
    out_name: str,
    ext: str,
    widths: list[str],
    no_width_suffix: bool = False
):

    output_directory = os.path.join(DESTINATION_ROOT, output_subdirectory)

    commands = []
    for width in widths:

        if no_width_suffix:
            out_path = os.path.join(
                output_directory, f"{out_name}.{ext}"
            )

        else:
            out_path = os.path.join(
                output_directory, f"{out_name}-{width}.{ext}"
            )

        os.makedirs(output_directory, exist_ok=True)
        command = f"convert {in_file} -resize {width}x {out_path}"

        commands.append(command)

    with ThreadPoolExecutor() as executor:
        list(executor.map(run_command, commands))


def convert_avif(in_file, out_name):

    convert_width(
        in_file=in_file,
        out_name=out_name,
        output_subdirectory="avif",
        ext="avif",
        widths=[300, 600, 1000, 2000, 3000, 4000],
    )


def convert_jpg(in_file, out_name):

    convert_width(
        in_file=in_file,
        out_name=out_name,
        output_subdirectory="jpg",
        ext="jpg",
        widths=[300, 600, 1000, 2000, 3000, 4000],
    )


def convert_webp(in_file, out_name):

    convert_width(
        in_file=in_file,
        out_name=out_name,
        output_subdirectory="webp",
        ext="webp",
        widths=[300, 600, 1000, 2000, 3000, 4000],
    )


def convert_fixed_ratio(in_file, out_name, output_subdirectory, width, height):

    parent_dir = os.path.join(DESTINATION_ROOT, output_subdirectory)
    out_path = os.path.join(parent_dir, f"{out_name}.jpg")

    os.makedirs(parent_dir, exist_ok=True)
    run_command(f"convert {in_file} -resize {width}x{height}^ -gravity center -extent {width}x{width} {out_path}")


def convert_og(in_file, out_name):

    convert_fixed_ratio(in_file, out_name, "og", 2400, 1260)


def main():
    if len (sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} IN_FILE IMAGE_NAME")
        exit(1)

    in_file = sys.argv[1]
    out_name = sys.argv[2]

    convert_avif(in_file, out_name)
    convert_jpg(in_file, out_name)
    convert_webp(in_file, out_name)
    convert_og(in_file, out_name)


if __name__ == "__main__":
    main()
