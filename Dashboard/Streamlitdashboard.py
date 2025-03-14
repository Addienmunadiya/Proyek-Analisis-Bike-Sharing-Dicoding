import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

st.title("Bike Sharing Dataset Analysis🚴")
st.text("Addien Munadiya Yunadiya")

# Loading data dan persiapan
@st.cache_data
def load_data():
    day_df = pd.read_csv("day.csv")
    hr_df = pd.read_csv("hour.csv")
    datetime_columns = ["dteday"]
    for column in datetime_columns:
        day_df[column] = pd.to_datetime(day_df[column])
        hr_df[column] = pd.to_datetime(hr_df[column])

    main_df = hr_df.copy()

    mapping_yr = {0: '2011', 1: '2012'}
    mapping_mnth = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
                    7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    mapping_season = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
    mapping_weathersit = {1: 'Clear', 2: 'Cloudy', 3: 'Light Snow/Rain', 4: 'Heavy Rain/Ice Pallets'}

    main_df['yr'] = main_df['yr'].map(mapping_yr)
    main_df['mnth'] = main_df['mnth'].map(mapping_mnth)
    main_df['weekday'] = main_df['dteday'].dt.day_name()
    main_df['season'] = main_df['season'].map(mapping_season)
    main_df['weathersit'] = main_df['weathersit'].map(mapping_weathersit)
    main_df = main_df[['dteday', 'yr', 'mnth', 'hr', 'weekday', 'season', 'weathersit','cnt', 'registered', 'casual']]

    return main_df

# Plotting functions 
def plot_rentals(monthly_rentals):
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(monthly_rentals['date'], monthly_rentals['cnt'], marker='o', color='green', linewidth=2, markersize=6, label='Total Rentals (cnt)')
    ax.plot(monthly_rentals['date'], monthly_rentals['cnt'].rolling(window=3).mean(), linestyle='--', color='skyblue', label='Trend Line')
    ax.set_title('Grafik Peminjaman Sepeda Selama Dua Tahun (2011-2012)', fontsize=16, fontweight='bold')
    ax.set_xlabel('Date', fontsize=14)
    ax.set_ylabel('Number of Rentals', fontsize=14)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend(fontsize=12)
    ax.set_facecolor('whitesmoke')
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.tight_layout()
    st.pyplot(fig)
    st.caption("Tren peminjaman sepeda antara 2011 dan 2012 menunjukkan fluktuasi yang signifikan. Tahun 2011 dimulai dengan kenaikan tajam pada kuartal pertama dan kedua, diikuti penurunan berkelanjutan di kuartal ketiga dan keempat. Sementara itu, 2012 melihat lonjakan besar di akhir kuartal pertama dan berlanjut hingga kuartal ketiga, sebelum penurunan di kuartal keempat. Secara keseluruhan, meski ada fluktuasi, peminjaman sepeda menunjukkan peningkatan yang lebih positif pada 2012.")

def plot_seasonal_rentals(seasonal_counts):
    fig, ax = plt.subplots(figsize=(12, 7))
    bars = ax.bar(seasonal_counts.index, seasonal_counts.values, color=['blue', 'orange', 'red', 'grey'], edgecolor='black', linewidth=1.5)
    ax.set_xlabel('Musim', fontsize=14, fontweight='bold', color='darkslategray')
    ax.set_ylabel('Jumlah Peminjaman', fontsize=14, fontweight='bold', color='darkslategray')
    ax.set_title('Jumlah Peminjaman Sepeda Berdasarkan Musim', fontsize=16, fontweight='bold', color='darkred')

    for i, value in enumerate(seasonal_counts.values):
        ax.text(i, value + 500, str(value), ha='center', va='bottom', fontsize=12, 
                color='black', fontweight='bold', 
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))
    ax.grid(True, linestyle='--', alpha=0.4)
    ax.set_facecolor('lightblue')
    plt.xticks(rotation=45, ha='right', fontsize=12, color='darkslategray')
    plt.tight_layout()
    st.pyplot(fig)
    st.caption ("Grafik di atas menunjukan hasil bahwa musim gugur (fall) dan musim panas (summer) memiliki jumlah peminjam sepeda tertinggi (puncak).")

