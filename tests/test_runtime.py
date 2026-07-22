import time

from robin_open.runtime import Candidate, Workflow, keyword_worker


def test_selects_highest_scoring_candidate_and_keeps_trace():
    workflow = Workflow([
        keyword_worker("low", keywords=["missing"], answer="low"),
        keyword_worker("high", keywords=["agent", "memory"], answer="high"),
    ])
    result = workflow.run("agent memory")
    assert result.answer == "high"
    assert result.candidates[-1].worker == "high"
    assert [event.name for event in result.events][-2:] == ["workflow.selected", "workflow.finished"]


def test_one_worker_failure_does_not_abort_the_run():
    def broken(_: str) -> Candidate:
        raise RuntimeError("boom")

    workflow = Workflow([("broken", broken), keyword_worker("ok", keywords=["task"], answer="works")])
    result = workflow.run("task")
    assert result.answer == "works"
    assert result.failures and "broken" in result.failures[0]
    assert any(event.name == "worker.failed" for event in result.events)


def test_timeout_keeps_completed_candidates_and_records_slow_worker():
    def slow(_: str) -> Candidate:
        time.sleep(0.1)
        return Candidate("late", 1.0, "slow")

    workflow = Workflow([("slow", slow), keyword_worker("fast", keywords=["task"], answer="ready")])
    result = workflow.run("task", timeout=0.01)
    assert result.answer == "ready"
    assert any("slow: TimeoutError" in failure for failure in result.failures)
