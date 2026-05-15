from datetime import datetime
from typing import Any


class FortiWebConnector:
    def __init__(self, config: dict[str, Any]) -> None:
        self.config = config

    def health_check(self) -> dict[str, Any]:
        host = str(self.config.get("host") or "").rstrip("/")
        ingest_mode = str(self.config.get("ingestMode") or "push")
        if not host:
            return {
                "ok": False,
                "status": "missing_host",
                "device": {},
                "message": "FortiWeb host is required",
            }
        return {
            "ok": True,
            "status": "ready",
            "device": {
                "vendor": "Fortinet",
                "product": "FortiWeb",
                "host": host,
                "ingestMode": ingest_mode,
            },
            "message": "FortiWeb add-on is ready for push telemetry",
        }

    def get_widget_data(self, req: dict[str, Any]) -> dict[str, Any]:
        return {
            "status": "ready",
            "data": {
                "message": "FortiWeb WAF events are surfaced through SIEM widgets",
                "widgetId": req.get("widget_id"),
            },
            "meta": {"source": "fortiweb", "mode": "push"},
        }

    def ingest_events(self, since: datetime | None) -> list[dict[str, Any]]:
        return []

    def close(self) -> None:
        return None


def get_connector(config: dict[str, Any]) -> FortiWebConnector:
    return FortiWebConnector(config)
