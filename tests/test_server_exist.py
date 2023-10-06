import os
def test_server_exist():
    usr_dir = os.path.expanduser('~')
    file_exist = os.path.exists(fr'{usr_dir}')
    assert file_exist