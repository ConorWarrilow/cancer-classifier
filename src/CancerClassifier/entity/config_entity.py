from dataclasses import dataclass
from pathlib import Path

# Frozen means we can't add any more functionality to the dataclass after it's created
@dataclass(frozen = True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path