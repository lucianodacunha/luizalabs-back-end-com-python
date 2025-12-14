"""
Para melhor aproveitamento, instalar a extensao SQLITE Viewer, do VSCode.
"""

import sqlite3

from pathlib import Path


ROOT_PATH = Path(__file__).parent
conn = sqlite3.connect(ROOT_PATH / "clientes.sqlite")
print(conn)

