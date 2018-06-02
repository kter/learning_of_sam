# How To Run

```
$ echo '{"key1": "this is key1", "key2": "this is key2", "key3": "this is key3"}' | sam local invoke helloworldpython3
2018-06-02 18:38:03 Reading invoke payload from stdin (you can also pass it from file with --event)
2018-06-02 18:38:03 Invoking lambda_function.lambda_handler (python3.6)
2018-06-02 18:38:03 Found credentials in shared credentials file: ~/.aws/credentials

Fetching lambci/lambda:python3.6 Docker container image......
2018-06-02 18:38:06 Mounting /Users/kter/workspace/learning_of_sam/hello-world-python3 as /var/task:ro inside runtime container
START RequestId: e075e63a-0a92-4ae4-906d-8c95bf78e422 Version: $LATEST
Loading function
value1 = this is key1
value2 = this is key2
value3 = this is key3
END RequestId: e075e63a-0a92-4ae4-906d-8c95bf78e422
REPORT RequestId: e075e63a-0a92-4ae4-906d-8c95bf78e422 Duration: 17 ms Billed Duration: 100 ms Memory Size: 128 MB Max Memory Used: 19 MB

"this is key1"
```
