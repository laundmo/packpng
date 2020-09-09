from app.app_factory import create_app
import unittest 


class FlaskTests(unittest.TestCase): 

    def setUp(self):
        # creates a test client
        self.app = create_app().test_client()
        # propagate the exceptions to the test client
        self.app.testing = True 
    
    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/') 

        # assert the status code of the responses
        self.assertEqual(result.status_code, 200)
    
    def test_faq_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/faq/') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)
    
    def test_contributors_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/contributors/') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)
    
    def test_method_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/method/') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)
        
    def test_timeline_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/timeline/') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)
    
    def test_gallery_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/gallery/') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)
        
    def test_about_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/about/') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)
    
    def test_details_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/details/') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_roadmap_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/roadmap/') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)
        
    def test_panoramasearch_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/panoramasearch/') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)


class ScriptTests(unittest.TestCase): 
    def test_thumbnails(self):
        try:
            import app.static.generate_thumbnails
        except Exception as e:
            self.fail(f"generate_thumbnails.py failed: {e}")
        
