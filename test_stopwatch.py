import time
import unittest

from stopwatch import StopwatchTimer


class TestStopwatchTimer(unittest.TestCase):

    def test_initial_state(self):
        timer = StopwatchTimer()

        self.assertFalse(timer.running)
        self.assertEqual(timer.elapsed_time, 0.0)
        self.assertEqual(timer.get_elapsed_time(), 0.0)

    def test_start(self):
        timer = StopwatchTimer()

        timer.start()

        self.assertTrue(timer.running)
        self.assertIsNotNone(timer.start_time)

    def test_stop_preserves_elapsed_time(self):
        timer = StopwatchTimer()

        timer.start()
        time.sleep(0.1)
        timer.stop()

        self.assertFalse(timer.running)
        self.assertGreater(timer.elapsed_time, 0)

    def test_reset(self):
        timer = StopwatchTimer()

        timer.start()
        time.sleep(0.05)
        timer.stop()
        timer.reset()

        self.assertFalse(timer.running)
        self.assertIsNone(timer.start_time)
        self.assertEqual(timer.elapsed_time, 0.0)
        self.assertEqual(timer.get_elapsed_time(), 0.0)

    def test_resume_after_stop(self):
        timer = StopwatchTimer()

        timer.start()
        time.sleep(0.05)
        timer.stop()

        first_elapsed = timer.elapsed_time

        timer.start()
        time.sleep(0.05)
        timer.stop()

        self.assertGreater(timer.elapsed_time, first_elapsed)


if __name__ == "__main__":
    unittest.main()