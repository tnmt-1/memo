# My Memo

日々の出来事やプログラミング関連のことなどを書いていきます。

## 環境

- Python3
- rye
    - sphinxです

## インストール

```shell
rye sync
```

## サーバ実行

```shell
rye run sphinx-autobuild docs docs/_build/ -a
```

<http::localhost:8000> で確認できます。
