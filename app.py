import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(layout="wide")
st.title("Top-100 Amazon Trending Books")

# Load data
df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")
df_books = df_top100_books

# Fill missing ratings with 0
df_books['rating'] = df_books['rating'].fillna(0)

# Sidebar filters
st.sidebar.header("Filters")

# Book title search filter
search = st.sidebar.text_input("Search by book title", "")
if search:
    df_books = df_books[df_books["book title"].str.contains(search, case=False, na=False)]

# Genre filter
genres = st.sidebar.multiselect("Genre", df_top100_books["genre"].unique())
if genres:
    df_books = df_books[df_books["genre"].isin(genres)]

# Price filter
min_price = df_top100_books["book price"].min()
max_price = df_top100_books["book price"].max()
price_filter = st.sidebar.slider("Price range 💲", min_price, max_price, max_price)
df_books = df_books[df_books["book price"] <= price_filter]

# Year filter
year_min = int(df_top100_books["year of publication"].min())
year_max = int(df_top100_books["year of publication"].max())
year_range = st.sidebar.slider("Year of publication 📅", year_min, year_max, (year_min, year_max))
df_books = df_books[df_books["year of publication"].between(year_range[0], year_range[1])]

# Rating filter
min_rating = float(df_top100_books["rating"].min())
max_rating = float(df_top100_books["rating"].max())
rating_filter = st.sidebar.slider("Minimum Rating ⭐", min_rating, max_rating, min_rating)
df_books = df_books[df_books["rating"] >= rating_filter]

# Display filtered data
st.write(f"### {len(df_books)} books found")

#Hide unnamed column
st.dataframe(df_books, hide_index=True)

# Create visualizations
# Books per year
fig = px.bar(df_books["year of publication"].value_counts().sort_index(),
             title="Books per Year", labels={"value": "Count", "index": "Year"})

# Price distribution
fig2 = px.histogram(df_books, x="book price", title="Book Pricing")

# Display first two charts side by side
col1, col2 = st.columns(2)
col1.plotly_chart(fig, use_container_width=True)
col2.plotly_chart(fig2, use_container_width=True)

# Rating distribution
fig3 = px.histogram(df_books, x="rating", nbins=20, title="Distribution of Ratings")
st.plotly_chart(fig3, use_container_width=True)

# Books by genre
genre_counts = df_books["genre"].value_counts().reset_index()
genre_counts.columns = ["genre", "count"]
fig4 = px.pie(genre_counts, values="count", names="genre", title="Books by Genre", hole=0.3)
st.plotly_chart(fig4)
