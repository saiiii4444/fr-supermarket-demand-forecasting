"""Utility script to download the Online Retail dataset.

This keeps the GitHub repository small while still allowing you
to reproduce the full pipeline locally.

Usage:
    python download_raw_data.py
"""

import os
import pathlib
import urllib.request


UCI_URL = (
    "https://archive.ics.uci.edu/ml/machine-learning-databases/00352/"
    "Online%20Retail.xlsx"
)


def main() -> None:
    root = pathlib.Path(__file__).resolve().parent
    raw_dir = root / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    target = raw_dir / "online_retail.xlsx"

    if target.exists():
        print(f"File already exists at {target} (size={target.stat().st_size} bytes).")
        return

    print("Downloading Online Retail dataset from UCI...")
    print(f"URL: {UCI_URL}")
    print(f"Destination: {target}")
    urllib.request.urlretrieve(UCI_URL, target)
    print("Download finished.")
    print(f"Final size: {target.stat().st_size} bytes")


if __name__ == "__main__":
    main()
