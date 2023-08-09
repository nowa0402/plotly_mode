import xml.etree.ElementTree as ET
from pathlib import Path

# xmlで読み込んだgタグ
SVG_G_TAG = "{http://www.w3.org/2000/svg}g"

input_path = Path("./output.svg")
template_path = Path("./legend_template.svg")

tree = ET.parse(input_path)
root = tree.getroot()


# 大元gタグから情報レイヤー取得
g_elems = root.findall(SVG_G_TAG)
info_elems = next(filter(lambda x: x.attrib["class"] == "infolayer", g_elems))

# 情報一覧から凡例取得
layer_elems = info_elems.findall(SVG_G_TAG)
legend_elems = next(filter(lambda x: x.attrib["class"] == "legend", layer_elems))


# テンプレートから凡例タグ取得
template_tree = ET.parse(template_path)
template_root = template_tree.getroot()
template_legend = template_root.find(f"{SVG_G_TAG}/{SVG_G_TAG}")
if template_legend is None:
    raise

# テンプレートに凡例を追加
[template_legend.append(elem) for elem in legend_elems]


# 結果反映
template_tree = ET.ElementTree(template_root)

# ns:0対策
namespaces = {
    node[0]: node[1] for _, node in ET.iterparse(template_path, events=["start-ns"])
}
for key, value in namespaces.items():
    ET.register_namespace(key, value)

# 凡例出力
legend_output_path = Path("./legend.svg")
template_tree.write(legend_output_path)

# 元画像から凡例削除
info_elems.remove(legend_elems)

# 変更反映
tree = ET.ElementTree(root)

# ns:0対策
target_namespaces = {
    node[0]: node[1] for _, node in ET.iterparse(input_path, events=["start-ns"])
}
for key, value in target_namespaces.items():
    ET.register_namespace(key, value)

# グラフ出力
graph_output_path = Path("./graph.svg")
tree.write(graph_output_path)
