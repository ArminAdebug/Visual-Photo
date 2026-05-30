from pathlib import Path


def get_save_path(path: Path, copy: bool, add_name):
    if copy:
        savepath = Path.joinpath(
            path.parent, path.stem + add_name + path.suffix)
        return savepath
    return path
