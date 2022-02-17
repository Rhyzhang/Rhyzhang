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

st.header("Idenity Projec[")



# # Tree
# render_basic_tree()




