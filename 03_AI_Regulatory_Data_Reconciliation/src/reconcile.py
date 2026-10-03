import pandas as pd
from pathlib import Path

# ---------------------------------------------------------
# AI-Assisted Regulatory Data Reconciliation
# ---------------------------------------------------------
# This script compares two synthetic regulatory-reporting
# datasets and identifies reconciliation exceptions.
#
# IMPORTANT:
# All data used in this project is synthetic and created
# solely for portfolio demonstration purposes.
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"

SOURCE_A = DATA_DIR / "source_a.csv"
SOURCE_B = DATA_DIR / "source_b.csv"
OUTPUT_FILE = OUTPUT_DIR / "reconciliation_results.csv"


def load_data():
    """Load the two synthetic source datasets."""

    source_a = pd.read_csv(SOURCE_A)
    source_b = pd.read_csv(SOURCE_B)

    return source_a, source_b


def identify_duplicates(source_b):
    """Identify duplicate record IDs in Source B."""

    duplicate_ids = source_b.loc[
        source_b.duplicated(subset=["record_id"], keep=False),
        "record_id"
    ].unique()

    return set(duplicate_ids)


def reconcile(source_a, source_b):
    """Compare Source A and Source B and classify exceptions."""

    duplicate_ids = identify_duplicates(source_b)

    # Keep one copy for record-level comparison.
    source_b_unique = source_b.drop_duplicates(
        subset=["record_id"],
        keep="first"
    )

    merged = source_a.merge(
        source_b_unique,
        on="record_id",
        how="outer",
        suffixes=("_a", "_b"),
        indicator=True
    )

    results = []

    for _, row in merged.iterrows():

        record_id = row["record_id"]

        # Duplicate takes priority as a control exception.
        if record_id in duplicate_ids:
            status = "Duplicate Record"
            variance = 0
            issue = "Record appears more than once in Source B"

        elif row["_merge"] == "left_only":
            status = "Missing Record"
            variance = 0
            issue = "Record exists in Source A but is missing from Source B"

        elif row["_merge"] == "right_only":
            status = "Unexpected Record"
            variance = 0
            issue = "Record exists in Source B but not Source A"

        elif row["business_unit_a"] != row["business_unit_b"]:
            status = "Attribute Mismatch"
            variance = 0
            issue = "Business unit differs between sources"

        elif row["reporting_period_a"] != row["reporting_period_b"]:
            status = "Attribute Mismatch"
            variance = 0
            issue = "Reporting period differs between sources"

        elif row["metric_name_a"] != row["metric_name_b"]:
            status = "Attribute Mismatch"
            variance = 0
            issue = "Metric name differs between sources"

        elif row["currency_a"] != row["currency_b"]:
            status = "Attribute Mismatch"
            variance = 0
            issue = "Currency differs between sources"

        elif row["reported_amount_a"] != row["reported_amount_b"]:
            status = "Amount Variance"
            variance = abs(
                row["reported_amount_a"] - row["reported_amount_b"]
            )
            issue = "Reported amounts differ between Source A and Source B"

        else:
            status = "Exact Match"
            variance = 0
            issue = "None"

        results.append(
            {
                "record_id": record_id,
                "reconciliation_status": status,
                "variance": variance,
                "issue_description": issue,
            }
        )

    return pd.DataFrame(results)


def main():

    OUTPUT_DIR.mkdir(exist_ok=True)

    source_a, source_b = load_data()

    results = reconcile(source_a, source_b)

    results.to_csv(OUTPUT_FILE, index=False)

    print("\nReconciliation completed successfully.")
    print(f"Results saved to: {OUTPUT_FILE}")

    print("\nReconciliation Summary")
    print("----------------------")
    print(results["reconciliation_status"].value_counts())


if __name__ == "__main__":
    main()
