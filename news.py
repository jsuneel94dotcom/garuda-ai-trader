import requests

def get_positive_news():

    url = "https://www.nseindia.com/api/corporate-announcements"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            data = response.json()

            results = []

            keywords = [
                "order",
                "contract",
                "dividend",
                "bonus",
                "acquisition",
                "capacity",
                "fund"
            ]

            for item in data[:50]:

                subject = item.get("subject", "")

                if any(k.lower() in subject.lower() for k in keywords):

                    results.append(
                        {
                            "stock": item.get("symbol", "N/A"),
                            "news": subject,
                            "impact": "HIGH"
                        }
                    )

            return results[:10]

    except Exception as e:
        print(e)

    return [
        {
            "stock": "No Data",
            "news": "Unable to fetch NSE announcements.",
            "impact": "LOW"
        }
    ]
