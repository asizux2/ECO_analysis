import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title('EDA with Streamlit & Plotly')

    # File upload functionality
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        # Display the DataFrame
        if st.checkbox('Show DataFrame'):
            st.write(df)

        # Select box for choosing column to visualize
        column_to_plot = st.selectbox('Select 1 column for visualization', df.columns)

        # Plotly Histogram
        if st.button('Show Histogram'):
            fig = px.histogram(df, x=column_to_plot)
            st.plotly_chart(fig)

        # Plotly Box Plot
        if st.button('Show Box Plot'):
            fig = px.box(df, y=column_to_plot)
            st.plotly_chart(fig)

        # If there are more than 1 numerical columns, enable scatter plot
        num_cols = df.select_dtypes(include=['float64', 'int64']).columns
        if len(num_cols) > 1:
            col1, col2 = st.selectbox('Select the first column:', num_cols), st.selectbox('Select the second column:', num_cols)
            if st.button('Show Scatter Plot'):
                fig = px.scatter(df, x=col1, y=col2)
                st.plotly_chart(fig)

        # More visualizations can be added here

if __name__ == "__main__":
    main()
