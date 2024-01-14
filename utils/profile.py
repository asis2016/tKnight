"""
Utility function to retrieve user's info.
"""

__author__ = "Ashish S. Maharjan"
__email__ = "hello@amaharjan.de"
__version__ = "1.0"

import subprocess


def get_profile():
    try:
        #Explanation:
        #stdout=subprocess.PIPE:    to capture the standard output of the command. 
        #text=True:                 treat it as a str
        #stdout:                    we are only interested in stdout and then strip.
        result = {}

        user = subprocess.run(['bash', '-c', 'echo $USER'], stdout=subprocess.PIPE, text=True)
        home = subprocess.run(['bash', '-c', 'echo $HOME'], stdout=subprocess.PIPE, text=True)
        shell = subprocess.run(['bash', '-c', 'echo $SHELL'], stdout=subprocess.PIPE, text=True)
        id = subprocess.run(['bash', '-c', 'id'], stdout=subprocess.PIPE, text=True)
        uname = subprocess.run(['bash', '-c', 'uname -a'], stdout=subprocess.PIPE, text=True)
        etc_passwd = subprocess.run(['bash', '-c', 'grep $USER /etc/passwd'], stdout=subprocess.PIPE, text=True)

        hardware_vendor_cmd = 'hostnamectl | grep "Hardware Vendor"'
        hardware_vendor = subprocess.run(['bash', '-c', f'{hardware_vendor_cmd}'], stdout=subprocess.PIPE, text=True)
        vendor = hardware_vendor.stdout.strip().split(':')[1]

        hardware_model_cmd = 'hostnamectl | grep "Hardware Model"'
        hardware_model = subprocess.run(['bash', '-c', f'{hardware_model_cmd}'], stdout=subprocess.PIPE, text=True)
        model = hardware_model.stdout.strip().split(':')[1]

        architecture_cmd = 'hostnamectl | grep Architecture'
        architecture = subprocess.run(['bash', '-c', f'{architecture_cmd}'], stdout=subprocess.PIPE, text=True)
        architecture = architecture.stdout.strip().split(':')[1]

        kernel_cmd = 'hostnamectl | grep Kernel'
        kernel_response = subprocess.run(['bash', '-c', f'{kernel_cmd}'], stdout=subprocess.PIPE, text=True)
        if kernel_response:
            kernel = kernel_response.stdout.strip().split(':')[1]
            result['kernel'] = kernel

        #result
        result['user'] = user.stdout.strip()
        result['home'] = home.stdout.strip()
        result['shell'] = shell.stdout.strip()
        result['id'] = id.stdout.strip()
        result['unameA'] = uname.stdout.strip()
        result['etcPasswd'] = etc_passwd.stdout.strip()
        result['hardwareVendor'] = vendor
        result['hardwareModel'] = model
        result['architecture'] = architecture

        return {'result': result}         

    except Exception as e:
        error = f'Error: {str(e)}'
        return {'error' : error}