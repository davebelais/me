from pathlib import Path

REPOSITORY_ROOT_PATH: Path = Path(__file__).absolute().parent.parent
INDEX_MD: Path = REPOSITORY_ROOT_PATH / "docs" / "index.md"
SOFTWARE_ENGINEER_RESUME_MD: Path = (
    REPOSITORY_ROOT_PATH / "docs" / "software_engineer_resume.md"
)


def main() -> None:
    """
    This is the main entry point for this script
    """
    md: str
    with open(INDEX_MD) as index_io:
        md = index_io.read()
    with open(SOFTWARE_ENGINEER_RESUME_MD, "w") as resume_io:
        resume_io.write(
            md.replace(
                "Data Engineer",
                "Data/Software Engineer",
            )
        )


if __name__ == "__main__":
    main()
