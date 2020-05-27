import datetime
from Cryptodome.Cipher import DES
from Cryptodome.Cipher import AES


BLOCK_SIZE = 16


# 错误日志记录
def error_log(error):
    with open('error_log.txt', 'a') as f:
        f.write(str(datetime.datetime.now()) +
                ': ' + str(error) + '\n')


# 填充数据
def pad(data):
    return data + (BLOCK_SIZE - len(data) % BLOCK_SIZE) * \
               chr(BLOCK_SIZE - len(data) % BLOCK_SIZE).encode()


# 去掉填充的数据
def un_pad(data):
    return data[:-ord(data[len(data) - 1:])]


# DES加密——ECB模式
def des_encrypt_ecb(data, key):
    try:
        data = pad(data)
        des = DES.new(key.encode('utf-8'), DES.MODE_ECB)
        encrypted_data = des.encrypt(data)
        return encrypted_data
    except Exception as e:
        error_log(e)
        return False


# DES解密——ECB模式
def des_decrypt_ecb(data, key):
    try:
        des = DES.new(key.encode('utf-8'), DES.MODE_ECB)
        plain_data = des.decrypt(data)
        plain_data = un_pad(plain_data)
        return plain_data
    except Exception as e:
        error_log(e)
        return False


# DES加密——CBC模式
def des_encrypt_cbc(data, key, vi):
    try:
        data = pad(data)
        des = DES.new(key.encode('utf-8'), DES.MODE_CBC, vi.encode('utf-8'))
        encrypted_data = des.encrypt(data)
        return encrypted_data
    except Exception as e:
        error_log(e)
        return False


# DES解密——CBC模式
def des_decrypt_cbc(data, key, vi):
    try:
        des = DES.new(key.encode('utf-8'), DES.MODE_CBC, vi.encode('utf-8'))
        plain_data = des.decrypt(data)
        plain_data = un_pad(plain_data)
        return plain_data
    except Exception as e:
        error_log(e)
        return False


# AES加密——CBC模式
def aes_encrypt_cbc(data, key, vi):
    try:
        data = pad(data)
        cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, vi.encode('utf-8'))
        encrypted_data = cipher.encrypt(data)
        return encrypted_data
    except Exception as e:
        error_log(e)
        return False


# AES解密——CBC模式
def aes_decrypt_cbc(data, key, vi):
    try:
        cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, vi.encode('utf-8'))
        plain_data = cipher.decrypt(data)
        plain_data = un_pad(plain_data)
        return plain_data
    except Exception as e:
        error_log(e)
        return False


# AES加密——ECB模式
def aes_encrypt_ecb(data, key):
    try:
        key = key.encode('utf-8')
        data = pad(data)
        cipher = AES.new(key, AES.MODE_ECB)
        encrypted_data = cipher.encrypt(data)
        return encrypted_data
    except Exception as e:
        error_log(e)
        return False


# AES解密——ECB模式
def aes_decrypt_ecb(data, key):
    try:
        key = key.encode('utf-8')
        cipher = AES.new(key, AES.MODE_ECB)
        plain_data = cipher.decrypt(data)
        plain_data = un_pad(plain_data)
        return plain_data
    except Exception as e:
        error_log(e)
        return False


if __name__ == '__main__':
    data = '123 '

    print('AES_ECB: ')
    en = aes_encrypt_ecb(data.encode(), '1234567812345678')
    print(en)
    de = aes_decrypt_ecb(en, '1234567812345678')
    print(de)

    print('\nDES_ECB: ')
    en = des_encrypt_ecb(data.encode(), '12345678')
    print(en)
    de = des_decrypt_ecb(en, '12345678')
    print(de)

    print('\nDES_CBC: ')
    en = des_encrypt_cbc(data.encode(), '12345678', '12345678')
    print(en)
    de = des_decrypt_cbc(en, '12345678', '12345678')
    print(de)

    print('\nAES_CBC: ')
    en = aes_encrypt_cbc(data.encode(), '12345678123456781234567812345678', '1234567812345678')
    print(en)
    de = aes_decrypt_cbc(en, '12345678123456781234567812345678', '123456781234567812345678')
    print(de)
