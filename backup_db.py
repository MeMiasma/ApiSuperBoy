"""Create a consistent SQLite backup using SQLite's online backup API."""
import os, sqlite3, time
from pathlib import Path

source = Path(os.environ.get("DATABASE_PATH", Path(__file__).with_name("shop.db")))
backup_dir = Path(os.environ.get("BACKUP_DIR", Path(__file__).with_name("backups")))
backup_dir.mkdir(parents=True, exist_ok=True)
if not source.exists():
    raise SystemExit(f"Database does not exist: {source}")
target = backup_dir / f"shop-{time.strftime('%Y%m%d-%H%M%S')}.sqlite3"
with sqlite3.connect(source) as src, sqlite3.connect(target) as dst:
    src.backup(dst)
print(f"Backup created: {target}")
