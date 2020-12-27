import logging
from logging import handlers
import os
"""
解决乱码问题两种方式：
1、修改底层代码logging的init文件FileHandler(StreamHandler)，encoding默认给utf-8格式
2、通过输出流来读取文件，filename= 替换stream=file来打开文件，弊端，文件需一直打开，操作的时候
# file = open('../log/runlog.log',encoding="utf-8", mode="a")#修改输出流，防止中文乱码
"""

logging.basicConfig(filename= '../log/runlog.log',level=logging.INFO,
                    format="%(asctime)s ""%(filename)s [line:%(lineno)d] ""%(levelname)s>""%(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S"
                    ,filemode='a'
                    )
logger = logging.getLogger()
logger.setLevel(logging.INFO)