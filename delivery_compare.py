import pandas as pd


def compare_delivery(yesterday_file, today_file):

    # .DAT files ko read karo
    yesterday = pd.read_csv(yesterday_file)

    today = pd.read_csv(today_file)

    # Delivery percentage wala column
    delivery_column = "% of Deliverable Quantity to Traded Quantity"

    # Sirf EQ stocks rakho
    yesterday = yesterday[yesterday["Series"] == "EQ"]
    today = today[today["Series"] == "EQ"]

    # Zaruri columns rakho
    yesterday = yesterday[
        ["Name of Security", delivery_column]
    ]

    today = today[
        ["Name of Security", delivery_column]
    ]

    # Column names change karo
    yesterday.columns = ["STOCK", "YESTERDAY"]
    today.columns = ["STOCK", "TODAY"]

    # Merge both files
    merged = pd.merge(
        yesterday,
        today,
        on="STOCK"
    )

    # Difference nikalo
    merged["DIFFERENCE"] = (
        merged["TODAY"] - merged["YESTERDAY"]
    )

    # Delivery % increase >= 5
    result = merged[
        merged["DIFFERENCE"] >= 5
    ]

    # Highest increase sabse upar
    result = result.sort_values(
        by="DIFFERENCE",
        ascending=False
    )

    return result
