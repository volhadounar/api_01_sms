import os
import sys
from os.path import abspath
from os.path import dirname

root_dir = dirname(dirname(abspath(__file__)))
sys.path.append(root_dir)

os.environ['ACCOUNT_SID'] = 'AC518aee95826d5273e616ce07d22a5f09'
os.environ['AUTH_TOKEN'] = '2e5cd9d943fe45378fee4f2f0b359b5b'
os.environ['VK_TOKEN'] = 'a754052d2193fc867dd8f5b7f2b6d73740d92912d5d1ce1f2ea4e41125cdc40dccefb01a859ad09632cd7'
os.environ['NUMBER_FROM'] = '+12185173754'
os.environ['NUMBER_TO'] = '+18564145634'

pytest_plugins = [
    'tests.fixtures.fixture_twilio',
    'tests.fixtures.fixture_vk',
]
