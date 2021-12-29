import sys, os, json, subprocess

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
    # data['dependencies']['pm2'] = '*'

    json_object = json.dumps(data, indent=2)

    with open(package_path, 'w') as package_file_write:
        package_file_write.write(json_object)

    push_changes_path = ''.join((script_path, '/push_changes.sh'))

    subprocess.call(['sh', push_changes_path])