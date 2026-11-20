"""Offline portfolio example using synthetic events. No external services."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Event:
    action: str
    revision: int


def check_trace(events: list[Event]) -> bool:
    """Accept a single draft's trace only if each dry run had current approval."""
    current = 0
    approved = None
    for event in events:
        if event.action == "draft" and event.revision > current:
            current = event.revision
            approved = None
        elif not current or event.revision != current:
            return False
        elif event.action == "approve":
            approved = current
        elif event.action == "reject":
            approved = None
        elif event.action == "dry_run" and approved == current:
            approved = None
        else:
            return False
    return True


if __name__ == "__main__":
    draft = Event("draft", 1)
    approve = Event("approve", 1)
    publish = Event("dry_run", 1)
    cases = [
        ("reviewed revision", [draft, approve, publish], True),
        ("missing approval", [draft, publish], False),
        ("edited after review", [draft, approve, Event("draft", 2), Event("dry_run", 2)], False),
        ("approval withdrawn", [draft, approve, Event("reject", 1), publish], False),
        ("approval reused", [draft, approve, publish, publish], False),
    ]
    for name, events, expected in cases:
        valid = check_trace(events)
        print(f"{name}: {'accepted' if valid else 'rejected'}")
        if valid != expected:
            raise SystemExit(f"Unexpected result for {name}")
