import logging
from logging import handlers
import os

"""
1、更高级的日志切割封装，目前为了展示效果按S切割日志
2、按每S切割，每次最新日志输出到runlog.log里面，就的日志进行时间切割
"""
def _logging(**kwargs):
  level = kwargs.pop('level', None)
  filename = kwargs.pop('filename', None)
  datefmt = kwargs.pop('datefmt', None)
  format = kwargs.pop('format', None)
  if level is None:
    level = logging.DEBUG
  if filename is None:
    filename = '../log/runlog.log'
  if datefmt is None:
    datefmt = '%Y-%m-%d %H:%M:%S'
  if format is None:
    format = '%(asctime)s [%(filename)s] [%(lineno)d] %(levelname)s %(message)s'
  log = logging.getLogger(filename)
  format_str = logging.Formatter(format, datefmt)
  def split_namer(filename):
    return filename.split('runlog.log.')[1]
  # backupCount 保存日志的数量，过期自动删除
  # when 按什么日期格式切分(这里方便测试使用的秒)
  if not os.path.exists('../log'):#判断目录是否存在
    os.makedirs('../log')
  th_debug = handlers.TimedRotatingFileHandler(filename=filename, when='S', backupCount=1,
                                               encoding='utf-8')
  th_debug.namer = split_namer
  th_debug.suffix = '../log/'+"%Y-%m-%d_%H-%M-%S.log"
  th_debug.setFormatter(format_str)
  # th_debug.setLevel(logging.DEBUG)
  log.addHandler(th_debug)
  log.setLevel(level)
  return log