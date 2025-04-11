# Amazon Books Dashboard

A Streamlit dashboard for exploring and analyzing Amazon's Top-100 Trending Books dataset. This interactive application allows users to filter books by various criteria and visualize trends in book publishing, pricing, and ratings.

## Features

- **Interactive Filters**: Filter books by title, genre, price range, publication year, and rating
- **Data Visualization**: 
  - Books published per year
  - Price distribution
  - Rating distribution
  - Books by genre (pie chart)
- **Responsive Layout**: Wide layout optimized for better visualization

## Screenshots

(Screenshots will be added here)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/amazon-books-dashboard.git
   cd amazon-books-dashboard
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Use the sidebar filters to explore the book data:
   - Search for books by title
   - Filter by genre
   - Adjust price range
   - Select publication year range
   - Set minimum rating

## Project Structure

- `app.py`: Main application file
- `pages/book_reviews.py`: Book reviews page
- `datasets/`: Directory containing the CSV data files
  - `customer reviews.csv`: Customer review data
  - `Top-100 Trending Books.csv`: Book information data

## Dependencies

- streamlit
- pandas
- plotly.express

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgements

- Data sourced from Amazon's Top-100 Trending Books
- Built with Streamlit 