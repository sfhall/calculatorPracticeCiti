import logging

def safe_eval(expr_str):
    if expr_str:
        return eval(expr_str, {"__builtins__": None}, None))
    else logging.debug('ERROR: expression string is empty.')