import streamlit as st
import math
from modules.dataset import Dataset

def init_session():
    if 'page_number' not in st.session_state:
        st.session_state.page_number = 1

def move_to_page(page_number):
    st.session_state.page_number = page_number

def main():
    dataset = Dataset()
    init_session()

    page_per = 20
    last_page = math.ceil(len(dataset.movies) / page_per)
    start_idx = (st.session_state.page_number - 1) * page_per
    end_idx = st.session_state.page_number * page_per

    with st.container():
        first, prev, pages, next, last = st.columns([1, 1, 5, 1, 1], gap="large")
        first.button('First', key='top-first-page', on_click=move_to_page, args=(1, ), disabled=(st.session_state.page_number == 1))
        prev.button('Prev', key='top-prev-page', on_click=move_to_page, args=(st.session_state.page_number - 1, ), disabled=(st.session_state.page_number == 1))
        next.button('Next', key='top-next-page', on_click=move_to_page, args=(st.session_state.page_number + 1, ), disabled=(st.session_state.page_number == last_page))
        last.button('Last', key='top-last-page', on_click=move_to_page, args=(last_page, ), disabled=(st.session_state.page_number == last_page))

    with st.container():
        st.title('Movie List')
        st.table(dataset.movies.iloc[start_idx:end_idx])

    with st.container():
        first, prev, pages, next, last = st.columns([1, 1, 5, 1, 1], gap="large")
        first.button('First', key='bot-first-page', on_click=move_to_page, args=(1, ), disabled=(st.session_state.page_number == 1))
        prev.button('Prev', key='bot-prev-page', on_click=move_to_page, args=(st.session_state.page_number - 1, ), disabled=(st.session_state.page_number == 1))
        next.button('Next', key='bot-next-page', on_click=move_to_page, args=(st.session_state.page_number + 1, ), disabled=(st.session_state.page_number == last_page))
        last.button('Last', key='bot-last-page', on_click=move_to_page, args=(last_page, ), disabled=(st.session_state.page_number == last_page))

if __name__ == "__main__":
    main()
