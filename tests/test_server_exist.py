import os
def test_server_exist():
    
    print(usr_dir)
    usr_dir = os.path.expanduser('~')
    file_exist = os.path.exists(fr'{usr_dir}/serverfiles')
    assert file_exist