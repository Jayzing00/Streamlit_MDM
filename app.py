import streamlit as st
import pandas as pd

def load_data():
    df = pd.read_csv('netflix_titles.csv')
    return df

def main():
    st.title('Netflix Data Exploration')
    
    st.markdown("""
    This app performs simple visualization of the Netflix Titles dataset!
    """)

    data = load_data()

    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.write(data)

    option = st.radio(
        'Which attribute do you want to explore?',
        ('Category', 'Country', 'Release Year'))

    top_n = st.slider('How many top categories/countries/years do you want to display?', 1, 20, 10)

    if option == 'Category':
        st.subheader(f'Top {top_n} Categories')
        st.bar_chart(data['listed_in'].value_counts().head(top_n))
    elif option == 'Country':
        st.subheader(f'Top {top_n} Countries')
        st.bar_chart(data['country'].value_counts().head(top_n))
    else:
        st.subheader(f'Top {top_n} Release Years')
        st.bar_chart(data['release_year'].value_counts().head(top_n))

if __name__ == "__main__":
    main()
