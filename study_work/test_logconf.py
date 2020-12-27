import logging
import logging.config
#读取日志配置文件，启动日志捕捉
CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)#从config格式的文件中读取，如果脚本有配置log参数，则会覆盖默认的log配置项
logging = logging.getLogger()

logging.info('testrizhi你这个可以吗？')