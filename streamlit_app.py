import streamlit as st
from main import parse_input, get_playlist_data

def main():
    if "res" not in st.session_state:
        st.session_state.res = []
    st.write("## YouTube Playlist Timer")
    msg = st.chat_input(placeholder="Enter a Playlist URL or ID")
    ids = [msg]
    if ids and parse_input(ids) is not None:
        ID = parse_input(ids)
        st.session_state.res.append(get_playlist_data(ID))
        add()

def add():
    print(st.session_state.res)
    for item in st.session_state.res:
        st.write(f"- {item}")

if __name__ == "__main__":
    main()

