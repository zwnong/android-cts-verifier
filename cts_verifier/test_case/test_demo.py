#!coding = utf -8
import pytest

from base.base_driver import BaseDriver


class TestDemo:
    def setup_class(self):
        driver = BaseDriver()
        self.driver = driver.android_driver(
            'DVKS232D20110300016',
            "com.android.cts.verifier",
            "com.android.cts.verifier.CtsVerifierActivity",
            4723
        )

    def setup(self):
        pass

    def teardown(self):
        pass

    def teardown_class(self):
        self.driver.quit()

    # pip install pytest-ordering
    @pytest.mark.run(order=1)
    def test_audioAcoustic_echo_cancellation_AEC_Test(self):
        """
        进入Audio Acoustic Echo Cancellation（AEC）Test测试，此测试项需要安静的环境，无需插耳机。
        单击Yes按钮，再单击TEST
        :return:
        """
        # test = self.app.goto_main_page().audio_acoustic_echo_cancellation_AEC_test()
        self.driver.find_element_by_xpath('//*[@resource-id="android:id/text1" and @text="Audio Acoustic Echo Cancellation (AEC) Test"]').click()
