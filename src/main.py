from src.io_utils import load_signal_csv
from src.signal_tools import sampling_frequency, moving_average
from src.analysis import basic_analysis
from src.plotting import plot_signals


def main():
    t, x = load_signal_csv("data/sample_signal.csv")

    fs = sampling_frequency(t)
    print(fs)

    mean, std, rms, min_val, max_val = basic_analysis(x)
    print(mean, std, rms, min_val, max_val)

    x_filtered = moving_average(x, window_size=5)

    plot_signals(
        t,
        x,
        x_filtered,
        "report/figures/time_signal.png"
    )


if __name__ == "__main__":
    main()
