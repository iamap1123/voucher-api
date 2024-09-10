def wrong_date_range(data):
    if "effective_date_from" in data and "effective_date_end" in data:
        if (
            data["effective_date_from"] is not None
            and data["effective_date_end"] is not None
            and data["effective_date_from"] > data["effective_date_end"]
        ):

            return True

    return False
