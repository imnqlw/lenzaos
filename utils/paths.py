def abs_path_from_project(relative_path: str):
    import pages
    from pathlib import Path

    return (
        Path(pages.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
