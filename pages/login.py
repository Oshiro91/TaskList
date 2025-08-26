import streamlit as st
import psycopg2

if 'logged_user' not in st.session_state:
    st.session_state.logged_user = None

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="postgres",
    user="postgres",
    password="123Oshiro456"
    )

cur = conn.cursor()
st.write(st.session_state.logged_user)

# Execute a SELECT query to retrieve data from the users table
cur.execute("SELECT * FROM users")

# Fetch the results of the query
results = cur.fetchall()
st.write(results)

# # Close the cursor and connection
# cur.close()
# conn.close()

def login_page():
    """Login page with styled inputs"""
    st.markdown("# 🔐 Login")
    
    # Center the login form
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        with st.container():
            # User input field
            username = st.text_input(
                "👤 Usuário",
                placeholder="Digite o usuário",
                key="username_input"
            )
            
            # Password input field  
            password = st.text_input(
                "🔒 Senha", 
                type="password",
                placeholder="Digite a senha",
                key="password_input"
            )

            # Login button
            if st.button("Acessar", use_container_width=True):
                st.write(f"SELECT * FROM users where name = '{username}'")
                try:
                    cur = conn.cursor()
                    cur.execute(f"SELECT * FROM users where name = '{username}'")
                    results = cur.fetchone()
                    st.write(results)
                    if results and results[2] == password:
                        st.success("Login bem-sucedido!", icon="✅")
                        st.session_state.logged_user = results[1]
                        st.rerun()
                    else:
                        st.error("Usuário ou senha inválidos. Tente novamente.", icon="🚫")
                except Exception as e:
                    results = None
                    st.error("Usuário ou senha inválidos. Tente novamente.", icon="🚫")
def main():
    """Main app controller"""
    # Check if user is already logged in and redirect
    if st.session_state.logged_user is not None:
        st.switch_page("pages/second_page.py")  # Replace with your target page
    else:
        login_page()        


if __name__ == '__main__':
    main()