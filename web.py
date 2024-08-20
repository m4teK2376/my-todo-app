import streamlit as st
import functions


todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] +"\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My todo app")

count = 0

for todo in todos:
    checkbox = st.checkbox(todo, key=count)
    if checkbox:
        todos.pop(count)
        functions.write_todos(todos)
        del st.session_state[count]
        st.rerun()

    count += 1

st.text_input(label=" ", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
