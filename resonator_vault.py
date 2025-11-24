# resonator_vault.py - Data Vault for Synaptic Resonator

import json
import time
from typing import Any, Dict, List


class ResonatorVault:
    """
    In-memory vault for storing and retrieving key/value pairs.
    Useful for quick access during runtime.
    """
    def __init__(self):
        self.storage: Dict[str, Any] = {}
        self.verdicts: Dict[str, Dict[str, Any]] = {}  # glyph -> verdict

    def store(self, key: str, value: Any) -> None:
        """Store a value under a given key."""
        self.storage[key] = value

    def retrieve(self, key: str) -> Any:
        """Retrieve a value by key, or None if not found."""
        return self.storage.get(key)

    def store_verdict(self, glyph: str, verdict: Dict[str, Any]) -> None:
        """Store a verdict by glyph for audit and replay."""
        self.verdicts[glyph] = verdict

    def retrieve_verdict(self, glyph: str) -> Dict[str, Any]:
        """Retrieve a verdict by glyph."""
        return self.verdicts.get(glyph, {})

    def list_verdicts(self) -> List[str]:
        """List all stored verdict glyphs."""
        return list(self.verdicts.keys())


def log_to_vault(entry: Dict[str, Any], vault_name: str = "SynapticVault") -> None:
    """
    Append a JSON-encoded entry to a vault log file.
    Each entry is timestamped for auditability.
    """
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    entry["logged_at"] = timestamp
    filename = f"{vault_name.lower()}.log"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
