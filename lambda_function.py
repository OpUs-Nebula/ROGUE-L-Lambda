import json
from Scoring.generate import * 

def lambda_handler(event, context):
    # TODO implement
    summaries = event['body']
    truth = summaries["truth"]
    generated = summaries["generated"]
    return {
        'statusCode': 200,
        'body': json.dumps(compute_rouge(truth,generated))
    }

if __name__ == "__main__":
	truth = open("Test/baseline.txt").read()
	generated = open("Test/generated.txt").read()
	score = compute_rouge(truth,generated)
	print(score)
	print("Test done!")