def plot_weather_rentals(weather_counts):
    fig, ax = plt.subplots(figsize=(12, 7))
    bars = ax.bar(weather_counts.index, weather_counts.values, color=['gold', 'lightskyblue', 'grey', 'darkblue'], edgecolor='black', linewidth=1.5)
    ax.set_xlabel('Cuaca', fontsize=14, fontweight='bold', color='darkslategray')
    ax.set_ylabel('Jumlah Peminjaman', fontsize=14, fontweight='bold', color='darkslategray')
    ax.set_title('Jumlah Peminjaman Sepeda Berdasarkan Cuaca', fontsize=16, fontweight='bold', color='darkred')

    for i, value in enumerate(weather_counts.values):
        ax.text(i, value + 500, str(value), ha='center', va='bottom', fontsize=12, 
                color='black', fontweight='bold', 
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))
    ax.grid(True, linestyle='--', alpha=0.4)
    ax.set_facecolor('lightblue')
    plt.xticks(rotation=45, ha='right', fontsize=12, color='darkslategray')
    plt.tight_layout()
    st.pyplot(fig)
    st.caption ("Grafik di atas menunjukan hasil bahwa cuaca cerah (clear) dan berawan memiliki jumlah peminjam sepeda tertinggi (puncak) terutama pada saat cerah.")

def plot_hourly_rentals(hourly_counts):
    fig, ax = plt.subplots(figsize=(12, 7))
    bars = ax.bar(hourly_counts.index, hourly_counts.values, color='mediumseagreen', edgecolor='black', linewidth=1.5)
    ax.set_title('Total Peminjaman Sepeda Berdasarkan Jam dalam Sehari', fontsize=16, fontweight='bold', color='darkred')
    ax.set_xlabel('Jam', fontsize=14, fontweight='bold', color='darkslategray')
    ax.set_ylabel('Jumlah Peminjaman', fontsize=14, fontweight='bold', color='darkslategray')

    for i, value in enumerate(hourly_counts.values):
        ax.text(i, value + 500, str(value), ha='center', va='bottom', fontsize=12, 
                color='black', fontweight='bold', 
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))
    ax.grid(axis='y', linestyle='--', alpha=0.4)
    ax.set_facecolor('lightblue')
    plt.xticks(rotation=0, fontsize=12, color='darkslategray')
    plt.tight_layout()
    st.pyplot(fig)
    st.caption ("Berdasarkan grafik di atas, dapat dianalisis bahwa pada pukul 5 sore dan 6 sore, terjadi lonjakan signifikan dalam jumlah peminjaman sepeda, dengan masing-masing melebihi 300.000 peminjam. Puncak peminjaman pada jam-jam ini menunjukkan adanya peningkatan permintaan yang tinggi pada periode sore hari, kemungkinan terkait dengan aktivitas harian seperti pulang kerja atau aktivitas luar ruangan lainnya yang memicu kebutuhan transportasi sepeda.")

def plot_heatmap(clustering):
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(clustering, cmap="coolwarm", annot=False, linewidths=0.5, linecolor='black')
    ax.set_title('Heatmap Peminjaman Sepeda Berdasarkan Hari dan Jam', fontsize=16, fontweight='bold', color='darkred')
    ax.set_xlabel('Jam dalam Sehari', fontsize=14, fontweight='bold', color='darkslategray')
    ax.set_ylabel('Hari dalam Seminggu', fontsize=14, fontweight='bold', color='darkslategray')
    plt.tight_layout()
    st.pyplot(fig)
    st.caption("Berdasarkan hasil **clustering** yang ditampilkan pada heatmap, dapat disimpulkan bahwa tren peminjaman sepeda menunjukkan peningkatan signifikan pada pukul 8 pagi, 5 sore, dan 6 sore di hari Senin hingga Jumat. Sementara itu, pada hari Sabtu dan Minggu, peminjaman sepeda cenderung meningkat pada siang hari, antara pukul 12 siang hingga 3 sore. Dalam analisis ini, clustering digunakan untuk mengelompokkan data berdasarkan dua fitur utama, yaitu 'hr' (jam) dan 'weekday' (hari dalam seminggu), yang kemudian dihitung total peminjaman ('cnt') untuk setiap kombinasi hari dan jam. Tujuan dari metode ini adalah untuk mengidentifikasi pola dan tren dalam data peminjaman sepeda, yang divisualisasikan dalam bentuk heatmap untuk memberikan gambaran yang lebih jelas tentang perilaku peminjam sepanjang minggu.")

