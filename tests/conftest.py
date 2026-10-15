"""Shared test setup: ensure the sub-agents script directory is on sys.path."""

from __future__ import annotations

import sys
from collections.abc import Iterator
from pathlib import Path
from unittest.mock import patch

import pytest

SCRIPTS_DIR = Path(__file__).parent.parent / "skills" / "sub-agents" / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))


@pytest.fixture(autouse=True)
def _opencode_is_v1() -> Iterator[None]:
    """Keep OpenCode command construction independent of the binary on PATH."""
    with patch("_builder._opencode_is_v2", return_value=False):
        yield
