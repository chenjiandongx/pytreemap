# 树图渲染命令行工具
本项目打包了 [antvis/g6](https://github.com/antvis/g6)，利用 JSON 数据生成 HTML 格式的树图


### 安装
#### pip 安装
```
$ pip install pytm-cli
```

#### 源码安装
```
 $ git clone https://github.com/chenjiandongx/pytreemap.git
 $ cd torrent-cli
 $ pip install -r requirements.txt
 $ python setup.py install
 ```

### 使用

#### 命令行参数

```
C:\Users\chenjiandongx>pytm-cli
usage: pytm-cli [-i INPUT] [-o OUTPUT] [-d DIRECTION] [-t TYPE] [-v] [-h]

树图渲染命令行工具-利用 JSON 数据生成 HTML 格式的树图

optional arguments:
  -i INPUT, --input INPUT
                        JSON 数据路径.
  -o OUTPUT, --output OUTPUT
                        输出 HTML 文件路径.(默认为`.\TreeMap.html`)
  -d DIRECTION, --direction DIRECTION
                        树图的布局方向, 有 LR/RL/H/TB/BT/V 可选.(默认为 LR)
  -t TYPE, --type TYPE  树图类型, 1.分层树 2.缩进树 3.生态树.(默认为 1)
  -v, --version         版本信息
  -h, --help            帮助页面

```

#### JSON 数据

首先假设你有一份数据需要生产树图，大概长这样
```
     |----B     |----E----|----I
     |          |
     |----C-----|----F         |----J
A----|                         |
     |----D-----|----G----|----|----K
                |
                |----H
```

这时候思路就很清晰了，你需要来编写成 JSON 数据了，节点都是以 {name, children} 为基础的递归嵌套模式，如下
```
{
    "children": [
        {
            "children": [],
            "name": "B"
        },
        {
            "children": [
                {
                    "children": [
                        {
                            "children": [],
                            "name": "I"
                        }
                    ],
                    "name": "E"
                },
                {
                    "children": [],
                    "name": "F"
                }
            ],
            "name": "C"
        },
        {
            "children": [
                {
                    "children": [
                        {
                            "children": [],
                            "name": "J"
                        },
                        {
                            "children": [],
                            "name": "K"
                        }
                    ],
                    "name": "G"
                },
                {
                    "children": [],
                    "name": "H"
                }
            ],
            "name": "D"
        }
    ],
    "name": "A"
}

```
怎么样，结构很清晰吧，将文件保存为 json 格式，如 data.json


#### 生成树图

接下来之执行 ```pytm-cli -i data.json -o demo.html``，然后用浏览器打开根目录下的 demo.html 文件，就可以看到已经生产了这样的一张图了

![](https://github.com/chenjiandongx/pytreemap/blob/master/screenshot/screenshot-0.png)

当指定 -t/--type 参数分别为 2 3 时，得到的图是这样的

type 为 2

![](https://github.com/chenjiandongx/pytreemap/blob/master/screenshot/screenshot-1.png)

type 为 3

![](https://github.com/chenjiandongx/pytreemap/blob/master/screenshot/screenshot-2.png)

其余参数尝试一下就知道效果了，这里提供官网提供的 [数据](https://github.com/chenjiandongx/pytreemap/blob/master/json/data.json) 生产的效果

```pytm-cli -i data.json``

![](https://github.com/chenjiandongx/pytreemap/blob/master/screenshot/screenshot-3.png)

```pytm-cli -i data.json -d H``

![](https://github.com/chenjiandongx/pytreemap/blob/master/screenshot/screenshot-4.png)

```pytm-cli -i data.json -t 3``

![](https://github.com/chenjiandongx/pytreemap/blob/master/screenshot/screenshot-5.png)

### 以模块方式使用

```python
from pytreemap import render

render('data.json', type, direction, outpath)
```

### MIT 许可证
