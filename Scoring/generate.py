from rouge_score import rouge_scorer
from rouge_score import scoring

def compute_rouge(truth,generated):
	scorer = rouge_scorer.RougeScorer(
      ["rouge1", "rouge2", "rougeL", "rougeLsum"], use_stemmer=True)
	scores = scorer.score(truth,generated)
	return scores
