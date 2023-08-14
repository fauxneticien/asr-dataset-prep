def ms_to_hms(start_ms: int) -> str:
    import math
    """
    Convert milliseconds to hours-minutes-seconds string format to use within identifiers

    e.g. 3990060 ms -> '01h06m30s060'
    """
    s, ms = divmod(start_ms, 1000)
    m, s  = divmod(s, 60)
    h, m  = divmod(m, 60)
    ms    = str(round(ms)).zfill(3)
    s     = str(math.floor(s)).zfill(2)
    m     = str(math.floor(m)).zfill(2)
    h     = str(math.floor(h)).zfill(2)

    return f"{h}h{m}m{s}s{ms}"
