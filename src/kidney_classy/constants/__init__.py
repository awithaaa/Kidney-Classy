from pathlib import Path

# Resolve project root dynamically
PROJECT_ROOT = Path(__file__).resolve()
while PROJECT_ROOT.name != "src":
    PROJECT_ROOT = PROJECT_ROOT.parent
PROJECT_ROOT = PROJECT_ROOT.parent 

CONFIG_FILE_PATH = PROJECT_ROOT / "config" / "config.yaml"
PARAMS_FILE_PATH = PROJECT_ROOT / "params.yaml"
