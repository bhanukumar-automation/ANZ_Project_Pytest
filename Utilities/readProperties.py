from configparser import ConfigParser


config = ConfigParser()
config_file_path = "..\\Configurations\\config.ini"
print(config_file_path)
config.read(config_file_path)


class ReadConfig:
    try:
        @staticmethod
        def get_app_url():
            url= config.get("commonInfo", "baseurl")
            return url


        @staticmethod
        def get_chrome_driver_path():
            chrome_drive_path= config.get("commonInfo", "chrome_driver")
            return chrome_drive_path


        @staticmethod
        def get_edge_driver_path():
            chrome_drive_path = config.get("commonInfo", "edge_driver")
            return chrome_drive_path

    except Exception as err:
        print("Configuration Error : ", err)

    finally:
        print("All Config file values fetched")
