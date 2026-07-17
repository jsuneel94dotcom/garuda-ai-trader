import requests

def get_positive_news():

    session = requests.Session()

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "application/json"
    }

    try:
        # Cookie generate karne ke liye
        session.get(
            "https://www.nseindia.com",
            headers=headers,
            timeout=10
        )

        # NSE announcements API
        response = session.get(
            "https://www.nseindia.com/api/corporate-announcements",
            headers=headers,
            timeout=10
        )

        if response.status_code != 200:
            return [{
                "stock": "ERROR",
                "news": f"Status Code: {response.status_code}",
                "impact": "LOW"
            }]

        data = response.json()

        keywords = [
            "order",
            "contract",
            "dividend",
            "bonus",
            "acquisition",
            "expansion",
            "approval",
            "wins",
            "received",
            "allotment"
        ]

        results = []

        for item in data:

            text = str(item.get("subject", "")).lower()

            if any(word in text for word in keywords):

                results.append({
                    "stock": item.get("symbol", "N/A"),
                    "news": item.get("subject", "N/A"),
                    "impact": "HIGH"
                })

            if len(results) >= 5:
                break

        if len(results) == 0:
            return [{
                "stock": "No Data",
                "news": "No positive announcements found.",
                "impact": "LOW"
            }]

        return results

    except Exception as e:

        return [{
            "stock": "ERROR",
            "news": str(e),
            "impact": "LOW"
        }]
