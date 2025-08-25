import streamlit as st
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="postgres",
    user="postgres",
    password="123Oshiro456"
    )

cur = conn.cursor()

# Execute a SELECT query to retrieve data from the users table
cur.execute("SELECT * FROM users where name = 'Fernando'")

# Fetch the results of the query
results = cur.fetchall()
st.write(results)

# Close the cursor and connection
cur.close()
conn.close()

def main():
    # Set the title of your web app
    st.title('Login Page')

    # Create a form with username and password fields
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    login_button = st.button('Login')

    if login_button:
        # Execute a SELECT query to retrieve data from the users table
        cur.execute("SELECT * FROM users where name = {username}")
        st.write(results)
        




if __name__ == '__main__':
    main()