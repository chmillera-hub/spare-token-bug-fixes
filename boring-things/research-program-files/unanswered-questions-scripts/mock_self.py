# Three ways to replace a method in a test with a quick stand-in that uses self (Python forum topic 104184)
import sys, unittest, unittest.mock

class Pipeline:
    def __init__(self): self.a = 2
    def very_expensive_method(self): self.a = self.a ** 100

def quick_method(self): self.a = 3

class TestPipeline(unittest.TestCase):
    def test_0_posted_version_fails(self):
        with unittest.mock.patch.object(Pipeline, "very_expensive_method") as m:
            m.side_effect = quick_method
            with self.assertRaises(TypeError):
                Pipeline().very_expensive_method()

    def test_1_new_plain_function(self):
        # a plain function put on the class becomes a normal method, so self arrives by itself
        with unittest.mock.patch.object(Pipeline, "very_expensive_method", new=quick_method):
            p = Pipeline(); p.very_expensive_method()
        self.assertEqual(p.a, 3)

    def test_2_autospec_with_side_effect(self):
        # autospec keeps the call record, and the record includes the instance as first argument
        with unittest.mock.patch.object(Pipeline, "very_expensive_method", autospec=True, side_effect=quick_method) as m:
            p = Pipeline(); p.very_expensive_method()
        self.assertEqual(p.a, 3); m.assert_called_once_with(p)

    def test_3_patch_on_the_instance(self):
        # patching one object: the stand-in closes over that object, and other objects keep the real method
        p = Pipeline()
        with unittest.mock.patch.object(p, "very_expensive_method", side_effect=lambda: quick_method(p)) as m:
            p.very_expensive_method()
        self.assertEqual(p.a, 3); m.assert_called_once_with()

    def test_4_original_method_is_back_afterwards(self):
        p = Pipeline(); p.very_expensive_method()
        self.assertEqual(p.a, 2 ** 100)

if __name__ == "__main__":
    print("Python", sys.version.split()[0])
    unittest.main(verbosity=2)
