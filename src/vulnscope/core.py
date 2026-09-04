ORDER = {"critical": 4, "high": 3, "medium": 2, "low": 1, "info": 0}

def filter_by_severity(items, minimum="low"):
    threshold = ORDER.get(minimum.lower(), 0)
    return [x for x in items if ORDER.get(str(x.get("severity", "info")).lower(), 0) >= threshold]

def summarize(items):
    return {level: sum(1 for x in items if str(x.get("severity", "info")).lower() == level) for level in ORDER}
