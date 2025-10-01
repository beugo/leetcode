def timeConversion(s):
    """
    Problem: Convert a 12-hour time format (with AM/PM) into a 24-hour format.

    Rules:
    - If the time ends with "AM":
        - "12AM" should be converted to "00".
        - Otherwise, keep the hour as-is.
    - If the time ends with "PM":
        - Add 12 to the hour (except for "12PM", which stays 12).
    - Return the resulting string in HH:MM:SS 24-hour format.

    Example:
    "07:05:45PM" → "19:05:45"
    "12:00:00AM" → "00:00:00"
    """

    if s[-2:] == "AM":
        if s[:2] == "12":
            return "00" + s[2:-2]
        else:
            return s[:-2]
    else:
        if s[:2] == "12":
            return s[:-2]
        new_hours = int(s[:2]) + 12
        return str(new_hours) + s[2:-2]
