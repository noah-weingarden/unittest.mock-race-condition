This repo is a minimal reproducible example of a race condition in `unittest.mock`. See [GitHub issue link here].

To demonstrate, run `python3 mre.py`. You should see output like this every time you run the test:

```
Test called sendall(), pausing and letting main() continue
main() finished creating sendall() mock, letting test continue
main() sendall() mock: <MagicMock name='socket().__enter__().sendall' id='140244035862144'>
Test resuming call to sendall()
Test sendall() mock: <MagicMock name='socket().__enter__().sendall' id='140244035739248'>
F
======================================================================
FAIL: test_message_sent (__main__.MockTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/noah/unittest-mock-mre/mre.py", line 20, in test_message_sent
    sendall.assert_called()
  File "/home/noah/unittest-mock-mre/mock.py", line 908, in assert_called
    raise AssertionError(msg)
AssertionError: Expected 'sendall' to have been called.

----------------------------------------------------------------------
Ran 1 test in 0.012s

FAILED (failures=1)
```
