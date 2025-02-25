import streamlit as st

from request import get_all_books

# A single page with a title and the books displayed in a table
st.title("Books are fun!")

books = get_all_books()
if books is None:
    # If the data cannot be fetched, display en error message
    st.text(
        "The service is not available at the moment. Try to refresh the page."
    )
else:
    st.dataframe(books)
