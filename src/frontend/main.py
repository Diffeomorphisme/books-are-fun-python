import streamlit as st

from request import get_all_books


st.title("Books are fun!")

books = get_all_books()
if books is None:
    st.text(
        "The service is not available at the moment. Try to refresh the page."
    )
else:
    st.dataframe(books)
