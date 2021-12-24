import sys, os, json

current_path = os.getcwd()
script_path = sys.path[0]

def main():
    package_path = ''.join((current_path, '/package.json'))

    package_file = open(package_path, 'r')

    data = json.load(package_file)

    data['scripts']['stop'] = 'pm2 kill'
    data['scripts']['start'] = 'pm2 start index.js'
    data['scripts']['list'] = 'pm2 list'
    data['scripts']['restart'] = 'pm2 restart index.js'

    package_file_write = open(package_path, 'w')

    json.dump(data, package_file_write, indent=2)

    