import subprocess
import unittest

class TestDockerSetup(unittest.TestCase):
    def test_build_image(self):
        result = subprocess.run(["docker", "build", "."], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertEqual(result.returncode, 0, "Docker image build failed")

    def test_run_containers(self):
        result = subprocess.run(["docker-compose", "up", "-d"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertEqual(result.returncode, 0, "Docker containers failed to start")