# Streamlit Dashboard
def main():
    st.subheader("Dashboard Peminjaman Sepeda 2011-2012")
    st.sidebar.header("Visualisasi Data")

    # Data Loading
    main_df = load_data()
    monthly_rentals = main_df.groupby(['yr', 'mnth'])[['cnt', 'registered', 'casual']].sum().reset_index()
    monthly_rentals['date'] = monthly_rentals['yr'] + '-' + monthly_rentals['mnth']
    monthly_rentals['date'] = pd.to_datetime(monthly_rentals['date'], format='%Y-%B')
    monthly_rentals = monthly_rentals.sort_values('date')

    seasonal_counts = main_df.groupby('season').cnt.sum().sort_values(ascending=False)
    weather_counts = main_df.groupby('weathersit').cnt.sum().sort_values(ascending=False)
    hourly_counts = main_df.groupby('hr')['cnt'].sum()

    # Opsi Sidebar
    option = st.sidebar.selectbox("Pilih Visualisasi", 
                                  ["Monthly Rentals", "Seasonal Rentals", "Weather Rentals", "Hourly Rentals", "Heatmap"])

    # Filter Berdasarkan Tanggal untuk Monthly Rentals
    if option == "Monthly Rentals":
        # Pilih rentang tanggal dengan slider
        min_date = main_df['dteday'].min().date()  # Mengonversi menjadi datetime.date
        max_date = main_df['dteday'].max().date()  # Mengonversi menjadi datetime.date
        
        selected_dates = st.sidebar.slider(
            "Pilih Rentang Tanggal", 
            min_value=min_date, 
            max_value=max_date, 
            value=(min_date, max_date),
            format="YYYY-MM-DD"
        )
        
        # Filter data berdasarkan rentang tanggal yang dipilih
        main_df_filtered = main_df[(main_df['dteday'].dt.date >= selected_dates[0]) & (main_df['dteday'].dt.date <= selected_dates[1])]
        monthly_rentals_filtered = main_df_filtered.groupby(['yr', 'mnth'])[['cnt', 'registered', 'casual']].sum().reset_index()
        monthly_rentals_filtered['date'] = monthly_rentals_filtered['yr'] + '-' + monthly_rentals_filtered['mnth']
        monthly_rentals_filtered['date'] = pd.to_datetime(monthly_rentals_filtered['date'], format='%Y-%B')
        monthly_rentals_filtered = monthly_rentals_filtered.sort_values('date')
    
    # Filter Musim dan Cuaca untuk Seasonal Rentals
    elif option == "Seasonal Rentals":
        selected_season = st.sidebar.selectbox("Pilih Musim", ['All'] + list(main_df['season'].unique()))
        selected_weather = st.sidebar.selectbox("Pilih Cuaca", ['All'] + list(main_df['weathersit'].unique()))
        if selected_season != 'All':
            main_df = main_df[main_df['season'] == selected_season]
        if selected_weather != 'All':
            main_df = main_df[main_df['weathersit'] == selected_weather]
    
    # Filter Musim dan Cuaca untuk Weather Rentals
    elif option == "Weather Rentals":
        selected_season = st.sidebar.selectbox("Pilih Musim", ['All'] + list(main_df['season'].unique()))
        selected_weather = st.sidebar.selectbox("Pilih Cuaca", ['All'] + list(main_df['weathersit'].unique()))
        if selected_season != 'All':
            main_df = main_df[main_df['season'] == selected_season]
        if selected_weather != 'All':
            main_df = main_df[main_df['weathersit'] == selected_weather]

    # Filter Jam untuk Hourly Rentals
    elif option == "Hourly Rentals":
        selected_hour = st.sidebar.slider("Pilih Jam", 0, 23, (0, 23))
        main_df = main_df[(main_df['hr'] >= selected_hour[0]) & (main_df['hr'] <= selected_hour[1])]

    # Filter Hari dan Jam untuk Heatmap
    elif option == "Heatmap":
        selected_day = st.sidebar.selectbox("Pilih Hari", ['All'] + list(main_df['weekday'].unique()))
        selected_hour = st.sidebar.slider("Pilih Jam", 0, 23, (0, 23))
        if selected_day != 'All':
            main_df = main_df[main_df['weekday'] == selected_day]
        main_df = main_df[(main_df['hr'] >= selected_hour[0]) & (main_df['hr'] <= selected_hour[1])]

    # Visualisasi berdasarkan pilihan
    if option == "Monthly Rentals":
        plot_rentals(monthly_rentals_filtered)
    elif option == "Seasonal Rentals":
        seasonal_counts = main_df.groupby('season').cnt.sum().sort_values(ascending=False)
        plot_seasonal_rentals(seasonal_counts)
    elif option == "Weather Rentals":
        weather_counts = main_df.groupby('weathersit').cnt.sum().sort_values(ascending=False)
        plot_weather_rentals(weather_counts)
    elif option == "Hourly Rentals":
        hourly_counts = main_df.groupby('hr')['cnt'].sum()
        plot_hourly_rentals(hourly_counts)
    elif option == "Heatmap":
        clustering = main_df.groupby(['weekday', 'hr'])['cnt'].sum().unstack()
        plot_heatmap(clustering)

if __name__ == "__main__":
    main()
