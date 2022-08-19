import streamlit as st
from streamlit_elements import elements, mui
import math
from modules.dataset import Dataset
from components.pagination import Pagination

def init_session():
    if 'page_number' not in st.session_state:
        st.session_state.page_number = 1

def move_to_page(event, page):
    st.session_state.page_number = page

def main():
    dataset = Dataset()
    init_session()

    page_per = 20
    last_page = math.ceil(len(dataset.movies) / page_per)
    start_idx = (st.session_state.page_number - 1) * page_per
    end_idx = st.session_state.page_number * page_per
    movies = dataset.movies.iloc[start_idx:end_idx]

    Pagination.pagination(key='movies-paginate-top',
        current_page=st.session_state.page_number,
        last_page=last_page, on_click=move_to_page)

    with elements('movides'):
        with mui.Grid(container=True, spacing=4):
            for index, row in movies.iterrows():
                with mui.Grid(item=True, xs=6):
                    with mui.Card:
                        mui.CardHeader(title=row['title'])
                        with mui.CardContent():
                            mui.Typography(row['genres'], variant='body2', color='text.secondary')

    Pagination.pagination(key='movies-paginate-bot',
        current_page=st.session_state.page_number,
        last_page=last_page, on_click=move_to_page)

if __name__ == "__main__":
    main()
