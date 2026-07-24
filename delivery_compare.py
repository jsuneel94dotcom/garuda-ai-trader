import pandas as pd


def compare_delivery():

    # .DAT file ko read karo
    yesterday = pd.read_csv("yesterday.dat")

    today = pd.read_csv("today.dat")

    # Column names ko short naam de dete hain
    delivery_column = "% of Deliverable Quantity to Traded Quantity"

    # Sirf EQ series wale stocks rakho
    yesterday = yesterday[yesterday["Series"] == "EQ"]
    today = today[today["Series"] == "EQ"]

    # Zaruri columns hi rakho
    yesterday = yesterday[
        ["Name of Security", delivery_column]
    ]

    today = today[
        ["Name of Security", delivery_column]
    ]

    # Column names badal do
    yesterday.columns = ["STOCK", "YESTERDAY"]

    today.columns = ["STOCK", "TODAY"]

    # Dono files ko STOCK ke basis par merge karo
    merged = pd.merge(
        yesterday,
        today,
        on="STOCK"
    )

    # Difference nikalo
    merged["DIFFERENCE"] = (
        merged["TODAY"] - merged["YESTERDAY"]
    )

    # Sirf wahi stocks chahiye
    # jinme delivery percentage 5% ya usse zyada badhi ho

    result = merged[
        merged["DIFFERENCE"] >= 5
    ]

    # Sabse jyada delivery increase wala stock upar aayega
    result = result.sort_values(
        by="DIFFERENCE",
        ascending=False
    )

    return result
