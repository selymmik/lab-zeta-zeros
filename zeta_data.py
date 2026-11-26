"""Data for the three plots in the Zeta Zeros lab."""
import csv
from pathlib import Path

from mpmath import zeta, zetazero


def sample_zeta(count=3, stop=30):
    """Return zero heights and ordered outputs, including the known crossings."""
    heights = [float(zetazero(n).imag) for n in range(1, count + 1)]
    samples = {i / 20 for i in range(stop * 20 + 1)}
    samples.update(height for height in heights if height <= stop)
    values = [complex(zeta(0.5 + t * 1j)) for t in sorted(samples)]
    return heights, values


def prime_counts():
    """Return the integers from 1 to 20 and the prime count at each one."""
    primes = {2, 3, 5, 7, 11, 13, 17, 19}
    numbers = list(range(1, 21))
    counts = []
    total = 0
    for number in numbers:
        if number in primes:
            total += 1
        counts.append(total)
    return numbers, counts


def prime_estimates():
    """Return x and a dictionary of four curves computed from zeta zeros."""
    x = []
    estimates = {4: [], 16: [], 64: [], 256: []}
    with Path(__file__).with_name("prime_estimates.csv").open() as file:
        for row in csv.DictReader(file):
            x.append(float(row["x"]))
            for n in estimates:
                estimates[n].append(float(row[str(n)]))
    return x, estimates
