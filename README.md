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
首先了解一下需要什么样格式的 JSON 数据，大概是长这样的

假设你有一份数据需要生产树图，大概长这样
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

接下来之执行 ```pytm-cli -i data.json -o demo.html``，然后用浏览器打开根目录下的 demo.html 文件，就可以看到已经生产了这样的一张图了

![]()

当指定 -t/--type 参数为 3 时，得到的图是这样的

![]()

