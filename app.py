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


# Main ###############################

st.title("Idenity Project")
st.caption("Made with 💖 by Ryan Zhang")

# Tree map
render_disk_usage()
st.caption("Please use mouse to interact with the treemap")
# # Tree
render_basic_tree()
st.caption("Please click on branch node to interact")



# Writings

st.header("Why these categories?")
st.markdown("""
    I chose these categories because these are the components that makeup me. 
    First, under the superset of Ryan holds the subset Human. The human subset consists of half of my attributes. It is the parent of the children clueless, dumb, lost, idiot. 
    Then, we have the other two subsets, work, and home. These two duos unbalance all our lives and internally fights each other for our attention. I decided to attempt to master these two areas of interest after a midlife crisis. I think it would be best for me to do well in these two areas so I can live a peaceful life and then die.
""")

st.header("What comparisons can you make between the number system classifications and the classifications you came up with for yourself?")
st.markdown("""
    Just like the number system, I classify myself into sets. These sets are infinitely long and infinitely complex. I only showed my favorite numbers just like how I selectively choose what attributes I show you. There is no way for you to see all my other numbers. Numbers like π gets classified into irrational without much thought. Yet, π is so crucial to the essence of the circle and even the world. Even though these attributes are classified we learn nothing about them except they belong somewhere.
""")

st.header("What are the benefits / drawbacks of classification?")
st.markdown("""
    The benefit of classification is our retreat to our comfortable communities. We get to associate ourselves with a group of humans and tell ourselves, "we are part of that." Yet, sometimes humans can not even classify themselves internally. Sometimes we cannot classify our emotions, we cannot classify our experiences, we can not classify our mistakes. The drawbacks start to surface when we randomly classify ourselves and other people. One day I am hardworking, and the next day I am a procrastinator. If I can classify myself I would lock myself in hardworking. Too bad you can't. 
""")


st.header("After completing this project, did you come across any types of personal classifications (or intersection of categories) that surprised you?")
st.markdown("""
    No, nothing surprised me in my classifications. However, I hope this visual map may serve as a guiding light for me in the future. I constantly wonder what I might become in the future and I only wish I become much smarter than I am now. Perhaps one day I will not be clueless. 
""")






