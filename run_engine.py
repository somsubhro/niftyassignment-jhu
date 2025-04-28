import json
from models import Policy, Request
from evaluator import PolicyEvaluator

def load_policies(filepath):
    with open(filepath) as f:
        policies_data = json.load(f)
    return [Policy(**p) for p in policies_data]

def load_requests(filepath):
    with open(filepath) as f:
        requests_data = json.load(f)
    return [Request(**r) for r in requests_data]

def main():
    policies = load_policies('sample_policies.json')
    requests = load_requests('sample_requests.json')
    evaluator = PolicyEvaluator(policies)

    for idx, request in enumerate(requests):
        result, explanation = evaluator.evaluate_request(request)
        print(f"Request {idx + 1}: {result}")
        print(f"Explanation: {explanation}")
        print()

if __name__ == "__main__":
    main()
