from server.services import eval_service

def test_simple_eval():
    assert eval_service.safe_eval('21 * 4') == 84
    assert eval_service.safe_eval('42 + 5') == 47
    assert eval_service.safe_eval('1 / 1') == 1