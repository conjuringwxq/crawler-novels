from pyecharts import Bar

attr =['衬衫','羊毛衫','雪纺衫','裤子','鞋','袜子']
value = [15, 20, 36, 40, 75, 90]
bar = Bar('柱状图', '销量统计')
bar.add('服装', attr, value, is_label_show=True)
bar.render()