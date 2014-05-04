from mock import Mock

class ConfigParserTest(unittest.TestCase):

    def test_should_instantiate(self):
        # Set
        conf_parser = ConfigParser()

        # Assertion
        self.assertIsInstance(conf_parser, ConfigParser)
        self.assertIn('src', conf_parser.path)

    def test_should_read(self):
        # Set
        conf_parser = ConfigParser()
        config_file_content = {'API Key': '1111', 'App ID': '777'}

        # Mocks
        json.load = Mock(return_value=config_file_content)

        # Assertion
        self.assertEqual(config_file_content, conf_parser.read('config.json'))
        self.assertEqual(config_file_content, conf_parser.raw_config)
        json.load.assert_called_once()
