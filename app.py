import json

import streamlit as st
from streamlit_echarts import JsCode, st_echarts


def render_disk_usage():
    """Tree Map"""
    with open("./me.tree.json", "r") as f:
        diskData = json.loads(f.read())

    option = {
        "title": {"text": "Identity Project", "left": "center"},
        "tooltip": {
            "formatter": JsCode(
                "function(info){var value=info.value;var treePathInfo=info.treePathInfo;var treePath=[];for(var i=1;i<treePathInfo.length;i+=1){treePath.push(treePathInfo[i].name)}return['<div class=\"tooltip-title\">'+treePath.join('/')+'</div>','Percentage: '+ value +' %'].join('')};"
            ).js_code,
        },
        "series": [
            {
                "name": "Identity Project",
                "type": "treemap",
                "visibleMin": 300,
                "label": {"show": True, "formatter": "{b}"},
                "itemStyle": {"borderColor": "#fff"},
                "levels": [
                    {"itemStyle": {"borderWidth": 0, "gapWidth": 5}},
                    {"itemStyle": {"gapWidth": 1}},
                    {
                        "colorSaturation": [0.35, 0.5],
                        "itemStyle": {"gapWidth": 1, "borderColorSaturation": 0.6},
                    },
                ],
                "data": diskData,
            }
        ],
    }
    st_echarts(option, height="500px")


def render_basic_tree():
    """Basic Tree diagram"""
    with open("./flare.json", "r") as f:
        data = json.loads(f.read())

    for idx, _ in enumerate(data["children"]):
        data["children"][idx]["collapsed"] = idx % 2 == 0

    option = {
        "tooltip": {"trigger": "item", "triggerOn": "mousemove"},
        "series": [
            {
                "type": "tree",
                "data": [data],
                "top": "1%",
                "left": "7%",
                "bottom": "1%",
                "right": "20%",
                "symbolSize": 7,
                "label": {
                    "position": "left",
                    "verticalAlign": "middle",
                    "align": "right",
                    "fontSize": 9,
                },
                "leaves": {
                    "label": {
                        "position": "right",
                        "verticalAlign": "middle",
                        "align": "left",
                    }
                },
                "emphasis": {"focus": "descendant"},
                "expandAndCollapse": True,
                "animationDuration": 550,
                "animationDurationUpdate": 750,
            }
        ],
    }
    st_echarts(option, height="500px")




# Tree map
render_disk_usage()

st.title("Idenity Project")

st.header("Why these categories?")
st.markdown("""
    I chose these categories because I wanted to capture myself in the most simplistic way possible.
    
    The umbrella that holds eve


""")

st.header("What comparisons can you make between the number system classifications and the classifications you came up with for yourself?")
st.markdown("""

    I believe humans are extrememly complex and complicated. There is no way to classify a human being into catergories like numbers. Numbers
    do not change their properties. You can not just simply turn a irrational number into a rational number. However, you can train and through
    experience, change yourself from irrational to rational. Maybe, it is a little bit like doing operatons on a number in order to change it
    into something else. Perhaps an irrational number can turn into a rational number by doing some addition, subtraction, or division on it or
    something. Any ways, I digress. Basically to sum things up just like the number classification system there are catergories that are subsets
    of each superset. Each set belongs into its own place in me.

""")

st.header("What are the benefits / drawbacks of classification?")
st.markdown("""

    In terms of classifying humas the benefits for classification is that you are able to visualize things in their perseived catergories. 

""")


st.header("After completing this project, did you come across any types of personal classifications (or intersection of categories) that surprised you?")
st.markdown("""
    No, I was not surprised by these catergories as I catergorized myself. There are no elements of surprises there. However, I do believe I
    somewhat learned more about myself by visualizing what I believe in myself. I am a boring person so there is not much to learn, but I is nice
    to see everything from a big picture standpoint. I think we go through life all clueless and maybe as I grow older I will become more and more
    dumb. Thus, potentially I might need to use this chart as a guide for myself when I become old. I really do hope my older self is much smarter
    than what I am now.

""")


# # Tree
# render_basic_tree()




