api_logs =[ {"model":"gpt 5.1", "user":"A", "tokens": 100},
            {"model":"gpt 3.5", "user":"C", "tokens": 80},
            {"model":"gpt 4", "user":"B", "tokens": 120},
            {"model":"gpt 4", "user":"B", "tokens": 120},
            {"model":"gpt 5.5", "user":"E", "tokens": 70}
]

def analyse_api_usage(api_logs):
  summary = {}
  
  for log in api_logs:
    model = log["model"]
    tokens = log["tokens"]

    if model not in summary:
      summary[model] = {"total_tokens": 0, "request_count": 0}

    summary[model]["total_tokens"] += tokens
    summary[model]["request_count"] += 1

  return summary
print(analyse_api_usage(api_logs))
