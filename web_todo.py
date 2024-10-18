import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo ='\n' +  st.session_state['new_todo']
    print(todo)
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my Web Todo Application")
st.write("This app is to increase your productivity and give you control over your schedules")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo", placeholder="Add a new todo",
              on_change=add_todo, key='new_todo')


st.session_state