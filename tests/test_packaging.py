import subprocess
import sys
import tarfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def test_sdist_includes_requirement_files(tmp_path):
    subprocess.run(
        [sys.executable, "setup.py", "sdist", "--dist-dir", str(tmp_path)],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )

    archive_path = next(tmp_path.glob("cloudconsolelink-*.tar.gz"))
    with tarfile.open(archive_path, "r:gz") as archive:
        archive_names = set(archive.getnames())

    archive_root = archive_path.name.removesuffix(".tar.gz")
    assert f"{archive_root}/requirements.txt" in archive_names
    assert f"{archive_root}/requirements-dev.txt" in archive_names
