# Get-Encrypted-Param

This is an example of getting 抖音/TikTok encryption algorithm parameters

For example to get x_ladon,x_gorgon,x_argus,x_cylons

## Running the tests
#### REQUEST - [Example one](demo/get_param.py)
        @staticmethod
        def get_x_ladon():
            param1 = XLadon.decrypt("ltCyalMN4I88MKaornPKU+LSy5Tl6jDZcJFrMF3eokqTucfp")
            print(param1)

            param2 = XLadon.encrypt(1646098215, "1225625952")
            print(param2)

            param3 = XLadon.decrypt(param2)
            print(param3 == param1)
#### RESULT
        96edab6bc5bf2fbc0000000021080304621d7727
        8404e03220003523b7c16d6cea06cece05f6e6c9d178d376f661
        True

## Environment requirements

Test with China version,To test the American version or the European version,you need to replace the data in [this](demo/bean/device_info.py) 

        Support iOS
        Python 3.9.7
        PyCharm 2022.2.1
        app_version = '22.0.0'

## Tip

This project only tests and verifies the research related to algorithms, and it is the old version used. I hope it will not cause problems. Welcome to discuss with each other!

