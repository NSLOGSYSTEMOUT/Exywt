


# ConfigParser用于生成和修改常见配置文件

import  configparser

config = configparser.ConfigParser()

config['DEFAULT'] = {

    'ServerAliveInterval':'45',
    'Compression'        :'yes',
    'CompressionLevel'   :'9'
}

config['bitbucket.org'] = {'User':'hg'}
# config['bitbucket.org']['User'] = 'hg'
# config['topsecreat.server.com'] = {}

# config['topsecret.server.com'] = {}
# topsecret = config['topsecret.server.com']
#
# topsecret['Host Port'] = '50022'
# topsecret['ForwardX11'] = 'no'
# topsecret['DEFAULT']['ForwardX11'] = 'yes'


with open('example.ini','w' ) as  configfile:
    config.write(configfile)



config.read('example.ini')
print(config.sections())
print(config['bitbucket.org']['User'])          #hg

# config.remove_option('bitbucket.org','User')
#
# config.set('bitbucket.org','User', 'zs')
# config.write(open('example.ini','w'))