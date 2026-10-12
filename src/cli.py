import argparse
import logging
import sys
from pathlib import Path

from src.errors import DataValidationError
from src.io_tools import read_text_checked, write_json
from src.log import setup_logging
from src.models import ColumnReport, FileReport

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="datacheck", description="CSV health check")
    sub = p.add_subparsers(dest="command", required=True)
    chk = sub.add_parser("check", help="inspect a csv file")
    chk.add_argument("path", type=Path)
    chk.add_argument("--json-out", type=Path, default=None)
    return p


def cmd_check(path: Path, json_out: Path | None) -> int:
    log = logging.getLogger(__name__)
    log.info("checking %s", path)
    try:
        text = read_text_checked(path)
    except FileNotFoundError:
        print(f"error: file not found: {path}", file=sys.stderr)
        return 1
    except DataValidationError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    lines = [ln for ln in text.splitlines() if ln.strip()]
    header = lines[0].split(",") if lines else []
    report = FileReport(
        path=str(path),
        rows=max(len(lines) - 1, 0),
        columns=[ColumnReport(name=c, dtype="unknown", missing=0, unique=0) for c in header],
    )
    print(f"{report.path}: {report.rows} rows, {len(report.columns)} columns")
    for col in report.columns:
        print(f"  - {col.name}")
    if json_out:
        write_json(json_out, report.to_dict())
        log.info("wrote %s", json_out)
    return 0


def main(argv: list[str] | None = None) -> int:
    setup_logging()
    args = build_parser().parse_args(argv)
    if args.command == "check":
        return cmd_check(args.path, args.json_out)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())