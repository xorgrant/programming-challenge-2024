[![Build](https://github.com/xorgrant/programming-challenge-2024/actions/workflows/actions.yaml/badge.svg?branch=main)](https://github.com/xorgrant/programming-challenge-2024/actions/workflows/actions.yaml)

# Programming Challenge (2024)

- [challenge](./challenge/) - Code used to generate the challenge.
- [solution](./solution/) - A solution to the challenge.

## Challenge

![](./assets/programming_challenge_2024.bmp)

There’s a secret message hidden in the image above with the following pattern:

```
___flag{$SECRET_MESSAGE}___

; where $SECRET_MESSAGE := [a-z0-9_]+
```

For example, if you have extracted “`___flag{hello_w0rld}___`”, the `$SECRET_MESSAGE` is the `“hello_w0rld`” part. In your application, please provide the `$SECRET_MESSAGE` and optionally your solution implementation or writeup for the full credit.

## License

**programming-challenge-2024** is under [MIT License](./LICENSE).
