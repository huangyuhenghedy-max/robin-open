from robin_open.demo import DEFAULT_TASK, render_demo, run_demo


def test_demo_exposes_scores_failure_isolation_and_trace():
    result = run_demo(DEFAULT_TASK)
    output = render_demo(result, color=False)

    assert "parallel workers" in output
    assert "architect      91/100" in output
    assert "1 worker failure kept outside the result" in output
    assert "unavailable failed | isolated" in output
    assert "selected architect | score 91" in output
