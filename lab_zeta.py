"""Make three figures about primes and the Riemann zeta function."""
import matplotlib.pyplot as plt

ESTIMATE_COLORS = {4: "#0072b2", 16: "#cb5012", 64: "#007a59", 256: "#875097"}


def plot_prime_count(ax, numbers, counts):
    """Draw the running count, with a jump at each prime."""
    pass


def plot_outputs(ax, values):
    """Trace the complex outputs in order and mark the origin."""
    pass


def plot_inputs(ax, heights):
    """Mark the inputs that send the curve through the origin."""
    pass


def plot_estimates(axes, numbers, counts, x, estimates):
    """Compare the staircase with one estimate per panel."""
    pass


def draw_estimate(ax, x, y, n):
    """Draw an estimate in its legend color. Supplied with the starter."""
    ax.plot(x, y, color=ESTIMATE_COLORS[n], linestyle="--", label=f"{n} zeros")


def add_shared_legend(fig, axes):
    """Collect each labeled line once for the key below the four panels."""
    entries = {}
    for ax in axes:
        lines, labels = ax.get_legend_handles_labels()
        entries.update(zip(labels, lines))
    if entries:
        fig.legend(entries.values(), entries.keys(), loc="lower center", ncol=5, frameon=False)


def main():
    from zeta_data import prime_counts, prime_estimates, sample_zeta

    numbers, counts = prime_counts()
    fig, ax = plt.subplots(figsize=(7, 3), layout="constrained")
    plot_prime_count(ax, numbers, counts)
    ax.set_xticks([1, 2, 3, 5, 7, 11, 13, 17, 19])
    fig.savefig("prime-steps.png", dpi=160)
    plt.close(fig)

    heights, values = sample_zeta()
    fig, (left, right) = plt.subplots(1, 2, figsize=(8, 3.7), layout="constrained")
    plot_outputs(left, values)
    plot_inputs(right, heights)
    right.set(xlim=(0, 1), ylim=(0, 30), xticks=[0, 0.5, 1])
    fig.savefig("zeta.png", dpi=160)
    plt.close(fig)

    x, estimates = prime_estimates()
    fig, axes = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(8, 5.9))
    plot_estimates(axes.flat, numbers, counts, x, estimates)
    axes[0, 0].set_xticks([2, 5, 7, 11, 13, 17, 19])
    add_shared_legend(fig, axes.flat)
    fig.tight_layout(rect=(0, 0.07, 1, 1))
    fig.savefig("prime-estimates.png", dpi=160)
    plt.close(fig)


if __name__ == "__main__":
    main()
