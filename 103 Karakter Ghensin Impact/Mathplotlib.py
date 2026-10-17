import os
import pandas as pd
import matplotlib.pyplot as plt


DATA_PATH = "Genshin.csv"  
OUT_DIR = "hasil_grafik"
os.makedirs(OUT_DIR, exist_ok=True)

df = pd.read_csv(DATA_PATH).drop(columns=["Unnamed: 0"])
df["release_date"] = pd.to_datetime(df["release_date"])
df["release_year"] = df["release_date"].dt.year


x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.savefig(f"{OUT_DIR}/01_dasar.png")
plt.close()   



fig, ax = plt.subplots(figsize=(6, 4)) 

ax.plot(x, y, color="tab:blue", marker="o", linestyle="--", label="y = 2x")
ax.set_title("Grafik dasar dengan label")
ax.set_xlabel("Sumbu X")
ax.set_ylabel("Sumbu Y")
ax.legend()                                  
ax.grid(True)

fig.tight_layout()                          
fig.savefig(f"{OUT_DIR}/02_figure_axes.png", dpi=110)
plt.close(fig)



per_tahun = df["release_year"].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(per_tahun.index, per_tahun.values, marker="o")
ax.set_title("Jumlah karakter rilis per tahun")
ax.set_xlabel("Tahun")
ax.set_ylabel("Jumlah karakter")
fig.tight_layout()
fig.savefig(f"{OUT_DIR}/03_line_per_tahun.png", dpi=110)
plt.close(fig)

rata = df.groupby("element")["pulled_count"].mean().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(rata.index, rata.values, color="tab:orange")
ax.set_title("Rata-rata pulled_count per element")
ax.set_ylabel("Rata-rata pulled_count")
ax.tick_params(axis="x", rotation=45)
fig.tight_layout()
fig.savefig(f"{OUT_DIR}/04_bar_element.png", dpi=110)
plt.close(fig)


fig, ax = plt.subplots(figsize=(6, 4))
ax.hist(df["pulled_count"], bins=20, color="tab:green", edgecolor="white")
ax.axvline(df["pulled_count"].median(), color="red", linestyle="--", label="median")
ax.set_title("Distribusi pulled_count")
ax.set_xlabel("pulled_count")
ax.set_ylabel("Jumlah karakter")
ax.legend()
fig.tight_layout()
fig.savefig(f"{OUT_DIR}/05_histogram.png", dpi=110)
plt.close(fig)



fig, ax = plt.subplots(figsize=(7, 5))

for rarity, warna in [(4, "tab:purple"), (5, "tab:orange")]:
    bagian = df[df["rarity"] == rarity]
    ax.scatter(bagian["num_banners"], bagian["pulled_count"],
               color=warna, label=f"Bintang {rarity}", alpha=0.7)

ax.set_title("Jumlah banner vs pulled_count")
ax.set_xlabel("num_banners")
ax.set_ylabel("pulled_count")
ax.legend()
fig.tight_layout()
fig.savefig(f"{OUT_DIR}/06_scatter.png", dpi=110)
plt.close(fig)


fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0][0].plot(per_tahun.index, per_tahun.values, marker="o")
axes[0][0].set_title("Karakter per tahun")

axes[0][1].bar(rata.index, rata.values, color="tab:orange")
axes[0][1].set_title("Rata-rata pull per element")
axes[0][1].tick_params(axis="x", rotation=45)

axes[1][0].hist(df["pulled_count"], bins=20, color="tab:green", edgecolor="white")
axes[1][0].set_title("Distribusi pulled_count")

axes[1][1].scatter(df["num_banners"], df["pulled_count"], alpha=0.6)
axes[1][1].set_title("num_banners vs pulled_count")

fig.suptitle("Ringkasan dataset Genshin", fontsize=14)
fig.tight_layout()
fig.savefig(f"{OUT_DIR}/07_subplots.png", dpi=110)
plt.close(fig)

print("Selesai! Cek folder:", OUT_DIR)
