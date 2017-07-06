import unittest
import bitstore.helpers as helpers


class GenerateS3PathTest(unittest.TestCase):
    def test___generate_s3_path_works_fine(self):
        in_path = 'path/{owner}/{name}/{md5}/{path}'
        owner = 'datahq'
        name = 'datax'
        path = 'relative/path'
        filedata = {
            "length": 1234,
            "md5": "79f983a99b520ae5111ceaa5b8fa81b9",
            "type": "application/json",
            "name": "datapackage.json"
        }
        expected = 'path/datahq/datax/79f983a99b520ae5111ceaa5b8fa81b9/relative/path'
        result = helpers.generate_s3_path(in_path, path, filedata, owner, name)
        self.assertEqual(expected, result)


    def test___generate_s3_path_errors_if_format_variable_not_available(self):
        in_path = 'path/{owner}/{name}/{md5}/{path}'
        name = 'datax'
        path = 'relative/path'
        filedata = {
            "relative/path": {
                "length": 1234,
                "md5": "79f983a99b520ae5111ceaa5b8fa81b9",
                "type": "application/json",
                "name": "datapackage.json"
            }
        }
        with self.assertRaises(KeyError) as context:
            helpers.generate_s3_path(in_path, path, filedata, name=name)

        in_path = 'path/{unknown}'
        with self.assertRaises(KeyError) as context:
            helpers.generate_s3_path(in_path, path, filedata, name=name)
