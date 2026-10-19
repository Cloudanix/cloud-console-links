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


def test_sdist_rebuilds_with_its_own_version(tmp_path):
    # pip/uv install an sdist by rebuilding it from the unpacked tarball, where there is no git.
    # Before: setup.py fell back to __init__.__version__ there (4.0.1), so installing 4.1.2 failed
    # with "Package metadata version 4.0.1 does not match given version 4.1.2".
    dist_dir = tmp_path / "dist"
    subprocess.run(
        [sys.executable, "setup.py", "sdist", "--dist-dir", str(dist_dir)],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    archive_path = next(dist_dir.glob("cloudconsolelink-*.tar.gz"))
    built_version = archive_path.name.removesuffix(".tar.gz").removeprefix("cloudconsolelink-")
    unpack_dir = tmp_path / "unpacked"
    with tarfile.open(archive_path, "r:gz") as archive:
        archive.extractall(unpack_dir, filter="data")

    rebuilt = subprocess.run(
        [sys.executable, "setup.py", "--version"],
        cwd=unpack_dir / archive_path.name.removesuffix(".tar.gz"),
        check=True,
        capture_output=True,
        text=True,
    )

    assert rebuilt.stdout.strip().splitlines()[-1] == built_version


def test_egg_info_excludes_local_bootstrap_requirement(tmp_path):
    subprocess.run(
        [sys.executable, "setup.py", "egg_info"],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )

    requires_path = REPO_ROOT / "cloudconsolelink.egg-info" / "requires.txt"
    requires_text = requires_path.read_text(encoding="utf-8")

    assert "." not in requires_text.splitlines()
    assert "-e ." not in requires_text
