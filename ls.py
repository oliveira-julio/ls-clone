from click import command
from click import echo
from click import argument
from pathlib import Path


def ishidden(archive):
    return archive.stem[0] == "."


def isnothidden(archive):
    return not ishidden(archive)


@command()
@argument("path", default=".")
def ls(path):
    """Clone of ls command, write in Python3"""
    my_path = Path(path)

    if not my_path.exists():
        echo("path %s not exist." % my_path)
        return

    if my_path.is_file():
        echo(my_path.stem)
        return

    if my_path.is_dir():
        archives = filter(isnothidden, my_path.iterdir())

        for archive in archives:
            echo(archive.stem)

        return


if __name__ == "__main__":
    ls()
