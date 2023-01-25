from datetime import datetime


def calculate_distance_fee(distance: int) -> int:
    """
    Calculates the distance fee based on received 'distance' (int).
    Args:
            distance (int): Delivery distance.

    Returns:
            (int): The distance fee.
    """
    BASE_FEE = 200
    THRESHOLD_DISTANCE = 500
    THRESHOLD_FEE = 100

    BASE_FEE = 200
    THRESHOLD_DISTANCE = 500
    THRESHOLD_FEE = 100

    if distance <= 1000:
        return BASE_FEE
    distance -= 1000
    multiplier = 1
    multiplier = distance // THRESHOLD_DISTANCE
    if distance % 500:
        multiplier += 1
    return int(THRESHOLD_FEE * multiplier + BASE_FEE)


def calculate_small_surcharge(cart_value: int) -> int:
    """
    Calculates a small surcharge fee for the received 'cart_value' (int).
    Args:
            cart_value (int): The total price of the cart.

    Returns:
            (int): Small surcharge fee.
    """
    BASE = 1000
    return BASE - cart_value


def calculate_item_count_fee(item_count: int) -> int:
    """
    Calculates a item count fee based on received 'item_count'.
    Args:
            item_count (int): Count of the items.

    Returns:
            (int): The item count fee.
    """
    BULK_FEE_THRESHOLD = 12
    BULK_FEE = 120
    EXTRA_FEE_THRESHOLD = 4
    FEE_PER_ITEM = 50

    fee = 0
    if item_count > BULK_FEE_THRESHOLD:
        fee += BULK_FEE
    return max(0, fee + ((item_count - EXTRA_FEE_THRESHOLD) * FEE_PER_ITEM))


def calculate_rush_hour_fee(time: str, current_fee: int) -> int:
    """
    Function checks that is received 'time' in rush hour zone,
    if it is function calculates rush hour fee.
    Args:
            time (str): time in ISO format.
            item_count (int): Current fee.

    Returns:
            If it is rush hour:
                    (int) current fee * RUSH_HOUR_MULTIPLIER
            else:
                            (int) current_fee
    """
    RUSH_HOUR_START = "15:00"
    RUSH_HOUR_END = "19:00"
    FRIDAY = 4
    RUSH_HOUR_MULTIPLIER = 1.2

    current = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
    if current.weekday() != FRIDAY:
        return (current_fee)
    start = datetime.strptime(RUSH_HOUR_START, "%H:%M")
    end = datetime.strptime(RUSH_HOUR_END, "%H:%M")
    if start.time() <= current.time() <= end.time():
        return (current_fee * RUSH_HOUR_MULTIPLIER)
    return (current_fee)
