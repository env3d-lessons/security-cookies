import os
import pytest
import pathlib
import base64

def test_q1():
    # Simply test if it exists
    assert pathlib.Path('q1.txt').is_file()

def test_q2_no_password():    
    cmd = f'./q2.sh'
    content = os.popen(cmd).read()
    assert '401' in content

@pytest.fixture
def q2_content():
    idpass = base64.b64encode(b'a:b')    
    cmd = f'HTTP_AUTHORIZATION="Basic {idpass}" ./q2.sh'
    content = os.popen(cmd).read()
    return content

def test_q2_status(q2_content):
    assert '200' in q2_content

def test_q2_cookie(q2_content):
    assert 'JWT' in q2_content

def test_q3_no_cookies():    
    cmd = './q3.sh'
    content = os.popen(cmd).read()
    assert '401' in content

def test_q3_invalid_jwt():
    jwt = 'asdf'
    cmd = f'HTTP_COOKIE="JWT={jwt}" ./q3.sh'
    content = os.popen(cmd).read()
    assert '401' in content

def test_q3_valid_jwt():
    jwt = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImFiY2RlIiwiZXhwIjoiMTcyMDc1MTg1OSJ9.5RAFekCOkcrUsv_kjQjau9U26ETjTw6dd1MLJlkajoU'
    cmd = f'HTTP_COOKIE="JWT={jwt}" ./q3.sh'
    content = os.popen(cmd).read()
    assert '401' not in content
