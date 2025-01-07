from typing import List, Any

def exact_match_metric(gold: List[Any], pred: List[Any], trace=None) -> float:
    """
    Calculates the exact match accuracy between gold and predicted outputs.
    
    Args:
        gold (List[Any]): List of ground truth values.
        pred (List[Any]): List of predicted values.
        trace: Additional trace information (unused).
    
    Returns:
        float: Exact match accuracy.
    """
    if not gold:
        return 0.0
    correct = sum(1 for g, p in zip(gold, pred) if g == p)
    return correct / len(gold)
