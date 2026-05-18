"""
Beginner-friendly data quality walkthrough for Arnio.

This example shows a small messy input, the profiling signals Arnio reports,
the suggested cleaning steps, and the difference between safe and strict
auto-cleaning.
"""

import pandas as pd

import arnio as ar


def main():
    raw = pd.DataFrame(
    {
        "order_id": [1001, 1002, 1002, 1003, 1004],
        "customer": [
            " Ishan ",
            " PRASOON ",
            " Prasoon ",
            "pranay ",
            " Dhruv ",
        ],
        "city": [
            " Paris ",
            "London",
            " london ",
            " New York ",
            " TOKYO ",
        ],
        "score": [95, None, 95, 88, None],
    }
)

    frame = ar.from_pandas(raw)

    print("--- Messy Input ---")
    print(raw)

    report = ar.profile(frame)
    summary = report.summary()
    suggestions = ar.suggest_cleaning(frame)

    print("\n--- Profiling Summary ---")
    print(summary)

    print("\n--- Suggested Cleaning Steps ---")
    print(suggestions)

    safe = ar.auto_clean(frame)
    print("\n--- auto_clean(mode='safe') ---")
    print(ar.to_pandas(safe))

    strict = ar.auto_clean(frame, mode="strict")
    print("\n--- auto_clean(mode='strict') ---")
    print(ar.to_pandas(strict))


if __name__ == "__main__":
    main()
