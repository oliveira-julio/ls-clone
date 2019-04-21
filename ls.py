from click import command
from click import echo
from click import argument
from click import option
from pathlib import Path


def ishidden(archive):
    return archive.stem[0] == "."


def isnothidden(archive):
    return not ishidden(archive)


@command()
@option(
    "-a",
    "--all",
    "hidden",
    help="not ignore archives which start with .",
    is_flag=True,
    default=False,
)
@argument("path", default=".")
def ls(path, hidden):
    """Clone of ls command, write in Python3"""
    my_path = Path(path)

    if not my_path.exists():
        echo("path %s not exist." % my_path)
        return

    if my_path.is_file():
        echo(my_path.stem)
        return

    if my_path.is_dir():
        archives = my_path.iterdir()
        if not hidden:
            archives = filter(isnothidden, archives)

        for archive in archives:
            echo(archive.stem)

        return


if __name__ == "__main__":
    ls()
