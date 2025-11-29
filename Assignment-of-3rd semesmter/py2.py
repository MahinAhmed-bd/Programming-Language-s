import ipywidgets as widgets
from IPython.display import display
import pandas as pd
data=pd.DataFrame(columns=["Name","Age"])
def save(b):
    name=name_input.value
    age=age_input.value
    if name and age:
        data.loc[len(data)]=[name,age]
        print("Data added successfully.")
def search(b):
    name=name_input.value
    if name:
        result=data[data["name"]==name]
        if not result.empty:
            print("Search results.")
            print(result)
        else:
            print("No matching data found.")
name_input=widgets.Text(description="Name:")
age_input=widgets.Text(description="Age:")
save_Button=widgets.Button(description="save")
search_Button=widgets.Button(description="Search")
save_Button.on_click(save)
search_Button.on_click(search)
display(name_input)
display(age_input)
display(save_Button)
display(search_Button)
