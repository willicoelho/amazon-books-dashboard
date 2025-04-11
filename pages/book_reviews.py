import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# Loading data
df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

# Sidebar: book selection with search
books = df_top100_books["book title"].unique()
book = st.sidebar.selectbox("📚 Type to search", books, index=0, placeholder="Search books...")

# Filtering book data and reviews
df_book = df_top100_books[df_top100_books["book title"] == book]
df_filtered_reviews = df_reviews[df_reviews["book name"] == book]

# Main book data
book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = df_book['book price'].iloc[0]
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

# Displaying book information
st.title(f"📖 {book_title}")
st.subheader(f"📂 Genre: *{book_genre}*")

col1, col2, col3 = st.columns(3)
col1.metric("💲 Price", f"${book_price}")
col2.metric("⭐ Rating", book_rating)
col3.metric("📅 Year", book_year)

st.divider()

# Reviews
st.subheader(f"📝 Reviews ({len(df_filtered_reviews)})")

if df_filtered_reviews.empty:
    st.info("This book has no reviews yet. 📭")
else:
    for _, row in df_filtered_reviews.iterrows():
        with st.expander(f"{row['reviewer rating']}⭐ *{row['review title']}* — {row['reviewer']}"):
            st.write(row["review description"])
