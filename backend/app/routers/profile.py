__author__ = 'amaharjan.de'

from fastapi import APIRouter
import subprocess
from ..logger import log

router = APIRouter()

@router.get('/profile/', tags=['System Info'])
def read_profile():
    '''
    Return "for profile page"
    '''
    log.info('/profile/ requested.')

    result = {}
    
    #Explanation:
        #stdout=subprocess.PIPE:    to capture the standard output of the command. 
        #text=True:                 treat it as a str
        #stdout:                    we are only interested in stdout and then strip.
    user = subprocess.run(['bash', '-c', 'echo $USER'], stdout=subprocess.PIPE, text=True)
    result['user'] = user.stdout.strip()

    home = subprocess.run(['bash', '-c', 'echo $HOME'], stdout=subprocess.PIPE, text=True)
    result['home'] = home.stdout.strip()

    shell = subprocess.run(['bash', '-c', 'echo $SHELL'], stdout=subprocess.PIPE, text=True)
    result['shell'] = shell.stdout.strip()

    id = subprocess.run(['bash', '-c', 'id'], stdout=subprocess.PIPE, text=True)
    result['id'] = id.stdout.strip()

    uname = subprocess.run(['bash', '-c', 'uname -a'], stdout=subprocess.PIPE, text=True)
    result['unameA'] = uname.stdout.strip()

    etc_passwd = subprocess.run(['bash', '-c', 'grep $USER /etc/passwd'], stdout=subprocess.PIPE, text=True)
    result['etcPasswd'] = etc_passwd.stdout.strip()

    hardware_vendor_cmd = 'hostnamectl | grep "Hardware Vendor"'
    hardware_vendor = subprocess.run(['bash', '-c', f'{hardware_vendor_cmd}'], stdout=subprocess.PIPE, text=True)
    vendor = hardware_vendor.stdout.strip().split(':')[1]
    result['hardwareVendor'] = vendor

    hardware_model_cmd = 'hostnamectl | grep "Hardware Model"'
    hardware_model = subprocess.run(['bash', '-c', f'{hardware_model_cmd}'], stdout=subprocess.PIPE, text=True)
    model = hardware_model.stdout.strip().split(':')[1]
    result['hardwareModel'] = model

    architecture_cmd = 'hostnamectl | grep Architecture'
    architecture = subprocess.run(['bash', '-c', f'{architecture_cmd}'], stdout=subprocess.PIPE, text=True)
    architecture = architecture.stdout.strip().split(':')[1]
    result['architecture'] = architecture

    kernel_cmd = 'hostnamectl | grep Kernel'
    kernel_response = subprocess.run(['bash', '-c', f'{kernel_cmd}'], stdout=subprocess.PIPE, text=True)
    if kernel_response:
        kernel = kernel_response.stdout.strip().split(':')[1]
        result['kernel'] = kernel

    return {'result': result}
