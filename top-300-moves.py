from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.axes import Axes
from matplotlib.figure import Figure


MOVIE_COLUMNS = ["电影名", "年份", "上映时间", "类型", "语言", "评分"]


def load_movie_data(csv_path: str | Path) -> pd.DataFrame:
    """Load the movie fields used by the analysis and fill missing years."""
    data = pd.read_csv(
        csv_path,
        usecols=MOVIE_COLUMNS,
        dtype={"年份": "string"},
    )
    release_year = pd.to_numeric(
        data["上映时间"].astype("string").str.extract(r"^(\d{4})", expand=False),
        errors="coerce",
    )
    data["年份"] = pd.to_numeric(data["年份"], errors="coerce").fillna(release_year)
    data["年份"] = data["年份"].astype("Int64")
    return data


def _count_categories(values: pd.Series) -> pd.Series:
    categories = values.dropna().astype(str).str.split(",").explode().str.strip()
    categories = categories[categories.ne("")]
    return categories.value_counts()


def _plot_movie_years(ax: Axes, data: pd.DataFrame) -> None:
    year_counts = data["年份"].dropna().value_counts().sort_index()
    if year_counts.empty:
        ax.set_title("每年上映电影数量变化")
        ax.text(0.5, 0.5, "没有可用的年份数据", ha="center", va="center")
        return

    years = range(int(year_counts.index.min()), int(year_counts.index.max()) + 1)
    counts = [int(year_counts.get(year, 0)) for year in years]
    ax.plot(list(years), counts, color="green")
    ax.set_xlabel("年份", fontsize=10)
    ax.set_ylabel("电影数量", fontsize=10)
    ax.set_title("每年上映电影数量变化", fontsize=15)
    ax.set_xticks(list(years)[::8])
    ax.set_yticks(range(0, max(counts) + 1, 5))
    ax.grid(linestyle="--", linewidth=0.5)


def _plot_category_counts(ax: Axes, counts: pd.Series, label: str, title: str) -> None:
    ax.bar(counts.index.tolist(), counts.values.tolist(), color="green", width=0.5)
    ax.set_xlabel(label, fontsize=10)
    ax.set_ylabel("电影数量", fontsize=10)
    ax.set_title(title, fontsize=15)
    ax.grid(axis="y", linestyle="--", linewidth=0.5)
    ax.tick_params(axis="x", rotation=45)


def _plot_rating_distribution(ax: Axes, data: pd.DataFrame) -> None:
    rating_counts = data["评分"].dropna().value_counts().sort_index()
    if rating_counts.empty:
        ax.set_title("不同电影评分的比例")
        ax.text(0.5, 0.5, "没有可用的评分数据", ha="center", va="center")
        return

    total = rating_counts.sum()
    large_ratings = rating_counts[rating_counts / total >= 0.02].copy()
    small_rating_total = rating_counts[rating_counts / total < 0.02].sum()
    if small_rating_total:
        large_ratings.loc["其他"] = small_rating_total

    ax.pie(
        large_ratings.values.tolist(),
        labels=large_ratings.index.tolist(),
        autopct="%1.1f%%",
        startangle=0,
        radius=1,
    )
    ax.set_title("不同电影评分的比例", fontsize=15)
    ax.legend(loc="lower center", ncol=4, bbox_to_anchor=(0.5, -0.3))


def plot_movie_analysis(data: pd.DataFrame) -> tuple[Figure, np.ndarray]:
    """Build the four charts for year, language, genre, and rating analysis."""
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    figure, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 12), dpi=100)
    figure.suptitle("TMDB TOP 300 电影数据分析", fontsize=15, x=0.5, y=0.95)
    figure.subplots_adjust(hspace=0.7, wspace=0.2)

    _plot_movie_years(axes[0, 0], data)
    _plot_category_counts(
        axes[0, 1],
        data["语言"].dropna().value_counts(),
        "语言",
        "不同语言的电影数量对比",
    )
    _plot_category_counts(
        axes[1, 0],
        _count_categories(data["类型"]),
        "类型",
        "不同类型的电影数量对比",
    )
    _plot_rating_distribution(axes[1, 1], data)
    return figure, axes


def main() -> None:
    csv_path = Path(__file__).resolve().parent / "data" / "movies.csv"
    data = load_movie_data(csv_path)
    plot_movie_analysis(data)
    plt.show()


if __name__ == "__main__":
    main()
