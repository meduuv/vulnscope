from vulnscope import filter_by_severity, summarize

def test_filter_and_summary():
    items = [{"severity": "high"}, {"severity": "low"}]
    assert len(filter_by_severity(items, "high")) == 1
    assert summarize(items)["low"] == 1
