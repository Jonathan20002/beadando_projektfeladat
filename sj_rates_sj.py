import requests
import re
from typing import Optional

NAPIARFOLYAM_URL_SJ = "https://www.napiarfolyam.hu/%C3%A1rfolyam/CIB+Bank/"

FALLBACK_RATES_SJ = {
    "EUR": 400.0,
    "USD": 370.0,
    "GBP": 460.0,
}


def _download_sj(url: str) -> str:
    resp = requests.get(url, timeout=5)
    resp.raise_for_status()
    return resp.text


def _parse_rate_from_napiarfolyam_html_sj(html: str, base: str) -> Optional[float]:
    base = base.upper()
    pattern_row = rf"{base}.*?(\d+,\d+|\d+\.\d+)"
    match = re.search(pattern_row, html, flags=re.DOTALL)
    if not match:
        return None

    raw_number = match.group(1)
    raw_number = raw_number.replace(",", ".")

    try:
        return float(raw_number)
    except ValueError:
        return None


def fetch_rate_to_huf_sj(base: str) -> float:
    base = base.upper()

    try:
        html = _download_sj(NAPIARFOLYAM_URL_SJ)
        rate = _parse_rate_from_napiarfolyam_html_sj(html, base)
    except Exception:
        rate = None

    if rate is None:
        rate = FALLBACK_RATES_SJ.get(base, 400.0)

    return rate


def convert_to_huf_sj(amount: float, base: str) -> float:
    rate = fetch_rate_to_huf_sj(base)
    return amount * rate
